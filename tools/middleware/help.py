import os
from flask import Flask, g

import settings
from orm.core import ORM


class FlaskHelp(object):

    def __init__(self, flask):
        super(FlaskHelp, self).__init__()
        self.flask = flask

    def create_file(self, file, name):
        file.save(os.path.join(self.flask.config['UPLOAD_FOLDER'], name))

    @property
    def orm(self):
        if not g.get('orm', None):
            g.orm = ORM(settings.DB_TYPE, settings.HOST, settings.PORT, settings.DATABASE)
        return g.get('orm', None)


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))