#!/usr/bin/python3
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local
from os.path import exists
from datetime import datetime
from fabric.api import local

env.hosts = ['34.74.168.246', '35.227.124.126']
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes archive"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        file_nametgz = archive_path.split("/")[-1]
        path = "/data/web_static/releases/"
        data = "/data/web_static/current"
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_nametgz, path, file_name))
        run('rm /tmp/{}'.format(file_nametgz))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_name))
        run('rm -rf {}{}/web_static'.format(path, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ {}'.format(path, file_name, data))
        return True
    except BaseException:
        return False


def do_pack():
    """script that generates a .tgz archive"""
    try:
        sysdate = datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        filename = "versions/web_static_{}.tgz".format(sysdate)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except BaseException:
        return None


def deploy():
    """creates and distributes an archive to your web servers,"""
    a_path = do_pack()
    if a_path is None:
        return False
    return do_deploy(a_path)
