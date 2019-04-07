"""
app.py
author: Tim "tjtimer" Jedro
created: 07.04.19
"""
import socket
from pathlib import Path

import jinja2
import jinja2_sanic
from sanic import Sanic, response
from sanic.exceptions import NotFound

config = {
    'DEBUG': socket.gethostname() == 'tjs-headquarter',
    'HOST': '127.0.0.1',
    'PORT': 7666,
    'WORKERS': 2,
    'ROOT_DIR': Path('/home/tjtimer/dev/py/tjs-hq')
}


def prepare():
    app = Sanic('tjs headquarter')
    app.config.from_object(config)
    app.on_close = []
    jinja2_sanic.setup(
        app,
        loader=jinja2.FileSystemLoader(
            searchpath=[
                (app.config.ROOT_DIR / 'templates').as_posix()
            ]
        )
    )

    @app.get('/')
    @jinja2_sanic.template('index.html')
    async def index(_):
        return {}

    @app.exception(NotFound)
    async def not_found(request, *_):
        if request.headers.get('referer', None) is None:
            return await index(request)
        return response.raw(b'\x00')

    @app.listener('before_server_start')
    async def setup(app, loop):
        pass

    @app.listener('after_server_stop')
    async def shutdown(app, loop):
        pass

    return app
