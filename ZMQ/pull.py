import sys
import zmq

class Pull:
    def __int__(self,port, ip='*'):
        self.context = zmq.Context()
        self.socket = None
        self.init_zmq(ip, port)

    def ini_zmq(self,ip, port):
        self.context = zmq.Cotext().socket(zmq.PULL)
        self.socket.connect(f'tcp://{ip }:{port}')

    def get_socket(self):
        return self.socket


if __name__ == '__main__':
    pullobject = Pull(ip='127.0.0.1', port=5556)
