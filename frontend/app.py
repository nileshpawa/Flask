from flask import Flask, jsonify, request, render_template
import json
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/api/todo')
def todo():
    return render_template('todo.html')

app.run(debug=True)
