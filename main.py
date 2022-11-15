
import json
import threading
import pandas as pd


from client import l2cap_client
from server import l2cap_server
from start_discoverable import start_discoverable


# �ݒ�p

# �r�[�R���̃A�h���X�ꗗ(�����̒[���ȊO�̃A�h���X���w��)
json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs = []

for bt_addr in json_data.values():
    bt_addrs.append(bt_addr)


# ���M����f�[�^�̊i�[�p���X�g
#[df, public_key, signature]
send_data_list = []

# �󂯎����̊i�[�p���X�g
# [[df, public_key, signature],[df, public_key, signature]]�̂悤�ȍ\���ɂȂ�D
# ���o�����߂ɂ�receive_data_list[1][0]�݂����Ȋ����Ŏg��
receive_data_list = []



# ���M�p�f�[�^�̍쐬
send_data_list.append(21)


print(send_data_list)


# �f�[�^�̑��M
client_thread = threading.Thread(
    target=l2cap_client(
        bt_addrs, send_data_list))

# �f�[�^�̎�M
#discoverable on
start_discoverable()
server_thread = threading.Thread(target=l2cap_server(receive_data_list))

# ����M�̎��s
client_thread.start()
server_thread.start()

