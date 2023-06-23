from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, emit ,SocketIO
import random
from string import ascii_uppercase
import openai


app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
# app.config["APPLICATION_ROOT"] = "/encrypted"
app.static_folder = 'static'
app.debug = True
socketio = SocketIO(app , port=5000 )

rooms = {}

# Store active users
active_users = set()

# Set up the OpenAI API client
openai.api_key = "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"
# Set up the model and prompt
model_engine = "text-davinci-003"



def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code

@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)

        if join != False and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
        
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template("home.html")

@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))

    return render_template("room.html", code=room, messages=rooms[room]["messages"])

@app.route("/doctor", methods=["POST", "GET"])
def doctor():
    return render_template("doctor.html")
    
    
@socketio.on("message")
def message(data):
    room = session.get("room")
    name = session.get("name")
    if room not in rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")
    
    prompt = data["data"]
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(completion.choices[0].text)
    response = {
    "name": "Dr FixUrIssues Tan",
    "message": completion.choices[0].text
    }
    send(response, to=room)
    rooms[room]["messages"].append(response)
    print(f"{'Dr FixUrIssues Tan'} said: {completion.choices[0].text}")

@socketio.on("connect")
def connect(auth):
    
    active_users.add(request.sid)
    emit('user_status', {'user': request.sid, 'status': 'online'}, broadcast=True)
    
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    
    join_room(room)
    
    if (name =="test"):
        send({"name": "Dr FixUrIssues Tan", "message": "has entered the room"}, to=room)
        send({"name": "Dr FixUrIssues Tan", "message": "How are you today? How may I help?"}, to=room)
    
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    
    active_users.remove(request.sid)
    emit('user_status', {'user': request.sid, 'status': 'offline'}, broadcast=True)
    
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")

@socketio.on('ping')
def handle_ping():
    emit('pong', {'user': request.sid})

@socketio.on('pong')
def handle_pong():
    # Optional: Add custom logic here if desired
    active_users.add(request.sid)
    pass


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0' , allow_unsafe_werkzeug=True )