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
            print(text[i])
            print()
        elif text[i].isspace() and text[i - 1] in ['.', '?', ':']:
            continue
        elif text[i].isspace() and text[i - 1].isspace():
            continue
        else:
            print("{}".format(text[i]), end='')
