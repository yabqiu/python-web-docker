from uuid import uuid4
import socket, os
from flask import Flask, request

app = Flask(__name__)
host_uid = str(uuid4()).split('-')[0]

@app.route('/')
def index():
    hostname = socket.gethostname()
    return 'Served by {}/{}\n'.format(hostname, host_uid)

if __name__ == '__main__':
    print('host uid: ' + host_uid)
    app.run(host='0.0.0.0', debug=False,
            port=int(os.getenv('HTTP_PORT', '80')))
