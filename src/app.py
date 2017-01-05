#!/usr/bin/env python3

import logging

from flask import Flask
from flask_ask import Ask
from flask_ask import convert_errors
from flask_ask import question
from flask_ask import session
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
    speech_text = "Commands list: help, what's up, what's new, say"
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


@ask.intent('SendMessageIntent')
def send_message():
    """ Richiede un messaggio da inviare.
    """
    session.attributes['is_sending_message'] = True
    speech_text                              = "What do you want to write?"
    reprompt_speech_text                     = "I didn't get that! " + \
                                               "What will be the text " + \
                                               "of the message?"
    return question(speech_text).reprompt(reprompt_speech_text)


@ask.intent('WriteMesssageIntent', mapping={'msg': 'Msg'})
def write_message(msg):
    if not session.attributes.get('is_sending_message', False):
        speech_text = "I'm sorry, I misunderstood what you said!"
        return statement(speech_text)
    session.attributes['is_text_received'] = True
    session.attributes['msg']              = msg
    speech_text                            = "Would you sign it?"
    reprompt_speech_text                   = "I didn't get that! " + \
                                             "Who are you bitch?"
    return question(speech_text).reprompt(reprompt_speech_text)


@ask.intent('ApplyAuthorIntent', mapping={'name': 'Name'})
def apply_author(name):
    if not session.attributes.get('is_sending_message', False):
        speech_text = "I'm sorry, I misunderstood what you said!"
        return statement(speech_text)
    if not session.attributes.get('is_text_received', False):
        speech_text = "I'm sorry, I misunderstood what you said!"
        return statement(speech_text)
    msg = session.attributes['msg']
    # TODO invia il messaggio
    # speech_text = "Message sent!"
    speech_text = '{0} said {1}'.format(name, msg)
    return statement(speech_text)


@ask.intent("SayHelloIntent", mapping={'name': 'Name'})
def say_hello(name):
    speech_text = 'Ciao {0}'.format(name)
    if name == 'Fabio':
        speech_text = 'Javascript sucks!'
    elif name == 'Costin':
        speech_text = 'Bella zio!'
    elif name == 'Simone':
        speech_text = 'Ciao troietta!'
    return statement(speech_text)


if __name__ == '__main__':
    app.run(debug=True)
