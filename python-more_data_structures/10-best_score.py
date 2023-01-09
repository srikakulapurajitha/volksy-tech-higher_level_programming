#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        b = len(a_dictionary.values())
        if b > 0:
            score = max(a_dictionary.values())
            for k in a_dictionary.keys():
                if a_dictionary[k] == score:
                    return k
    return None
