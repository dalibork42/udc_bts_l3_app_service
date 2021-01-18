import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqlles3'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'dbles3'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udbles3'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Pwd@1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'blobaccl3'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 's/5LJIngTj21hg8JD2pQSUqWGlSi+nFSsqrsNYvWwOKotBegDzjgqV/E3d/WNDm2lCxXFUlrCgGL9Yhw81U6wA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'blobcl3'
