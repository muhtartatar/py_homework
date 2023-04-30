from flask import Flask

app = Flask(__name__)


@app.rout("/")
def hello_world():
    return "<h3>Hello World!!!<h3>"


#if __name__ == "__maim__":
    #app.run(host='0.0.0.0', port=8000, debug=True)