#!/usr/bin/python3
"""
-Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
-All archives must be stored in the folder versions
(your function should create this folder if it doesn’t exist)
-The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
c – create
z – using gzip compression
v – verbal, displaying information about the archive while archiving
f – using an archive file
"""
from datetime import datetime
from fabric.api import local


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
