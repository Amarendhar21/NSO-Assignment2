import flask
import time
import socket


host_name = socket.gethostname()
IP_address = socket.gethostbyname(host_name)


app = flask.Flask(__name__)

@app.route('/')
def index():
    Time = time.strftime("%H:%M:%S")
    return Time+" Serving from "+host_name+" ("+IP_address+")\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
