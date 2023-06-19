import socket
import ssl
import threading

def handleClient(conn):
    buf = ""  # Buffer to hold received client data
    try:
        while True:
            try:
                data = conn.recv(4096)
                if data:
                    buf += str(data.decode('utf-8'))
                else:
                    print("###########################################################################################################")
                    print("Received:", buf , "\n")
                    print("###########################################################################################################")
                    buf = b''
                    break
            except socket.error:
                print("###########################################################################################################")
                print("Closing connection (Unexpected client termination)")
                print("###########################################################################################################")
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
            else:
                    print("###########################################################################################################")
                    print("Received:", buf , "\n" )
                    print("###########################################################################################################")
                    break
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
    finally:
        print("###########################################################################################################")
        print("Closing connection (Client shutdown)")
        print("###########################################################################################################")
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

if __name__ == '__main__':

    threads = list()

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain(certfile="server/certs/server.crt", keyfile="server/certs/server.key")
    context.load_verify_locations(cafile="server/certs/ca-certificates.crt")

    bindsocket = socket.socket()
    bindsocket.bind(("127.0.0.1", 8080))
    bindsocket.listen(15)

    while True:
        try:
            print("###########################################################################################################")
            print("Waiting for client")
            print("###########################################################################################################")

            newsocket, fromaddr = bindsocket.accept()
            print("###########################################################################################################")
            print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
            print("###########################################################################################################")

            conn = context.wrap_socket(newsocket, server_side=True)
            print("###########################################################################################################")
            print("SSL established. Peer: {}".format(conn.getpeercert()))
            print("###########################################################################################################")

            x = threading.Thread( target=handleClient , args=(conn,) )
            x.start()

        except Exception as e:
            print(f"An exception occurred: {str(e)}")
        
#-----------------------------------------------------------------------------------------------
# python server/server.py
#-----------------------------------------------------------------------------------------------
# openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt