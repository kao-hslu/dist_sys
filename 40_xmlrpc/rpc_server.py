#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import time, datetime, locale


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # define procedures that can be called remotely
    def double(n):
        res = n + n
        print("double of", n, "is", f'{res:n}' )
        return res

    def twotopowerof(n):
        res = pow(2, n)
        print("two to the power of", n, "is", f'{res:n}' )
        return res

    def sleep(n):
        print("sleeping for", n, "seconds")
        time.sleep(n)
        return n

    # register functions with RPC-server so that they can be invoked remotely
    server.register_function(double, 'double')
    server.register_function(twotopowerof, 'twotopowerof')
    server.register_function(sleep, 'sleep')
    print("Starting RPC server...")

    try:
        # Run the server's main loop, wait for RPC requests
        server.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt.")
    print("Bye, bye!")