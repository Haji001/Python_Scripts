import subprocess
import docker 



def dockerPull(ImageName, ContainerName, PortMapping):
    subprocess.run(['docker', 'pull', ImageName])
    subprocess.run(['docker', 'run', '-d', '-p', PortMapping, ContainerName, ImageName, 'sh'])


def execute():
    dockerPull(ImageName="httpd",
               ContainerName="tnm_container_qa",
               PortMapping=8080)


def StatusContainer(ContainerID):
    client = docker.from_env()
    container = client.containers.get(ContainerID)
    status = container.status

    return status

def main():
    execute()
    StatusContainer(ContainerID="24g4sgalkjdgf698")
    

    


