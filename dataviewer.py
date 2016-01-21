from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/config')
def config():
    return render_template('config.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # python -m SimpleHTTPServer 8080
