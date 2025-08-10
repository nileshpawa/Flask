from flask import Flask, render_template, request
import requests

BACKEND_URL = 'http://localhost:9000'

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/api/todo')
def todo():
    return render_template('todo.html')

@app.route('/api/submittodoitem', methods=['POST'])
def submittodoitem():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    requests.post(f"{BACKEND_URL}/api/submittodoitem", data={
        "itemName": item_name,
        "itemDescription": item_description
    })
    return 'Data submitted successfully!'

app.run(host='0.0.0.0', port=8001, debug=True)
