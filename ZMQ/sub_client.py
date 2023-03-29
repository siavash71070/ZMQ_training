import zmq
import time
import struct

port = 5556
context = zmq.context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, chr(id.encode()))

socket.connect('tcp:// localhost%s' % port)
socket.setsockopt(zmq.RCVTIMEO, 500)

while True:
    try:

        data = socket.recv_multipart()
        id_value = struct.unpack('i', data[0])
        message = data[1].decode()
        print(message)

    except zmq.Again:

        pass
