import socket

def GetOpenPorts(IpAddresses):
    """List open ports of given IP addresses."""
    
    OpenPorts = []

    for IpAddress in IpAddresses:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            sock.connect((IpAddress, 24))  # Replace 0 with the specific port number you want to check
            
            # If the connection is successful, add the remote port to the list
            OpenPorts.append(sock.getpeername()[1])
            
            sock.close()  # Close the socket after use
        except (socket.error, socket.timeout):
            # Handle connection errors or timeouts here
            pass

    return OpenPorts

Ip_Addresses = ['192.168.0.1', '192.168.0.2']
print(GetOpenPorts(Ip_Addresses))
