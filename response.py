import json
import base64

text_mimetypes = {
    "application/javascript",
    "application/json",
    "application/postscript",
    "application/xml",
    "image/svg+xml",
    "text/css",
    "text/csv",
    "text/html",
    "text/javascript",
    "text/json",
    "text/plain",
    "text/richtext",
    "text/tab-separated-values",
    "text/x-python",
    "text/x-setext",
    "text/x-sgml",
    "text/x-vcard",
    "text/xml"
}


class Response:

    def __init__(self, body_data='', code=200):
        self.body = body_data
        self.status_code = code
        self.headers = dict()
        self.headers['Content-Type'] = 'text/plain'
        self.is_binary = False


    def __repr__(self):

        return {
            'body': (base64.encodebytes(self.body) if self.is_binary else self.body),
            'statusCode': self.status_code,
            'headers': self.headers,
            'isBase64Encoded': self.is_binary
        }


    def add_header(self, header, value):
        self.headers[header] = value


    def set_content_type(self, mime_type='application/octet-stream'):
        self.add_header('Content-Type', mime_type)
        if mime_type not in text_mimetypes:
            self.is_binary = True
