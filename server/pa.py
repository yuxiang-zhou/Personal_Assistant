import sys
import os
import Queue
import threading
import logging
import json
import socket
from test_module import TestModule
from AutoSign.sign import ACGSignModule

# called by each thread
def add_Module(q, am):
    m = am(q)
    m.run()


# Queue Execution
def execute_queue(q, thread_list, client_list):
    while True:
        logging.info('Waiting for Message')
        msg_obj = q.get()
        # os.system('notify-send -u critical -t 3000 -i {} "{}" "{}"'.format(
        #     msg_obj['icon'],
        #     msg_obj['title'],
        #     msg_obj['content'])
        # )
        logging.info(msg_obj)
        logging.info('Broadcasting info')

        msg_obj['type'] = 'notify'
        disconnected=[]
        for client in client_list:
            try:
                client.send(json.dumps(msg_obj))
            except Exception as e:
                disconnected.append(client)
                print e

        for dc in disconnected:
            client_list.remove(dc)

        q.task_done()


def start_connection_handler(client_list):
    print client_list

    #create an INET, STREAMing socket
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    # bind the socket to a public host, and servicing port
    serversocket.bind((socket.gethostname(), 9000))
    #become a server socket
    serversocket.listen(5)

    while True:
        # establish a connection
        clientsocket,addr = serversocket.accept()      

        logging.info("Connection from {}".format(str(addr)))
        clientsocket.send(json.dumps({
            'type': 'notify',
            'title': 'Welcome',
            'content': 'Personal Assistant is Helping You :)',
            'icon': 'icon'
        }))
        client_list.append(clientsocket)


if __name__ == "__main__":
    # Logging Specification
    logging.basicConfig(filename='server_info.log', level=logging.DEBUG)

    # Module Registration
    assist_modules = [TestModule, ACGSignModule]

    # Thread Queue Initialisation
    q = Queue.Queue(maxsize=0)

    # Start Modules
    thread_list = []
    for am in assist_modules:
        t = threading.Thread(target=add_Module, args = (q, am))
        t.daemon = True
        t.start()
        thread_list.append(t)

    # Start Connections
    client_list = []
    connection_thread = threading.Thread(target=start_connection_handler, args=[client_list])
    connection_thread.daemon = True
    connection_thread.start()

    # Handling Modules
    execute_queue(q, thread_list, client_list)

