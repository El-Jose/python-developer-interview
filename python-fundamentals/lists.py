import random


# write a program that removes duplicate elements in a list
def not_repeated_list_simple(my_list):
    return list(set(my_list))

# write a program that returns a reversed list
def reversed_list(my_list):
    return my_list.reverse()

# write a program that remove all even numbers from a list
def remove_even_numbers(my_list):
    return [x for x in my_list if x%2==0]

# write a program to find the sum of all elements in a list
def sum_all_elements(my_list):
    return sum(my_list)

# write a program to organize a list of strings by length
def sort_by_length(my_list):
    my_list.sort(key=len)
    return my_list

# write a python program to find the first ocurrance of an element in a list
def elem_position(my_list, elem):
    return my_list.index(elem)