import socket
import ssl
import pprint

if __name__ == '__main__':

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain(certfile="server/certs/server.crt", keyfile="server/certs/server.key")
    context.load_verify_locations(cafile="server/certs/ca-certificates.crt")

    bindsocket = socket.socket()
    bindsocket.bind(("127.0.0.1", 8080))
    bindsocket.listen(10)

    while True:
        print("Waiting for client")
        newsocket, fromaddr = bindsocket.accept()
        print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
        conn = context.wrap_socket(newsocket, server_side=True)
        print("SSL established. Peer: {}".format(conn.getpeercert()))
        buf = b''  # Buffer to hold received client data
        try:
            while True:
                data = conn.recv(4096)
                if data:
                    # Client sent us data. Append to buffer
                    buf += data
                else:
                    # No more data from client. Show buffer and close connection.
                    print("Received:", buf)
                    break
        finally:
            print("Closing connection")
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
#-----------------------------------------------------------------------------------------------
# python server/server.py
#-----------------------------------------------------------------------------------------------
# openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt