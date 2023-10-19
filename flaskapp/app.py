from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> CloudDevOps Engineer - Capstone Project </h1>'

app.run(host='0.0.0.0', port=80)
