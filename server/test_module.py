from module import Module
import time

class TestModule(Module):
    """docstring for TestModule"""
    def __init__(self, queue):
        super(TestModule, self).__init__(queue)

    def _run(self):
        # while True:
        #    self.put_message('Admin', 'Personal Assistant is Helping You :)', 'Icon')
        #    time.sleep(5) # delays for 5 seconds
        self.put_message('Admin', 'Personal Assistant is Helping You :)', 'Icon')
        