import os

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    app_version = os.environ['FLASK_APP_VERSION']
    return render_template('hello.html', app_version=app_version)
