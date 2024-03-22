#!/usr/bin/env python3

import xmlrpc.client
import time
import locale
import sys

locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'

with xmlrpc.client.ServerProxy('http://localhost:8000') as server:
    print("Proxy to remote Server initialized")

    while True:
        print("Enter an integer number (or CTRL-C to exit): ")
        try:
            n = int(input())
            print(f"Invoking RPC twotopowerof( {n} )")
            res = server.twotopowerof(n)  # calls remote(!) function
            print("twotopowerof(", n, ") returned", f'{res:n}')

        except KeyboardInterrupt:
            print("Keyboard interrupt.")
            break
        except ValueError:
            print("Not an int value, try again.")
    print("Bye, bye!")
    sys.exit()
