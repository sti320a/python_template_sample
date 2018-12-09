import os
import redis
from urllib.parse import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
import string

class HelloWorld(object):

    def dispatch_request(self, request):
        response = self.template()
        return Response(response)

    def template(self):
        t = string.Template('Hello ${name}!')
        html = t.safe_substitute({'name':'Python'})
        return html

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def app():
    app = HelloWorld()
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
   