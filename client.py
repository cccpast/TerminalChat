# -*- coding:utf-8 -*-
import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 3001))

    while (1):
        receive_data = sock.recv(1024)
        receive_data = str(receive_data.decode('utf-8'))
        print("server > ", receive_data)
        send_data = input("client > ")
        sock.send(bytes(send_data, 'utf-8'))

        # クライアントサイドからのみ切断可能
        if send_data == "q":
            sock.close()
            break

if __name__ == "__main__":
    main()
