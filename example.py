from flask import Flask

app = Flask(__name__)


@app.route("/u")
def greeting():
    return 'Hello World'

@app.route("/calculator/add/<int:a>/<int:b>")
def add(a,b):
    return "sum is "+str(a+b)

@app.route("/calculator/subtract/<int:a>/<int:b>")
def subtract(a,b):
    return "diff is "+str(a-b)

if __name__ == '__main__':
    app.run()

