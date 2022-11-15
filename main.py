
import json
import threading
import pandas as pd


from client import l2cap_client
from server import l2cap_server
from start_discoverable import start_discoverable


# 設定用

# ビーコンのアドレス一覧(自分の端末以外のアドレスを指定)
json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs = []

for bt_addr in json_data.values():
    bt_addrs.append(bt_addr)


# 送信するデータの格納用リスト
#[df, public_key, signature]
send_data_list = []

# 受け取る情報の格納用リスト
# [[df, public_key, signature],[df, public_key, signature]]のような構成になる．
# 取り出すためにはreceive_data_list[1][0]みたいな感じで使う
receive_data_list = []



# 送信用データの作成
send_data_list.append(21)


print(send_data_list)


# データの送信
client_thread = threading.Thread(
    target=l2cap_client(
        bt_addrs, send_data_list))

# データの受信
#discoverable on
start_discoverable()
server_thread = threading.Thread(target=l2cap_server(receive_data_list))

# 送受信の実行
client_thread.start()
server_thread.start()

