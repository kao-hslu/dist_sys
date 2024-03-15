#!/usr/bin/env python3

import socket
import sys

# Counterpart to tcp_receiver.py.
#
# Sends 1024 chunks of data to sender.
# This program is used to check how many bytes can be sent to the server
# without the server ever receiving any data. That is, we can test how much
# we can send before send() blocks depending on the (send and receive) buffer
# space


# =======================================================================
# === YOUR CHANGES BELOW THIS LINE
# =======================================================================

TCP_PORT = 12345  # remote server port, change here too if changed in receiver
IP_ADDR = socket.gethostbyname(socket.gethostname())  # 'this machines IP-address
# IP_ADDR = '10.180.21.230' # use this to connect to different computer

# buffer size in Kilobyte (-1: don't change from default)
buff_size = -1

# =======================================================================
# === YOUR CHANGES ABOVE THIS LINE
# =======================================================================

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if buff_size >= 0:
    # Get and set the size of the socket's send buffer
    # bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    # print("Send buffer size [Before]: ", bufsize)
    print(f"Setting send buffer size to: {buff_size} KB")
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000 * buff_size)  # send buffer size
buff_size_actual = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print(f"Send buffer size is: {buff_size_actual}")

print(f"Connecting socket to {IP_ADDR}:{TCP_PORT}")
sock.connect((IP_ADDR, TCP_PORT))  # will fail if no remote socket or not accepting

# the text in "data" is 50 bytes long, repeated 20 time = 1000 bytes = 1 kilobyte
data = ".        10        20        30        40       .\n" * 20  # 50 x 20 = 1000 bytes
data = data.encode()  # returns the string a byte array, as required by socket.send()

input("Connection established, press Enter to start sending data")

try:
    i = 0  # number of chunks (of 1024 byes each)
    total_bytes_sent = 0  # total amount of bytes sent
    while True:
        print("about to send ", len(data), "bytes more  ...")
        bytes_sent = sock.send(data)
        i = i + 1
        total_bytes_sent = total_bytes_sent + bytes_sent
        print(f'...sent {bytes_sent} bytes, {total_bytes_sent:,} in total')
        # input("Press Enter to send more, Ctrl-C to abort")
except KeyboardInterrupt:
    print("Interrupted, closing socket end ending program")
    sock.close()



