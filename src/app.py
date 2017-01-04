#!/usr/bin/env python3

from flask import Flask


__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


HOST = '0.0.0.0'  # : str
PORT = 8000       # : int


app = Flask(__name__)


@app.route('/')
def index__html() -> str:
    return """<!DOCTYPE html>
<html>
    <body>
        <h1>Hello, world!</h1>
    </body>
</html>
"""


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
