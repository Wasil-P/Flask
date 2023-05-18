from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/flask"

app.secret_key = "0jd092190d09120edj=231244561xf"

db = SQLAlchemy(app)