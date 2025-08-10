from flask import Flask, jsonify, request
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

@app.route('/api/getdata')
def get_json_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/submittodoitem', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data submitted successfully!'

app.run(host='0.0.0.0', port=9000, debug=True)
