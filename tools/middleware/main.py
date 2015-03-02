#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: main
   :platform: Unix, Windows, Mac
   :synopsis: CloudOpting middleware main module.

.. moduleauthor:: Francisco Hidalgo <fjhidalgo@wtelecom.es>


"""

import os
from flask import Flask, jsonify, render_template, request, g
from werkzeug import secure_filename

from orm.core import ORM
from utils.fileutils import allowed_file


# TODO: Export to settings file
API_VERSION = 'v1'
UPLOAD_FOLDER = 'resources/tosca_files'
FILENAME = 'tosca_file'
DB_TYPE = 'mongo.Engine'
HOST = 'localhost'
PORT = 27017
DATABASE = 'middleware'
# END TODO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/%s/tosca' % (API_VERSION), methods=['GET', 'POST'])
def parser(): 
    """Fetch, add or update a TOSCA parser.

    Retrieves, adds or updated TOSCA configuration from DB.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """

    if request.method == 'POST':
        file = request.files[FILENAME]
        if file and allowed_file(file.filename):
            secure_filename(file.filename)
            g.orm = ORM(DB_TYPE, HOST, PORT, DATABASE)
            doc_id = g.orm.create(
                filename = file.filename,
                collection = 'tosca' 
            )

            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(doc_id)))
            else:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(doc_id)))
            
            return jsonify(
                {"response" : "success"}
            )


if __name__=='__main__':
    app.run(threaded=True)