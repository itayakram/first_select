# -*- coding: utf-8 -*-
import socket


def main():
    client_socket = socket.socket()
    client_socket.connect(('192.168.13.90', 23))
    while True:
        data = raw_input('name:')
        client_socket.send(data)

if __name__ == '__main__':
    main()