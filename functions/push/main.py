# -*- coding: utf-8 -*-
from dependency import requests

print "start simple function"
def handle(event, context):
    print "processing event"
    print requests
    return event
