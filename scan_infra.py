import subprocess 
import re


def check_open_ports(host):

    command = ["nmap", "-sT", host]
    command_output = subprocess.check_output(command)
    open_ports = re.findall(r"\d+/\w", command_output.decode())

    return open_ports
    

def vulnerabilities_check(host):

    command = ["nessus", "-sT", "10", host]
    command_output = subprocess.check_output(command)
    vul = re.findall(r"\s+(\d+)\s+\[(\w+)\]\s+(.+)", command_output.decode())

    return vul

def main():
    host = "172.20.20.20"

    open_ports = check_open_ports(host)
    vulnerabilities = vulnerabilities_check(host)


    print("open ports;\n")
    for port in open_ports:
        print(port)

    print("vulnerabilities:\n")
    for vulnerability in vulnerabilities:
        print(vulnerability)

if "__name__" == "__main__":
    main()