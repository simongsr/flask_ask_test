#!/usr/bin/env python3

import json
from urllib.request import Request, urlopen
import urllib.request

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


def send_request():
    data = {
        "session": {
            "sessionId": "SessionId.8e0b2789-1083-4a28-8299-f184ffe829f0",
            "application": {
                "applicationId": "amzn1.ask.skill.f4da0a02-e36f-47dd-8be2-b2dd8bd1e258"
            },
            "attributes": {},
            "user": {
                "userId": "amzn1.ask.account.AEYWT2VO5DYLPVGUFZAEIUJ3J4JHRGMT4BDO4BWRYM26375PA7JYGERLBQ5ST7WVOX4KVM2JFQAPQYJI6NWD4VYN5UL6JSXJOHI5IVINCKGNW37DSDM72AMFOMP5BDLVMLYLQJZAKLWBC3VTRPVCTAJCV3RJSGU4T2F6OZYKMYJX6GDDWPHLIMEMRTDWGTMHDUOWOTCOZZRUIPQ"
            },
            "new": True
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.0bbd5df6-0064-46a0-941e-c7fc62407385",
            "locale": "en-US",
            "timestamp": "2017-01-04T14:01:08Z",
            "intent": {
                "name": "SayHello",
                "slots": {
                    "Name": {
                        "name": "Name",
                        "value": "Simone"
                    }
                }
            }
        },
        "version": "1.0"
    }

    req = Request('http://localhost:8000')
    req.add_header('Content-Type', 'application/json')

    response = urlopen(req, bytearray(json.dumps(data), encoding="UTF-8"))

    print(response)


if __name__ == '__main__':
    send_request()
