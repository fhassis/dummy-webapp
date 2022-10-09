from falcon.asgi import App
from falcon.asgi.request import Request
from falcon.asgi.response import Response
from orjson import dumps


class HomeResource:
    """
    Dummy Home endpoint.
    """

    async def on_get(self, req: Request, resp: Response):
        resp.data = dumps({"msg": f"Welcome to Dummy WebApp API!"})


class HelloResource:
    """
    Dummy Hello endpoint.
    """

    async def on_get(self, req: Request, resp: Response):
        resp.data = dumps({"msg": f"Hello user from IP {req.host}!"})


# creates the resources
home_resource = HomeResource()
hello_resource = HelloResource()

# creates the Falcon app
app = App()

# configures the routes
app.add_route("/", home_resource)
app.add_route("/hello", hello_resource)
