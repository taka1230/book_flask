from flask import Flask

app =Flask(__name__)

@app.route('/')
def hello_world():
    return "hi flask"

if __name__ == '__main__':
    print(__name__)
    app.run(host='0.0.0.0', port=1991, debug=True)
