"""
Copyright 2013, Patrick J. Franz
"""

from fabric.api import sudo
from fabric.api import run

# Most of this is informed by the following thread:
# http://www.raspberrypi.org/phpBB3/viewtopic.php?f=66&t=57001&p=434804
def cleanDistribution():
    sudo('apt-get -y update')
    sudo('apt-get -y upgrade')

    unneededPkgs = [
        'python*',
        'omxplayer',
        'scratch',
        'midori',
        'dillo',
        'lxde-common',
        'hicolor-icon-theme',
        'galculator',
        'xarchiver',
        'lxde-icon-theme',
        'libpoppler19',
        'x11-common',
        'ed',
        'vim-common',
        'lxsession',
        'lxappearance',
        'lxpolkit',
        'lxrandr',
        'lxsession-edit',
        'lxshortcut',
        'lxtask',
        'lxterminal',
        'xauth',
        'debian-reference-common',
        'samba-common',
        'fontconfig',
        'fontconfig-config',
        'fonts-freefont-ttf',
        'netsurf-gtk',
        'netsurf-common',
        'dbus-x11',
        'desktop-base',
        'desktop-file-utils',
        'libxmuu1']

    for pkg in unneededPkgs:
        sudo("apt-get -y autoremove %s" % pkg, warn_only=True)

    sudo('apt-get -y autoremove')
    sudo('apt-get -y clean')

    unneededDirs = [
        '/opt/vc/src',
        '/usr/share/icons/*',
        '/usr/share/sounds/',
        '/usr/share/squeak/',
        '/usr/share/wallpapers',
        '/usr/share/themes',
        '/usr/share/kde4',
        '/usr/share/images/*',
        '/home/pi/python_games',
        '/home/pi/Desktop']

    for d in unneededDirs:
        sudo("rm -rf %s" % d, warn_only=True)


def installPython():
    """
    Install Python 2.7 only w/ pip support.
    """

    sudo('apt-get -y install python2.7')
    sudo('ln -s /usr/bin/python2.7 /usr/local/bin/python', warn_only=True)

    sudo('apt-get -y install python-pip')
    sudo('apt-get -y install python2.7-dev')


def installServer():
    sudo('pip install flask')
    sudo('pip install flask-wtf')
    sudo('pip install Flask-SQLAlchemy')
    sudo('pip install SQLAlchemy-migrate')
    sudo('pip install flask-login')
    sudo('pip install flask-bcrypt')
