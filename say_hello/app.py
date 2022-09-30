from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = 'jvrejgrhnsaspk'

@app.route('/hello')
def index():
    flash("What's Your Name?")
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash(f"Hi {request.form['name']}, great to see you!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)