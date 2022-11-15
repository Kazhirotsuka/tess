from http import server
import bluetooth


def l2cap_server():

    server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    server_sock.bind(('', 0x1001))
    server_sock.listen(1)

    while True:
        print('���M����Ă���f�[�^��҂��Ă܂�')
        client_sock, address = server_sock.accept()
        print(f'�f�[�^���󂯎��܂���{str(address)}')

        print('�f�[�^����M��')

        total = 0
        total_data = ''
        while True:
            try:
                data = client_sock.recv(1024)
            except bluetooth.BluetoothError as e:
                break

            if len(data) == 0:
                break

            total += len(data)

            print(f'total byte read:{total}')
            print(f'data is: {data}')

        client_sock.close()

        print('connection closed')
        return data

    server_sock.close()

    print(receive_data_list)

