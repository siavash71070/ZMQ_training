import struct
import zmq
import time
import sys

port = 5556
context = zmq.Context
socket = context.socket(zmq.PUB)
socket.bind('tco://* :%s' %port)
id = 1
message = "hello client im coming..."

while True:

    value = struct.pack('i', id)
    M = socket.send_multipart([value,message.encode()])
    time.sleep(1

               )
