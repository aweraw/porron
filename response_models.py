from time import asctime, gmtime
from response import Response

timestamp = lambda: asctime(gmtime())

class HTTPBase(Exception):

    def __init__(self):
        self.response = None


class Redirect(HTTPBase):

    def __init__(self, location, permanent=False):
        code = 301 if permanent else 302
        self.response = Response('Redirecting', code)
        self.response.headers['Location'] = location


class Fail(HTTPBase):

    def __init__(self, message, code=400):
        self.response = Response('{} | {}: {}'.format(timestamp(), code, message), code)


class Error(HTTPBase):
    
    def __init__(self, message, code=500):
        self.response = Response('{} | Error: {}'.format(timestamp(), message), code)
