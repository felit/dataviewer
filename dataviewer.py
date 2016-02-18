# -*- coding:utf8 -*-
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

app = Flask(__name__)
from data_adapter import *
import psycopg2
from models.datasource import DataSource


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


from models.meta_data import MetaData
# 保有存配置信息
@app.route('/config_list')
def config_list():
    datasources = MetaData().get_all_datasource()
    return render_template('datasource_config_list.html', datasources=datasources)


@app.route('/json')
def json():
    pass


@app.route('/semantic/menu')
def menu():
    return render_template('semantic/menu.html')


@app.route('/datasource')
def datasource():
    return render_template('datasource.html')


@app.route('/chart/config')
def chart_config():
    datasources = MetaData().get_all_datasource()
    print(datasources)
    return render_template('chart/two-dimension.html', datasources=datasources)


@app.route('/monitor')
def monitor():
    return render_template('monitor/index.html')


@app.route('/test_query', methods=['POST'])
def test_query():
    query = request.form['query']
    datasource = request.form['datasource']
    conn = psycopg2.connect(host='192.168.232.11', port=5433, database='xiaoya_crm', user='trace', password='readonly')
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    return jsonify({'result': query, 'from': 'server',
                    'columns': [{}],
                    'description': [row[0] for row in cursor.description],
                    'example_data': data
    })


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    # python -m SimpleHTTPServer 8080
