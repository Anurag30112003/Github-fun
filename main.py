from flask import Flask, render_template, request, redirect, url_for, jsonify
# from fetch import *
import requests
app = Flask(__name__)  

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form['user']
        api = requests.get(f'https://api.github.com/users/{username}')
        name = api.json()['login']
        url = api.json()['html_url']
        repos = api.json()['public_repos']
        location = api.json()['location']
        return  render_template('index.html', username=username,location=location,repos = repos)
    else:
        return render_template('index.html')

    

# if __name__ == '__main__':
#     app.run(debug=True , port=5000)