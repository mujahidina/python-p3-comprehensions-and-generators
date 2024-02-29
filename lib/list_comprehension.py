#!/usr/bin/env python3



def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
print(return_evens([1, 2, 3, 4, 5, 6]))





def make_exclamation(sentence_list):
    return [word + "!" for word in sentence_list]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))