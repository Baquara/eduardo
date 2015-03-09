import re, requests

class Ed(object):

    def __init__(self, name='Eduardo', port='8085'):
        self.name = name
        self.port = port

    def say(self, text):
        url = 'http://www.ed.conpet.gov.br/mod_perl/bot_gateway.cgi'
        server = '0.0.0.0:' + self.port
        params = dict(server=server,charset_post='utf-8',
        charset='utf-8',pure=1,js=0,tst=1, msg=text)

        r = requests.get(url, params=params)
        return self.name + ': ' + re.sub(r'\n+$','', r.text)
