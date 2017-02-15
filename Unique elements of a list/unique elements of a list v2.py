# Write a program that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.

num_list = [4, 2, 3, 6, 2, 1, 4, 7, 6, 3, 8, 1]

def set_unique_numbers(lst):
    return list(set(lst))

print set_unique_numbers(num_list)
