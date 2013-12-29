"""
Copyright 2013 Patrick J. Franz
"""

from migrate.versioning import api

import config


if __name__ == '__main__':
    api.upgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
    print "Current database version: %s" % api.db_version(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
