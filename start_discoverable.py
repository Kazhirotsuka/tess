import subprocess


def start_discoverable():
    
    subprocess.run(['sudo','bluetoothctl','discoverable','on'])


start_discoverable()