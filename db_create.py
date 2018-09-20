#!flask/bin/python
from migrate.versioning import api
from arbor.config import Config
from arbor.app import db
import os.path
def crDb():
   db.create_all()
   conf = Config()
   SQLALCHEMY_DATABASE_URI=conf.SQLALCHEMY_DATABASE_URI
   SQLALCHEMY_MIGRATE_REPO=conf.SQLALCHEMY_MIGRATE_REPO

   if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
       api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
       api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
   else:
       api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

if __name__ == "__main__":
    crDb()