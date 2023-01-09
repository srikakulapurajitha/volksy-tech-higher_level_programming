#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict1 = a_dictionary.copy()
    for i in new_dict1:
        if new_dict1[i] == value:
            del a_dictionary[i]
    return a_dictionary
