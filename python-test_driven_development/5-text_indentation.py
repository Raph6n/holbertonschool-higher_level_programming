#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    idx = 0
    new_string = ''
    starting = True

    while idx < len(text):
        if text[idx] == ' ' and starting:
            idx += 1
            continue

        starting = False

        if text[idx] in '.?:':
            new_string += text[idx] + '\n\n'
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue

        new_string += text[idx]
        idx += 1

    print(new_string, end='')
