"""
Copyright 2013 Patrick J. Franz
"""

from os import path

import imp
from migrate.versioning import api

import config
from app import db

if __name__ == '__main__':
    migration = path.join(config.SQLALCHEMY_MIGRATE_REPO, 'versions',
                          '%03d_migration.py' % (api.db_version(config.SQLALCHEMY_DATABASE_URI,
                                                                config.SQLALCHEMY_MIGRATE_REPO) + 1))
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)

    exec old_model in tmp_module.__dict__

    script = api.make_update_script_for_model(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO,
                                              tmp_module.meta, db.metadata)
    with open(migration, "wt") as fp:
        fp.write(script)

    api.upgrade(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)

    print "New migration: %s" % migration
    print "Current database version: %s" % api.db_version(config.SQLALCHEMY_DATABASE_URI,
                                                          config.SQLALCHEMY_MIGRATE_REPO)
