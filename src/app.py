#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import request
from flask_ask import Ask
from flask_ask import statement
from gunicorn.http.wsgi import log

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


HOST = '0.0.0.0'  # : str
PORT = 8000       # : int


app = Flask(__name__)
ask = Ask(app, route='/')


# @app.route('/test')
# def index__html() -> str:
#     name = request.args.get('name', 'troietta')
#     return """<!DOCTYPE html>
# <html>
#     <body>
#         <h1>Hello, {name}!</h1>
#     </body>
# </html>
# """.format(name=name)


# @ask.on_session_started
# def new_session() -> None:
#     log.info('new session started')
#
#
# @ask.session_ended
# def session_ended() -> iter:
#     return "", 200


@ask.intent("SayHello", mapping={'name': 'Name'})
def say_hello(name: str) -> str:
    log.info("In SAY_HELLO")
    # text = render_template('hello', name=name)
    text = "Ciao {0}".format(name)
    return statement(text).simple_card('Hello', text)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
