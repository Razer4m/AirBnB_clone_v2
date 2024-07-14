#!/usr/bin/python3
# Fabfile to distribute an archive to a web server using deploy.
from fabric.api import env, put, run, sudo
import os

env.hosts = ['54.160.97.159', '54.237.124.193']


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
