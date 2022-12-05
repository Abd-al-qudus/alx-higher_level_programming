#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        new = [len(sentence), sentence[0]]
        return tuple(new)
    else:
        new = [0, None]
        return tuple(new)
