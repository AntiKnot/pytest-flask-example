from flask import Flask
from flask import jsonify

from config import DevConfig
from factory import create_app

app = create_app(DevConfig)

if __name__ == '__main__':
    app.run()
