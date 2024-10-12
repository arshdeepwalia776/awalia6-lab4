#!/usr/bin/env python3
#Author Name:Aswalia6
def join_lists(l1, l2):
    # Perform a set union on both lists and convert the result to a sorted list
    return list(set(l1) | set(l2))

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return list(set(l1).intersection(l2))

def diff_lists(l1, l2):
    # Perform a symmetric difference of the two lists and return the result as a sorted list
    return list(set(l1).symmetric_difference(set(l2)))

if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
