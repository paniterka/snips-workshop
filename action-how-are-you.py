#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

INTENT_HOW_ARE_YOU = "tkdev:how_are_you"


def main():
    with Hermes("127.0.0.1:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .start()


def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "I'm doing great."
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
