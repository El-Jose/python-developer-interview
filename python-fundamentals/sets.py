# Given two sets, write a function to find their intersection, union, or difference.
def set_operations(set_one, set_two, op):
    if op == "intersection":
        return set_one.intersection(set_two)
    elif op == "union":
        return set_one.union(set_two)
    elif op == "difference":
        return set_one.difference(set_two)

# remove duplicate from a list using sets
def remove_duplicated(my_list):
    return list(set(my_list))

# finding the frequency of elements in a list using sets
def counting_elements(my_list):
    count = {}
    for i in set(my_list):
        count[i] = my_list.count(i)
    return count