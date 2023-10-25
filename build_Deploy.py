import subprocess
import paramiko
import os

source_code = 'https://github.com/docker/getting-started-app.git'

target_server = 'sms-devops@company.com'
app_user = 'devops'
app_user_pass = '1234%^&*'

local_app_dir = '/Users/haji/Devops_Python/getting-started-app'
work_dir = '/Users/haji/Devops_Python/getting-started-app'


def pull_source():

    if 'getting-started-app' not in work_dir:
      subprocess.run(['git', 'clone', source_code], check=True)
      subprocess.run(['cd', 'getting-started-app'], check=True)
    else:
        os.chdir(work_dir)

def build_application():
    
    subprocess.run(['npm', 'cache', 'clean', '--force'], check=True, cwd=work_dir)
    subprocess.run(['npm', 'install'], check=True, cwd=work_dir)
    subprocess.run(['npm', 'run', 'build'], check=True, cwd=work_dir)


def perform_testing():
    with open("test_results.txt", "w") as output_files:
        try:
            subprocess.run(['npm', 'test'], check=True, stdout=output_files, stderr=subprocess.STDOUT)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e.returncode}")
    
 
def deploy_server():
    ssh_client = paramiko.SSHClient(target_server, app_user, app_user_pass)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    sftp = ssh_client.open_sftp()

    remote_dir = '/app'
    sftp.put(local_app_dir, remote_dir)


def check():
    pull_source()
    build_application()
    perform_testing()
check()