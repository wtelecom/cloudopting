#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: main
   :platform: Unix, Windows, Mac
   :synopsis: CloudOpting middleware main module.

.. moduleauthor:: Francisco Hidalgo <fjhidalgo@wtelecom.es>


"""

import os
import json
from flask import render_template, request
from werkzeug import secure_filename

import settings
from utils.fileutils import allowed_file, jsonify
from help import FlaskHelp, CustomFlask


app = CustomFlask(__name__)
app.config['UPLOAD_FOLDER'] = settings.UPLOAD_FOLDER
app.config['DEBUG'] = True
flk_help = FlaskHelp(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list():
    return render_template('list.html')


@app.route('/api/%s/tosca/files/<id>' % (settings.API_VERSION), methods=['GET'])
def get_data(id):
    if request.method == 'GET':
        return jsonify(
            flk_help.orm.get(
                id = id,
                collection = 'tosca_files' 
            )
        )


@app.route('/api/%s/tosca/files/all' % (settings.API_VERSION), methods=['GET'])
def get_all_data():
    if request.method == 'GET':
        return json.dumps(
            flk_help.orm.get_all(
                collection = 'tosca_files' 
            )
        )


@app.route('/api/%s/tosca/files' % (settings.API_VERSION), methods=['POST'])
def parser(): 
    """Add and parse a TOSCA file.

    Add and parses a TOSCA file and make accesible the result 
    from DB.

    Args:
        tosca_file: A XML Tosca file to parse.

    Returns:
        A JSON response showing the results. For
        example:

        {
            'response': 'OK',
            '_id': '54f45f0adb4cc05b47e3c7d4'
        }

    Raises:
        IOError: An error occurred accessing the database.
    """

    if request.method == 'POST':
        file = request.files[settings.FILENAME]
        if file and allowed_file(file.filename):
            secure_filename(file.filename)
            doc_id = flk_help.orm.create(
                filename = file.filename,
                collection = 'tosca_files' 
            )

            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
                flk_help.create_file(file, str(doc_id))
            else:
                flk_help.create_file(file, str(doc_id))

            return jsonify(
                {"response" : "OK"}
            )


@app.route('/api/%s/tosca/configurations' % (settings.API_VERSION), methods=['GET', 'POST', 'PUT'])
def tosca_conf():
    if request.method == 'POST':
        if request.json:
            doc_id = flk_help.orm.create(
                fields = request.json,
                collection = 'tosca_conf' 
            )
            return jsonify(
                {
                    "response" : "OK",
                    "id": str(doc_id)
                }
            )
    elif request.method == 'PUT':
        if request.json:
            if flk_help.orm.update(
                search = request.json['search'],
                change = request.json['change'],
                collection = 'tosca_conf' 
            ):
                return jsonify(
                    {"response" : "OK"}
                )
    elif request.method == 'GET':
        return json.dumps(
            flk_help.orm.get_all(
                collection = 'tosca_conf' 
            )
        )



if __name__=='__main__':
    app.run(threaded=True)



