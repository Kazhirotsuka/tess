import json
import threading
from sendandreceive import toTwo

start_discoverable()

json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs = []

for bt_addr in json_data.values():
    bt_addrs.append(bt_addr)

send_data_list = []

send_data_list.append(21)

toTwo.start()
