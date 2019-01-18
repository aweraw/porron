from response import Response
from s3object import S3Object
from response_models import Redirect, Fail, Error
from router import Router
from request_handler import RequestHandler


class Porron:

    def __init__(self):
        self.router = Router()
        self.request_handler = RequestHandler(self.router)
        self.handle = self.router.handle
    
    def __call__(self, event, context):
        return self.request_handler.process(event, context)
