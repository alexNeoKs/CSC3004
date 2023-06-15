import socket
import ssl
import pprint

if __name__ == '__main__':

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="client/certs/ca-certificates.crt")
    context.load_cert_chain(certfile="client/certs/client.crt", keyfile="client/certs/client.key")
    print("SSL context created")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = context.wrap_socket(s, server_side=False, server_hostname="*.chatserver.com")
    conn.connect(("127.0.0.1", 8080))
    print("SSL established. Peer: {}".format(conn.getpeercert()))
    print("Sending: 'Hello, world!")
    conn.send(b"Hello, world!")
    print("Closing connection")
    conn.close()

#-----------------------------------------------------------------------------------------------
# python client/client.py
#-----------------------------------------------------------------------------------------------
# openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt