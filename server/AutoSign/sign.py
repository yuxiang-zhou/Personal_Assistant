# coding: utf-8
from WebLogin import WebLogin
from module import Module
import time as st
from datetime import datetime

class ACGSignModule(Module):
    """docstring for ACGSignModule"""
    def __init__(self, queue):
        super(ACGSignModule, self).__init__(queue)
        self.username = "theifgun"
        self.password = "1330871pp"

    def _run(self):
        self.sign()
        while True:
            if datetime.now().time().hour == 16 or datetime.now().time().hour == 17: 
                self.sign()
                st.sleep(1800)

    def sign(self):
        n_retry = 10
        retry = n_retry
        signing = False

        wl = WebLogin(self.username, self.password)
        while retry > 0:
            if wl.loginToACG():
                print 'Logged In'
                if wl.checkSigned():
                    print 'Signed'
                    retry = 0
                else:
                    print 'Perform Signing'
                    wl.sign()
                    signing = True
            else:
                print 'Login Failed'
                retry = retry - 1

        if signing:
            self.put_message('ACG Sign', 'Signed In Seccussfully Today :)', 'Icon')