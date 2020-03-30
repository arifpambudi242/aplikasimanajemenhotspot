import socket
import ssl
import hashlib
import binascii


PORT = 8728
SSL_PORT = 8729
USER = 'admin'
PASSWORD = ''
USE_SSL = False
VERBOSE = False


CONTEXT = ssl.create_default_context()
CONTEXT.check_hostname = False
CONTEXT.verify_mode = ssl.CERT_NONE


class LoginError(Exception):
    pass


class WordTooLong(Exception):
    pass


class CreateSocketError(Exception):
    pass


class RouterOSTrapError(Exception):
    pass


class Api:

    def __init__(self, address, user=USER, password=PASSWORD, use_ssl=USE_SSL, port=False,
                 verbose=VERBOSE, context=CONTEXT):

        self.address = address
        self.user = user
        self.password = password
        self.use_ssl = use_ssl
        self.port = port
        self.context = context

        if port:
            self.port = port
        elif use_ssl:
            self.port = SSL_PORT
        else:
            self.port = PORT

        self.sock = None
        self.connection = None
        self.open_socket()
        self.login()
        self.is_alive()

    def open_socket(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        try:
            self.connection = self.sock.connect((self.address, self.port))

        except OSError:
            raise CreateSocketError('Error: API failed to connect to socket. Host: {}, port: {}.'.format(self.address,
                                                                                                         self.port))

        if self.use_ssl:
            self.sock = self.context.wrap_socket(self.sock)



    def login(self):
        sentence = ['/login', '=name=' + self.user, '=password=' + self.password]
        reply = self.communicate(sentence)
        if len(reply[0]) == 1 and reply[0][0] == '!done':
            return reply
        elif 'Error' in reply:
            raise LoginError('Login ' + reply)
        elif len(reply[0]) == 2 and reply[0][1][0:5] == '=ret=':
            md5 = hashlib.md5(('\x00' + self.password).encode('utf-8'))
            md5.update(binascii.unhexlify(reply[0][1][5:]))
            sentence = ['/login', '=name=' + self.user, '=response=00'
                        + binascii.hexlify(md5.digest()).decode('utf-8')]
            return self.communicate(sentence)


    def communicate(self, sentence_to_send):

        def send_length(w):
            length_to_send = len(w)
            if length_to_send < 0x80:
                num_of_bytes = 1
            elif length_to_send < 0x4000:
                length_to_send += 0x8000
                num_of_bytes = 2
            elif length_to_send < 0x200000:
                length_to_send += 0xC00000
                num_of_bytes = 3
            elif length_to_send < 0x10000000:
                length_to_send += 0xE0000000
                num_of_bytes = 4
            elif length_to_send < 0x100000000:
                num_of_bytes = 4
                self.sock.sendall(b'\xF0')
            else:
                raise WordTooLong('Word is too long. Max length of word is 4294967295.')
            self.sock.sendall(length_to_send.to_bytes(num_of_bytes, byteorder='big'))




        def receive_length():
            r = self.sock.recv(1)


            if r < b'\x80':
                r = int.from_bytes(r, byteorder='big')
            elif r < b'\xc0':
                r += self.sock.recv(1)
                r = int.from_bytes(r, byteorder='big')
                r -= 0x8000
            elif r < b'\xe0':
                r += self.sock.recv(2)
                r = int.from_bytes(r, byteorder='big')
                r -= 0xC00000
            elif r < b'\xf0':
                r += self.sock.recv(3)
                r = int.from_bytes(r, byteorder='big')
                r -= 0xE0000000
            elif r == b'\xf0':
                r = self.sock.recv(4)
                r = int.from_bytes(r, byteorder='big')

            return r

        def read_sentence():
            rcv_sentence = []
            rcv_length = receive_length()

            while rcv_length != 0:
                received = b''
                while rcv_length > len(received):
                    rec = self.sock.recv(rcv_length - len(received))
                    if rec == b'':
                        raise RuntimeError('socket connection broken')
                    rec = rec
                    received += rec
                received = received.decode('utf-8')

                rcv_sentence.append(received)
                rcv_length = receive_length()

            return rcv_sentence



        for word in sentence_to_send:
            send_length(word)
            print('ini masuk word')
            print(word)
            print('ini akhir word')
            self.sock.sendall(word.encode('utf-8'))

        self.sock.sendall(b'\x00')

        paragraph = []
        received_sentence = ['']
        while received_sentence[0] != '!done':
            received_sentence = read_sentence()
            paragraph.append(received_sentence)
        return paragraph


    def talk(self, message):


        if type(message) == str or type(message) == tuple:
            return self.send(message)
        elif type(message) == list:
            reply = []
            for sentence in message:
                reply.append(self.send(sentence))
            return reply
        else:
            raise TypeError('talk() argument must be str or tuple containing str or list containing str or tuples')

    def send(self, sentence):

        if type(sentence) == str:
            sentence = sentence.split()
        reply = self.communicate(sentence)


        if '!trap' in reply[0][0]:

            raise RouterOSTrapError("\nCommand: {}\nReturned an error: {}".format(sentence, reply))
            pass



        nice_reply = []
        for m in range(len(reply) - 1):
            nice_reply.append({})
            for k, v in (x[1:].split('=', 1) for x in reply[m][1:]):
                nice_reply[m][k] = v
        return nice_reply

    def is_alive(self) -> bool:
        """Check if socket is alive and router responds"""


        try:
            self.sock.settimeout(2)
        except OSError:

            return False

        try:
            self.talk('/system/identity/print')

        except (socket.timeout, IndexError, BrokenPipeError):

            self.close()
            return False

        self.sock.settimeout(None)
        return True

    def create_connection(self):
        self.open_socket()
        self.login()

    def close(self):
        self.sock.close()