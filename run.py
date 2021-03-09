
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<hi>Welcome to e-Kazi</h1>"


if __name__ == '__main__':
    app.run(debug =True)