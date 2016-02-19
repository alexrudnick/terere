#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

def sum_and_difference(x, y):
    return x+y, x-y

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/sample',)

    def _dispatch(self, method, params):
        try: 
            return self.server.funcs[method](*params)
        except:
            import traceback
            traceback.print_exc()
            raise

def main():
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000),
                                requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_function(sum_and_difference)
    print("SERVER IS NOW ON IT.")
    server.serve_forever()

if __name__ == "__main__": main()
