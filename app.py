from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello GUVI GEEK networks this is MANIKANTARAJU DIBBIDI D07 DEVOPS GUVI"

if __name__ == '__main__':
    # Listen on all available network interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)
