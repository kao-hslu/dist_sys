#!/usr/bin/env python3

import socket
import sys


# Counterpart to tcp_sender.py.

# =======================================================================
# === YOUR CHANGES BELOW THIS LINE
# =======================================================================

TCP_PORT = 12345  # change if already in use
IP_ADDR = socket.gethostbyname(socket.gethostname())  # 'this machines IP-address
# IP_ADDR = '10.180.21.230' # use this to connect to different computer

# buffer size in Kilobyte (-1: don't change from default)
buff_size = -1

# =======================================================================
# ===  YOUR CHANGES ABOVE THIS LINE
# =======================================================================

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if buff_size >= 0:
    # Get and set the size of the socket's receive buffer
    # bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    # print("Receive buffer size [Before]: ", bufsize)
    print(f"Setting receive buffer size to: {buff_size} KB")
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1000 * buff_size)  # send buffer size
buff_size_actual = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
print(f"Receive buffer size is: {buff_size_actual}")

print(f"Starting as server. Please connect to {IP_ADDR}:{TCP_PORT}")

sock.bind((IP_ADDR, TCP_PORT))
sock.listen()

# now the socket exists but is not yet accepting connections
# input('Listening to connections, press Enter to start accepting client connections')

try:
    while True:
        # before accept(), the socket exists but will not allow connecting to it
        print("Now accepting (i.e., waiting for) new connection...")
        conn, addr = sock.accept()
        print(f"Connection established from address: {addr}")

        input("Press Enter to start receiving data, Ctrl-C to abort")
        #  note: receive means getting data from the local buffer
        print("... waiting for data")

        # Read data from the socket...
        total_bytes_received = 0  # total numer of bytes received

        while True:
            data_received = conn.recv(1000)  # read max n bytes at a time
            if not data_received:
                print("*** connection broken ***")
                break
            bytes_received = len(data_received)
            total_bytes_received = total_bytes_received + bytes_received
            print(f'received {bytes_received} bytes of data, {total_bytes_received:n} bytes in total ')
    # end while True

except KeyboardInterrupt:
    print("\nInterrupted, closing socket end ending program")
    sock.close()
