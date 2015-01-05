# -*- coding: utf-8 -*-
"""
    Main view
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
API_version = "v1"


@app.route('/api/%s/' % API_version)
def execute_cmd():
    """Executes an ad-hoc command in the client specified"""
    pass


@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.run()