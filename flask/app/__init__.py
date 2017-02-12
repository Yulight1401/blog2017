from flask import Flask,Response
from werkzeug.datastructures import Headers

class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        allow_header = ('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
            headers.add(*allow_header)
        else:
            headers = Headers([origin, methods, allow_header])
        kwargs['headers'] = headers
        return super(MyResponse, self).__init__(response, **kwargs)

app = Flask(__name__)
app.response_class = MyResponse

from app import Blogmodel
from app import Blogcontroler
from app import views
