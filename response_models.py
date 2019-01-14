from response import Response


class HTTPBase(Exception):

    def __init__(self, message=''):
        super(HTTPBase, self).__init__(message)


class HTTPSuccess(HTTPBase):

    def __init__(self, response):
        self.response = response


class HTTPRedirect(HTTPBase):

    def __init__(self, location, permanent=False):
        code = 301 if permanent else 302
        self.response = Response('Redirecting', code)
        self.response.headers['Location'] = location


class HTTPFail(HTTPBase):

    def __init__(self, message, code=400):
        self.response = Response('{}: {}'.format(code, message), code)


class HTTPError(HTTPBase):
    
    def __init__(self, message):
        self.response = Response('Error: ' + message, 500)
