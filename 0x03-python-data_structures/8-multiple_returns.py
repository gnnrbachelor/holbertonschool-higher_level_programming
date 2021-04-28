#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    if strlen == 0:
        sen_tup = (0, None)
    else:
        sen_tup = (strlen, sentence[0])
    return (sen_tup)
