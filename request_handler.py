import json

from typing import Type
from functools import reduce

from .router import Router
from .response_models import Response, HTTPBase


def convert_to_response(data):
    if not issubclass(type(data), Response):
        data = Response(json.dumps(data))
        data.set_content_type('application/json')
    return data
    
class RequestHandler:

    def __init__(self, router: Type[Router]):
        self.router = router
        self.event_pipeline = list()
        self.data_pipeline = list()

        self.register_data_processor(convert_to_response)


    def register_event_processor(self, func):
        self.event_pipeline.append(func)


    def register_data_processor(self, func):
        self.data_pipeline.append(func)


    def process_pipeline(self, pipeline, obj):
        return reduce(lambda ob, fu: fu(ob), pipeline, obj)


    def process(self, event, context):

        if event.get('type') == 'TOKEN':
            event['resource'] = 'authorizer'

        try:
            event = self.process_pipeline(self.event_pipeline, event)
            data  = self.process_pipeline(self.data_pipeline, self.router.dispatch(event))
        except HTTPBase as e:
            response = e.response
        else:
            response = data

        return response.gw_dict()
