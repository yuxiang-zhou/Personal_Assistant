import abc

class Module(object):
    """Basic Class for All PA Modules"""
    def __init__(self, queue):
        self.queue = queue

    def run(self):
        retry = 10
        while retry > 0:
            try:
                self._run();
                retry = 0
            except:
                print 'Daemon thread goes wrong, retarting...'
                retry -= 1


    @abc.abstractmethod
    def _run(self):
        pass

    def put_message(self, title, content, icon):
        self.queue.put({
            'title': title,
            'content': content,
            'icon': icon
        })
        