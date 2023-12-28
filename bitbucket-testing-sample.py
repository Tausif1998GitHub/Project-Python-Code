import socket

def check_server_status(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            s.shutdown(socket.SHUT_RDWR)  # Close immediately
            return True  # Server is up
        except ConnectionRefusedError:
            return False  # Server is not running

bitbucket_host = "43.205.206.172"
bitbucket_port = 7990

if check_server_status(bitbucket_host, bitbucket_port):
    print("Bitbucket server is up and running!")
else:
    print("Bitbucket server is not responding.")
