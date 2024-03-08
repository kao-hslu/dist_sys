#!/usr/bin/env python3

# simple tcp SERVER
import socket
import platform

if __name__ == '__main__':
    print(f"Starting as SERVER on '{socket.gethostname()}' ({platform.system()})")

    # Create a TCP/IP socket
    l_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    TCP_PORT = 12345
    IP_ADDR = socket.gethostbyname(socket.gethostname())  # 'this machines IP-address
    # IP_ADDR = '10.180.21.230' # use this to connect to different computer

    l_socket.bind((IP_ADDR, TCP_PORT))
    l_socket.listen()  # now the socket exists but server is not yet accepting connections

    print(f"Please connect to {IP_ADDR}:{TCP_PORT}")
    r_socket, r_addr = l_socket.accept()  # blocks till connected
    print(f"Connection established from address: {r_addr}")
    # now we're connected to a client

    # Read data from connection into byte array...
    data_received = r_socket.recv(1000)  # read max n=1000 bytes
    if not data_received:
        print("*** connection broken ***")
    print(f'Received {len(data_received)} bytes of data')
    print(f'Received data: "{data_received.decode()}"')

    l_socket.close()
