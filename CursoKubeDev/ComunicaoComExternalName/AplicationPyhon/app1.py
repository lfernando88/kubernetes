from app import *
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def main():
    # return socket.gethostname()

    for musica_id in range(album.estimated_document_count()):
        album.find_one({"_id": musica_id})
        return album.find_one()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
