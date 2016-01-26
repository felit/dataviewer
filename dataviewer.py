from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)
from weixin import Weixin
from data_adapter import *

@app.route('/config')
def config():
    return render_template('config.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/layout')
def table():
    return render_template('layout.html')

@app.route('/json')
def json():
    result = Weixin().macro_channel()
    print result
    print(zip(*result))
    TableAdapter().adapter(result)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    # python -m SimpleHTTPServer 8080