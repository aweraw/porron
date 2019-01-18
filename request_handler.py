import json

from typing import Type

from router import Router
from response_models import HTTPBase
from response import Response

class RequestHandler:

    def __init__(self, router: Type[Router]):
        self.router = router

    def process(self, event, context):

        try:
            data = self.router.dispatch(event)
        except HTTPBase as e:
            response = e.response
        else:
            if type(data) is not Response:
                response = Response(json.dumps(data))
                response.set_content_type('application/json')
            else:
                response = data

        return response
