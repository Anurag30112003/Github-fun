from flask import Flask, render_template, request, redirect, url_for, jsonify
from fetch import *
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html', username=username,location=location,repos = repos)

if __name__ == '__main__':
    app.run(debug=True , port=5000)