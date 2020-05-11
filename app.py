from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init app
app = Flask(__name__)


#basedir = os.path.abspath(os.path.dirname(__file__))

#Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  false


#Init ma

app.route('/', methods=['GET'])
def get():
	return 'Hello World'
	#return jsonify({'msg':'Helloworld'})

#Run
#if __name__ == '__main__':
app.run()
