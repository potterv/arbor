import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ''' 
        SQLALCHEMY_DATABASE_URI необходим для расширения Flask-SQLAlchemy. Это путь к файлу с нашей базой данных.
        SQLALCHEMY_MIGRATE_REPO — это папка, где мы будем хранить файлы SQLAlchemy-migrate.
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    hostname=os.environ.get('hostname') or "0.0.0.0"