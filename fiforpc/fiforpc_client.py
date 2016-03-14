#!/usr/bin/env python3

import fileinput
import os

SERVER_TO_CLIENT_PATH = "/tmp/server_to_client.fifo"
CLIENT_TO_SERVER_PATH = "/tmp/client_to_server.fifo"

def perform_query(s):
    with open(CLIENT_TO_SERVER_PATH, "w") as c2s:
        print(s, file=c2s)

    out = ""
    with open(SERVER_TO_CLIENT_PATH, "r") as s2c:
        out = s2c.readline()
    return out

def main():
    while True:
        line = ""
        try: line = input("> ")
        except: break
        line = line.strip()
        print("got this line: ", line)

        returned = perform_query(line)
        print("returned from server: ", returned)

if __name__ == "__main__": main()
