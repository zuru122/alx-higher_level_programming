#!/usr/bin/python3
for ascii_value in range(97, 123):
    char = chr(ascii_value)
    if (char == 'e' or char == 'q'):
        continue
    print("{}".format(char), end="")
