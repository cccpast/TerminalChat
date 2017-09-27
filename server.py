# -*- coding:utf-8 -*-
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.bind(("localhost", 3001))
    s.listen(1)
    sock, addr = s.accept()
    print("connected by" + str(addr))

    while (1):
        send_data = input("server > ")
        sock.send(bytes(send_data, 'utf-8'))
        receive_data = sock.recv(1024)
        receive_data = str(receive_data.decode('utf-8'))
        print("client > ", receive_data)

        # サーバサイドからは切断できない
        if receive_data == "q":
            sock.close()
            break

if __name__ == "__main__":
    main()
