# coding: utf-8

import cookielib
import urllib
import urllib2

class WebLogin(object):

    def __init__(self, login, password):
        """ Start up... """
        self.login = login
        self.password = password

        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        # need this twice - once to set cookies, once to log in...

    def loginToACG(self):
        """
        Handle login. This should populate our cookie jar.
        """
        login_data = urllib.urlencode({
            'username' : self.login,
            'password' : self.password,
        })
        response = self.opener.open("http://www.ccwzz.cc/logging.php?action=login&loginsubmit=yes", login_data)
        data = ''.join(response.readlines())
        html = data.decode('gbk')
        return self.login in html
    
    def checkSigned(self):
        response = self.opener.open("http://www.ccwzz.cc/plugin.php?id=dps_sign:sign")
        data = ''.join(response.readlines())
        return not '今天签到了吗？请选择您此刻的'.decode('utf8') in data.decode('gbk')
    
    def sign(self):
        login_data = urllib.urlencode({
            'qdxq' : 'kx',
            'qdmode' : 3,
        })
        response = self.opener.open("http://www.ccwzz.cc/plugin.php?identifier=dps_sign&module=sign&operation=qiandao&infloat=1", login_data)
        data = ''.join(response.readlines())
        return data.decode('gbk')