#!/usr/bin/python3
# Fabfile to generates a .tgz
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        now = datetime.now()
        archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
        archive_path = "versions/{}".format(archive_name)

        local("tar -cvzf {} web_static".format(archive_path))

        if os.path.exists(archive_path):
            return archive_path
        else:
            return None

    except Exception as e:
        return None
