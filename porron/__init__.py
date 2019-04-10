from .response_models import Response, S3Response, Redirect, Fail, Error
from .router import Router
from .request_handler import RequestHandler

name = "porron"

class Porron:

    def __init__(self):
        self.router = Router()
        self.request_handler = RequestHandler(self.router)
        self.handle = self.router.handle
    
    def __call__(self, event, context):
        return self.request_handler.process(event, context)

    def generate_open_api_spec(self):
        type_map = {
            int: 'integer',
            str: 'string'
        }
        definition = dict()
        for path, func in self.router.routes.items():
            operations = dict(get=dict())
            operations['get']['summary']     = func.__name__
            operations['get']['description'] = func.__doc__
            parameters = list()
            for k in func.__annotations__:
                if k == "return": continue
                
                param = {
                    'name': k,
                    'in': 'path',
                    'required': True,
                    'schema': {
                        'type': type_map[func.__annotations__[k]]
                    }
                }

                parameters.append(param)
                
            operations['get']['parameters'] = parameters
            operations['get']['responses'] = {
                200: {}
            }
            definition[path] = operations

        return dict(paths=definition)

