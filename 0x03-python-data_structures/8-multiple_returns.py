#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return

    first_char = ''
    _len = len(sentence)

    if _len == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return (_len, first_char)
