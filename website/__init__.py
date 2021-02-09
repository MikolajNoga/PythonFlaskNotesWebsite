from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'OFq*88f2HB +#!Mfaa8{<BD'

    return app
