# Write a program that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.

num_list = [4, 2, 3, 6, 2, 1, 4, 7, 6, 3, 8, 1]

def unique_numbers(lst):
    unique_num_list = []
    for i in lst:
        if i not in unique_num_list:
            unique_num_list.append(i)
    return unique_num_list

print unique_numbers(num_list)
