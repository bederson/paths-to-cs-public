from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('file.html', name='Person', age=50)

@app.route('/test_loop')
def loop():
    u1 = User('Ben Bederson', 'Professor')
    u2 = User('Tak Yeon Lee', 'TA')
    u3 = User('Nick Aversano', 'TA')
    people = [u1, u2, u3]
    return render_template('users.html', name='Person', users=people)

class User:
    def __init__(self, full_name, role):
        self.full_name = full_name
        self.role = role

if __name__ == '__main__':
    app.run(debug=True)