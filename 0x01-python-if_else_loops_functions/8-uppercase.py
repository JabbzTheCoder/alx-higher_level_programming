#!/usr/bin/python3

def uppercase(input_str):
    txt = ""
    for char in input_str:

        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))

        txt = txt + "{}".format(char)

    print(txt)
