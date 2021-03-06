from typing import Any, Callable

from .response_models import Response, Error


class Router:

    def __init__(self):
        self.routes = dict()


    def dispatch(self, event, context) -> Any:
        if event['resource'] not in self.routes:
            raise Error("No route for {}".format(event['resource']))

        self.routes[event['resource']].__globals__['_context'] = context
        if event.get("pathParameters"):
            self.routes[event['resource']].__globals__['_event'] = event
            data = self.routes[event['resource']](**event['pathParameters'])
        else:
            data = self.routes[event['resource']](event)

        return data


    def add_route(self, resource: str, func: Callable) -> None:
        if resource in self.routes:
            raise Error("Too many routes for {}".format(resource))

        self.routes[resource] = func


    def handle(self, resource: str) -> Callable[[Callable], Callable]:

        def decorator(func: Callable):
            self.add_route(resource, func)
            return func

        return decorator
