from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
