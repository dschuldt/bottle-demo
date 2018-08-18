import bottle, socket
from bottle import route, run

app = bottle.default_app()

@route('/')
def info():
    version = '1.0'
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return 'Bottle Demo v{0} running on {1} ({2})'.format(version, hostname, ip)

if __name__ == "__main__":
    run(host='localhost', port=8080)
