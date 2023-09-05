#!/usr/bin/python3
"""
test_indentation
prints a text with 2 new lines after
each of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if any(ch.isdigit() for ch in text):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print()
            print()
        else:
            if text[i - 1] in ['.', '?', ':']:
                if text[i].isspace():
                    continue
            print("{}".format(text[i]), end='')
