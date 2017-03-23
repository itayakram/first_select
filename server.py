# -*- coding: utf-8 -*-
import socket
import select


def main():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 23))
    server_socket.listen(5)
    open_client_sockets = []
    while True:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, [], [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                print 'New data from client!'


if __name__ == '__main__':
    main()