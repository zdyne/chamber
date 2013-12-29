"""
Copyright 2013, Patrick J. Franz
"""

import argparse

from app import db
from app import models
from app import bcrypt


def main(opts):
    user = models.User(email=opts.email, password=bcrypt.generate_password_hash(opts.password))
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', dest='email', metavar='EMAIL')
    parser.add_argument('--password', dest='password', metavar='PASSWORD')
    args = parser.parse_args()

    main(args)
