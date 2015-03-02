# TODO: Set in settings
ALLOWED_EXTENSIONS = set(['xml'])
# END TODO

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS