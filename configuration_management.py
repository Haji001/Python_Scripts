
""" Configuration management tool using Python to manage and enforce the desired state of infrastructure resources. 
You can utilize libraries like SaltStack, Puppet, or your own custom solution to define configurations, manage 
system files, install software, and ensure consistency across multiple servers."""

import subprocess
import platform


def installPackages(packages):

    if platform.system() == "Linux":
        PackageManager = 'apt-get'

    if platform.system() == 'Windows':
        PackageManager = 'choco'

    else:
        raise Exception("Cannot supporting operating system.")
    
    for package in packages:
        subprocess.run([PackageManager, 'install', package, '-y'])



def manageFiles(files):

    for src, dest in files.items():
        subprocess(['cp', src, dest])


def configServer():

    PackageToInstall = ['nginx', 'Git', 'Apache']
    PackageFiles = {
        "/etc/nginx/nginx.conf": "/bin/nginx/nginx.conv",
        "/etc/git/config": "/bin/git/config",
        "/etc/apache/apache.conf": "/bin/apache/apache.conf"
    }

    installPackages(PackageToInstall)
    manageFiles(PackageFiles)

configServer()