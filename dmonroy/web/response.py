import json

from aiohttp import web


class Response(web.Response):
    def __init__(self, body, **kwargs):
        super(Response, self).__init__(
            body=body.encode('utf-8'), **kwargs
        )


class JavaScriptResponse(Response):

    def __init__(self, data, **kwargs):
        super(JavaScriptResponse, self).__init__(
            body=json.dumps(data), content_type='application/javascript',
            **kwargs
        )


class JSONResponse(Response):

    def __init__(self, data, **kwargs):
        super(JSONResponse, self).__init__(
            body=json.dumps(data), content_type='text/json', **kwargs
        )


class HTMLResponse(Response):

    def __init__(self, body, **kwargs):
        super(HTMLResponse, self).__init__(
            body=body, content_type='text/html', **kwargs
        )