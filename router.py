from typing import Any, Callable
from response_models import Error
from response import Response


class Router:

    def __init__(self):
        self.routes = dict()


    def dispatch(self, event: dict) -> Any:
        if event['resource'] not in self.routes:
            raise Error("No route for {}".format(event['resource']))

        self.routes[event['resource']].__globals__['_event'] = event
        if event.get("pathParameters"):
            data = self.routes[event['resource']](**event['pathParameters'])
        else:
            data = self.routes[event['resource']]()

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