import sys
import bluetooth


def l2cap_client(bt_addr, data):

    

    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

  

    port = 0x1001

    print(f'trying to connect to {bt_addr} on PSM 0x{port}')

    sock.connect((bt_addr, port))

    print('connected. type stuff')

    while True:
        if(len(data) == 0):
            break
        sock.send(data)
        data = sock.recv(1024)
        print(f'Data received:{str(data)}')

    sock.close()

