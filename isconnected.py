import socket
def is_connected():
    try:
        socket.create_connection(('www.google.com',80))
        return True
    except OSError:
        pass
    return False

def check_connection():
    if not is_connected():
        raise Exception("Problem with connectivity")
