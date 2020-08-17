#!/usr/bin/python3
"""
distributes an archive to your web servers,
"""
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local
from os.path import exists

env.hosts = ['34.74.168.246', '35.227.124.126']
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes archive"""
    if not exists(archive_path):
        return False
    try:
        try:
            f_name = archive_path.split("/")[-1].split(".")[0]
        except BaseException:
            return False
        try:
            f_nametgz = archive_path.split("/")[-1]
        except BaseException:
            return False

        path = "/data/web_static/releases/"
        data = "/data/web_static/current"
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(f_name))

        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(f_nametgz, path, f_name))

        try:
            run('sudo rm /tmp/{}'.format(f_nametgz))
        except BaseException:
            return False

        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, f_name))
        run('sudo rm -rf {}{}/web_static'.format(path, f_name))
        run('sudo rm -rf /data/web_static/current')
        try:
            run('sudo ln -s {}{}/ {}'.format(path, f_name, data))
        except BaseException:
            return False

        return True
    except BaseException:
        return False
