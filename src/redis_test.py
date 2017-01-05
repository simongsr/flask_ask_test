#!/usr/bin/env python3

import redis

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


HOST = 'localhost'
PORT = 6379


def test():
    r = redis.StrictRedis(host=HOST, port=PORT)

    custom_key = 'chiave_prova'

    value_1    = 'Pippo'
    value_2    = 'Topolino'
    value_3    = 'Paperino'

    r.set(custom_key, value_1)
    print(r.get(custom_key))

    r.set(custom_key, value_2)
    print(r.get(custom_key))

    r.set(custom_key, value_3)
    print(r.get(custom_key))

    r.set(custom_key, value_1)
    r.set(custom_key, value_2)
    print(r.get(custom_key))


if __name__ == '__main__':
    test()
