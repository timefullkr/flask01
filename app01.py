from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def wwwRoot():
    return render_template('index.html', message='Hello Flask WebApp')

@app.route('/apple')
def page1():
    return "<h1>사과</h1>"

@app.route('/<path:page>')
def page2(page):
    return f"<h1>{page}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')