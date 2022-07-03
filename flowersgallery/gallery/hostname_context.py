import socket


def hostname(request):
    try:
        HOSTNAME = socket.gethostname()
    except:
        HOSTNAME = 'localhost'
    return { "hostname": HOSTNAME }
