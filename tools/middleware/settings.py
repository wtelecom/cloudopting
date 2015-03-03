# Set Flask debug 
DEBUG = True
# Set API version
API_VERSION = 'v1'
# Set the upload directory
UPLOAD_FOLDER = 'resources/tosca_files'
# Set the key searched in the parser API POST
FILENAME = 'tosca_file'
# Set the allowed extensions to upload
ALLOWED_EXTENSIONS = set(['xml'])

# Database settings
# Set the database engine
DB_TYPE = 'mongo.Engine'
# Set the database host
HOST = 'localhost'
# Set the database port
PORT = 27017
# Set the database name
DATABASE = 'middleware'