#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0 ]
#     for n in num_list:
#         if n % 2 == 0:
#             evens.append(n)
    return evens
print(return_evens(list(range(0,10))))


def make_exclamation(sentence_list):
    updated_list = [s + "!" for s in sentence_list]
    return updated_list
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))