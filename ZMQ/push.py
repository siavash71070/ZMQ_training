import zmq


class Push:

    def __init__(self, port, ip='*'):
        self.context = zmq.Context()
        self.socket = None
        self.init_zmq(ip, port)
        self.socket = zmq.socket(zmq.PUSH)
        self.socket.bind(f'tcp://{ip}:{port} ')

    def get_socket(self):
        return self.socket


if __name__ == '__main__':
    pushobject = Push(port=5556)
