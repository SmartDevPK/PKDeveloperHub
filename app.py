from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_pyfile('config.py')

mongo = PyMongo(app)


if __name__ == "__main__":
    app.run(debug=True)