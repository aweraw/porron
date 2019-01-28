from response_models import Response, S3Response, Redirect, Fail, Error
from router import Router
from request_handler import RequestHandler


class Porron:

    def __init__(self):
        self.router = Router()
        self.request_handler = RequestHandler(self.router)
        self.handle = self.router.handle
    
    def __call__(self, event, context):
        return self.request_handler.process(event, context)
