from module import Module

class TestModule(Module):
    """docstring for TestModule"""
    def __init__(self, queue):
        super(TestModule, self).__init__(queue)

    def _run(self):
        self.put_message('Admin', 'Personal Assistant is Helping You :)', 'Icon')
        