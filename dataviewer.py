#-*- coding:utf8 -*-
from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)
from data_adapter import *


@app.route('/config')
def config():
    return render_template('react_test.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')


@app.route('/datasource_config')
def form():
    return render_template('datasource_config.html')

# 保有存配置信息
@app.route('/config_list')
def config_list():
    return render_template('datasource_config_list.html')


@app.route('/json')
def json():
    pass


@app.route('/datasource_config')
def datasource_config():
    return render_template('datasource.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    # python -m SimpleHTTPServer 8080
