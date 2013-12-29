"""
Copyright 2013 Patrick J. Franz
"""

from migrate.versioning import api

import config


if __name__ == '__main__':
    v = api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, v - 1)
    print "Current database version: %s" % api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
