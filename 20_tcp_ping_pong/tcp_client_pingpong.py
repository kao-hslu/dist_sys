#!/usr/bin/env python3

# simple tcp CLIENT
import socket
import platform
import sys

if __name__ == '__main__':
    print(f"Starting as CLIENT on '{socket.gethostname()}' ({platform.system()})")

    # Create a TCP/IP socket
    l_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    TCP_PORT = 12345
    IP_ADDR = socket.gethostbyname(socket.gethostname())  # 'this machines IP-address
    # IP_ADDR = '10.180.21.230' # use this to connect to different computer

    print(f"Connecting to {IP_ADDR}:{TCP_PORT}")
    try:
        l_socket.connect((IP_ADDR, TCP_PORT))  # blocks till connected
    except ConnectionRefusedError:
        print("Error: Destination is not accepting connections (server started?). ")
        sys.exit(0)
    # now we're connected to the server
    print("Now connected! Sending a message...")

    # SEND to acceptor/ server
    # Send data to remote socket...
    bytes_sent = l_socket.send("Hello Server!".encode())
    print(f'Done: sent {bytes_sent}  bytes')

    # RECEIVE from initiator/ server
    data_received = l_socket.recv(1000)  # read max n=1000 bytes
    if not data_received:
        print("*** connection broken ***")
    print(f'Received {len(data_received)} bytes of data')
    print(f'Received data: \"{data_received.decode()}\"')

    l_socket.close()
