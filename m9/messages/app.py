from flask import Flask, render_template
import requests
app = Flask(__name__)

api_base = 'http://messenger.pythonanywhere.com'

@app.route('/')
def user():
    response = requests.get(api_base + '/users/2')
    json_data = response.json() # convert the response to JSON
    result = 'Name: ' + json_data['name'] + '<br>'
    result += 'Full name: ' + json_data['full_name'] + '<br>'
    result += 'Created time: ' + json_data['created_time'] + '<br>'
    result += 'ID: ' + str(json_data['id'])
    return result

@app.route('/test_login')
def register():
    # CHANGE THE NAME AND PASSWORD FOR YOUR ACCOUNT HERE
    payload = {'name': 'xxx', 'password': 'yyy'}
    response = requests.post(api_base + '/users/login', payload)
    if response.status_code == 200:
        return 'User logged in successfully!'
    return response.json()['error'], 404


if __name__ == '__main__':
    app.run(debug=True)