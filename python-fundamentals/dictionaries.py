"""
write a function tha takes two dictionaries
as arguments and returns a new dictionary
containing only the key-values in common to both dictionaries
"""
def common_dictionary(dict_one, dict_two):
    # get common keys
    common = {}
    keys = set(dict_one.keys()).intersection(set(dict_two.keys()))
    # check values
    for i in keys:
        if dict_one[i] == dict_two[i]:
            common[i] = dict_one[i]
    return common

"""
Write a function to count the frequency of words
in a given sentence using a dictionary
"""
def count_words(sentence):
    count = {}
    list_of_words = sentence.split(" ")
    for i in list_of_words:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
    return count

"""
Write a function that takes a list of dictionaries as input and returns 
a new dictionary that contains the sum of the values of a given key across
all dictionaries in the list.
"""
def count_all_values(my_list, key):
    count = {}
    for i in my_list:
        if key in i.keys():
            if key in count.keys():
                count[key] += i[key]
            else:
                count[key] = i[key]
    return count

"""
Write a function that takes a dictionary as input
and returns a new dictionary with the keys and values swapped
"""
def swapped_dictionary(my_dictionary):
    swap = {}
    for i in my_dictionary.items():
        swap[i[1]] = i[0]
    return swap