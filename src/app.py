#!/usr/bin/env python3

import logging

from flask import Flask
from flask_ask import Ask
from flask_ask import convert_errors
from flask_ask import statement

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


app = Flask(__name__)
ask = Ask(app, route='/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)


# @ask.intent('SayHelloIntent', default={'name': 'World'})
# def say_hello(name):
#     text = "Hello, {0}".format(name)
#     return statement(text)


@ask.intent('HelpIntent')
def help_func():
    """ Messaggio di HELP.
    """
    speech_text = "Commands list: help, what's up, what's new, " + \
                  "to write something by user's name"
    return statement(speech_text)


@ask.intent('WhatsUpIntent')
def whats_up():
    """ Aggiornamente sullo stato della produzione.
    """
    speech_text = "Stato della produzione"
    return statement(speech_text)


@ask.intent('WhatsNewIntent')
def whats_new():
    """ Gli ultimi messaggi inviati nella chat.
    """
    # TODO inserire una logica di persistenza per ricordare il timestamp
    #      dell'ultimo messaggio letto
    speech_text = "Ultimi messaggi"
    return statement(speech_text)


@ask.intent('SayIntent', mapping={'msg': 'Msg', 'name': 'Name'})
def say(msg, name):
    """ Scrive un messaggio nella chat.
    """
    if 'msg' in convert_errors:
        speech_text = 'Could not understand message, please try again'
    elif 'name' in convert_errors:
        speech_text = 'Could not understand your name, please try again'
    else:
        speech_text = "{0} writes: {1}".format(name, msg)
    return statement(speech_text)


if __name__ == '__main__':
    app.run(debug=True)
