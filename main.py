
import json
import threading



from client import l2cap_client
from server import l2cap_server
from start_discoverable import start_discoverable



start_discoverable()


json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs = []

for bt_addr in json_data.values():
    bt_addrs.append(bt_addr)



send_data_list = []


receive_data_list = []


send_data_list.append(21)




client_thread = threading.Thread(
    target=l2cap_client(
        bt_addr, send_data_list))



server_thread = threading.Thread(target=l2cap_server(receive_data_list))


client_thread.start()
server_thread.start()

