import subprocess
import platform


def installPackages(packages):

    if platform.system() == 'Linux':
        package_install = 'apt-get'

    elif platform.system() == 'Windows':
        package_install = 'choco'

    else:
        raise Exception('Unsupported version')
    

    for package in packages:
        subprocess.run([package_install, 'install', '-y', package])



def manage_files(files):
    for dest, src in files.items:
        subprocess.run(['cp', src, dest])



def config_server():
    
    package_to_install = ['nginx', 'mysql-server']
    
    files = {'etc/nginx/nginx.conf': '/Users/config_files/nginx.conf',
             'etc/mysql-server/my.conf': '/Users/config_files/my.conf'}
    

    installPackages(package_to_install)
    manage_files(files)

def main():
    config_server()
main()