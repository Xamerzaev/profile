from os.path import join, dirname, realpath

class Config():
    SECRET_KEY = 'rfdsa89fyu9sfsfsfsfewgw8eyr322q3'
    SQLALCHEMY_TRACK_MODIFICATION = False
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'core/static/images/')
