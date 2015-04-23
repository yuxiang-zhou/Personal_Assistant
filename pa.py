import sys
import os
import Queue
import threading
from test_module import TestModule
from AutoSign.sign import ACGSignModule

# called by each thread
def add_Module(q, am):
    m = am(q)
    m.run()

# Queue Execution
def execute_queue(q, thread_list):
    while True:
        msg_obj = q.get()
        os.system('notify-send -u critical -t 3000 -i {} "{}" "{}"'.format(
            msg_obj['icon'],
            msg_obj['title'],
            msg_obj['content'])
        )
        q.task_done()

if __name__ == "__main__":
    assist_modules = [TestModule, ACGSignModule]
    q = Queue.Queue(maxsize=0)
    thread_list = []
    for am in assist_modules:
        t = threading.Thread(target=add_Module, args = (q, am))
        t.daemon = True
        t.start()
        thread_list.append(t)

    execute_queue(q, thread_list)