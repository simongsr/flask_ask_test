#!/usr/bin/env python3

import logging

from flask import Flask
from flask_ask import Ask
from flask_ask import statement
from gunicorn.http.wsgi import log

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


app = Flask(__name__)
ask = Ask(app, route='/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)


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


@ask.intent(intent_name='SayHelloIntent')
def say_hello(name: str) -> str:
    text = "Hello, {0}!".format(name)
    return statement('<speak>{0}</speak>'.format(text))


if __name__ == '__main__':
    app.run(debug=True)


# @ask.launch
# def launch():
#     speech_text = 'Welcome to the Alexa Skills Kit, you can say hello'
#     return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
#
#
# @ask.intent('HelloWorldIntent')
# def hello_world():
#     speech_text = 'Hello world'
#     return statement(speech_text).simple_card('HelloWorld', speech_text)
#
#
# @ask.intent('AMAZON.HelpIntent')
# def help():
#     speech_text = 'You can say hello to me!'
#     return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
#
#
# @ask.session_ended
# def session_ended():
#     return "", 200
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
