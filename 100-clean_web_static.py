#!/usr/bin/python3
"""
Deletes out-of-date archives, using the function do_clean
"""
from fabric.api import env, run, local
import os

env.hosts = ['54.160.97.159', '54.237.124.193']


def do_clean(number=0):
    """
    Remove old archives.

    Args:
        number (int): The number of archives to retain.

    If number is 0 or 1, only the most recent archive is kept.
    If number is 2, t
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))

    [archives.pop() for _ in range(number)]

    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [
            archive for archive in archives
            if "web_static_" in archive
        ]

        [archives.pop() for _ in range(number)]

        [run("rm -rf ./{}".format(archive)) for archive in archives]
