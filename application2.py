import Flask
import time
import socket


host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)


app = Flask(__name__)

@app.route('/')
def index():
    current_time = time.strftime("%H:%M:%S")
    return f"{current_time} - Serving from {"host_name"} "({ip_address})\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

