import os
import sys
import socket
import numpy as np
from PIL import Image

INTERFACE = "eth0"
OUTPUT_FOLDER = "unclassified"

ETH_P_ALL = 3

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind(("eth0", 0))

count = 0
while True:
    r = s.recv(1500)
    sys.stdout.write(f"<{str(r)}> (len: {len(r)})\n")

    arr = np.zeros((75, 20, 3), dtype=np.uint8)

    x, y = 0, 0
    for e in list(r):
        arr[x, y] = [e, e, e]
        x += 1
        if x == 75:
            x = 0
            y += 1
        if y == 20:
            break

    img = Image.fromarray(arr, 'RGB')
    img.save(f"{OUTPUT_FOLDER}/frame-{count}.png")
    count += 1
