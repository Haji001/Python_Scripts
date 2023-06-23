import socket

"""Python script that will take a list of IP addresses as input and print out the hostnames for each IP address."""




def getHostname(IpAddress):


    try:
        host = socket.gethostbyaddr(IpAddress)[0]
    except socket.gaierror:
        host = None
    return host


IpAddresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]


for IpAddress in IpAddresses:
    hostname = getHostname(IpAddress)
    print(f"The hostname for {IpAddress} is:\n{hostname}")