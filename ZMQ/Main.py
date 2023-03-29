import zmq
import sys
import struct
import time
from threading import Thread
from pub_socket import Pubsocket
from pull import Pull

class Receiver:

    def __init__(self, ip, port):
        self.pull_object = Pull(ip=ip, port=port)
        self.pubobj = pub_socket(port=5555)
        self.pubsocket = self.pubobj.get_socket()
        self.rec_flag = None
        self.thread_rec = None
        self.socket_pull : zmq.socket
        self.socket_pull = self.pull_object.get_socket()

    def get_socket(self):
        if self.socket_pull is None:
            self.socket_pull = self.pull_object.get_socket()

    def rec_data(self):
        print('receiver is ready...')
        while self.rec_flag:
            try:
                self.socket_pull : zmq.socket
                value = self.socket_pull.recv()
                message = value.decode()

                print(f'receiver message: {message}')
                new_msg = message + 'siavash'
                new_message = new_msg.encode()
                id = 1
                value = struct.packe('i', id)
                time.sleep(1)
                self.pub_socket.send_multipart([value,new_message])
            except zmq.Again:
                continue


    def creat_thread(self):
        if self.thread_rec is None:
            self.thread_rec = Thread(target=self.rec_data)
            self.thread_rec.run()

    def close_thread(self):
        self.rec_flag = False
        self.socket_pull = None
        self.thread_rec.join()
        print('receiver is closed...')


def run():
    receiver = Receiver(ip='127.0.0.1', port=5555)


