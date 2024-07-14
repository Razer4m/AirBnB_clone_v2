#!/usr/bin/python3
"""
Fabric script that creates and
distributes an archive to the web servers
"""
from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = ['54.160.97.159', '54.237.124.193']


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


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_basename = os.path.splitext(archive_filename)[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_basename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_basename))
        run("rm /tmp/{}".format(archive_filename))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(archive_basename, archive_basename))

        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_basename))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(archive_basename))

        return True

    except Exception as e:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
