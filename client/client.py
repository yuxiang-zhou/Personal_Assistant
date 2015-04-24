import sys
import os
import Queue
import threading
import logging
import socket
import json

if __name__ == '__main__':
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # connection to hostname on the port.
    s.connect((socket.gethostname(), 9000))                               

    # Receive no more than 1024 bytes
    while True:
        tm = s.recv(4096)
        print 'Message Recieved: {}'.format(tm)
        try:
            msg_obj = json.loads(tm)
            if msg_obj['type'] == 'notify':
                os.system('notify-send -u critical -t 3000 -i {} "{}" "{}"'.format(
                    msg_obj['icon'],
                    msg_obj['title'],
                    msg_obj['content'])
                ) 
        except:
            print 'Cannot handle msg as json: {}'.format(tm)
        
