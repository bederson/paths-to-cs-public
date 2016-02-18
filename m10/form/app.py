from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html', name='Person', age=30)

@app.route('/doit', methods=["POST"])
def doit():
    name = request.form.get('name')
    return redirect(url_for('result', name=name))

@app.route('/result')
def result():
    name = request.args.get('name')
    return render_template('result.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)