from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask marshmallow import Marshmallow
import os

# Init app
app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
:wq

