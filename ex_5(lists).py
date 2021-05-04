# Write a Python program to get unique values from a list.

list1 = [4, 7, 8, 9, 8, 1, 2, 7]
unique_list = []
for i in range(len(list1)):
    # remove item from list1
    list1_without_i_element = list1[:i] + list1[i + 1:]
    if list1[i] not in list1_without_i_element:
        unique_list.append(list1[i])
print(unique_list)
