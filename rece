import json
import threading

from server import l2cap_server
from start_discoverable import start_discoverable


start_discoverable()

receive_data_list = []

server_thread = threading.Thread(target=l2cap_server(receive_data_list))

server_thread.start()
