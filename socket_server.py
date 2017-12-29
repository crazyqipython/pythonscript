import logging
import sys
import socketserver

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s')

class EchoRequestHandler(socketserver.BaseRequestHandler):
    '''
    test request handler
    '''
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger("EchoRequestHandler")
        self.logger.debug('__init__')
        super(EchoRequestHandler, self).__init__(request, client_address, server)

    def setup(self):
        self.logger.debug('setup')
        return super(EchoRequestHandler, self).setup()

    def handle(self):
        self.logger.debug('handle')

        data = self.request.recv(1024)
        self.logger.debug("recv()->'%s'", data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug('finish')
        return super(EchoRequestHandler, self).finish()


class EchoServer(socketserver.TCPServer):
    '''
    tcp server
    '''
    def __init__(self, server_address, handle_class=EchoRequestHandler):
        self.logger = logging.getLogger('EchoServer')

        self.logger.debug('__init__')
        super(EchoServer, self).__init__(server_address, handle_class)
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        super(EchoServer, self).server_activate()

    def server_forever(self):
        self.logger.debug('waiting for request')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        while True:
            self.handle_request()
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return super(EchoServer, self).handle_request()

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)', request, client_address)
        return super(EchoServer, self).verify_request(request, client_address)

    def process_request(self, request, client_address):
        self.logger.debug('process_request(%s, %s)', request, client_address)
        return super(EchoServer, self).process_request(request, client_address)

    def server_close(self):
        self.logger.debug('server_close')
        return super(EchoServer,self).server_close()

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)', request, client_address)
        return super(EchoServer,self).finish_request(request, client_address)

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return super(EchoServer,self).close_request(request_address)


if __name__ == '__main__':
    import socket
    import threading

    address=('localhost', 0)
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    logger = logging.getLogger('client')
    logger.info('Server on %s:%s', ip, port)

    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')
    s.connect((ip, port))

    message = b'Hello, world'
    logger.debug(b'sending data: "%s"', message)
    len_sent = s.send(message)

    logger.debug('waiting for response')
    response = s.recv(len_sent)
    logger.debug('response from server: "%s"', response)

    logger.debug('closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()