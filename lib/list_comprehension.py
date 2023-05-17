#!/usr/bin/env python3
import ipdb

def return_evens(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return evens

def make_exclamation(sentence_list):
    exclamated = []
    for sentence in sentence_list:
        modified_sentence = sentence + '!'
        exclamated.append(modified_sentence)
    return exclamated