# Write a program that takes a list of numbers and makes a new list
# of only the first and last elements of the given list.

a = [2, 4, 6, 8, 10, 12, 14, 16, 18]

def first_and_last_element(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[0], lst[-1]]

print first_and_last_element(a)
