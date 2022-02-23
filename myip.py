# Copyright (c) 2020, Scott Stone <scott.allan.stone@gmail.com>
from requests import get
import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("1.1.1.1", 80))
    public_ip = get('https://api.ipify.org').text
    private_ip = sock.getsockname()[0]
    print(f'WAN: {public_ip}\nLAN: {private_ip}')

if __name__ == "__main__":
    main()