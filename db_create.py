"""
Copyright 2013 Patrick J. Franz
"""

from os import path

from migrate.versioning import api

import config
from app import db

if __name__ == '__main__':
    db.create_all()

    if not path.exists(config.SQLALCHEMY_MIGRATE_REPO):
        api.create(config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO,
                            api.version(SQLALCHEMY_MIGRATE_REPO))
