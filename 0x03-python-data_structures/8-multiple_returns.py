#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length < 1:
        value = length, None
        return (value)
    else:
        value = length, sentence[0]
        return (value)
