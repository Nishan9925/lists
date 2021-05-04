# Write a Python program to remove duplicates from a list.


list_numbers = [4, 5, 4, 5, 6]
second_list_members = []
for i in list_numbers:
    if i not in second_list_members:
        second_list_members.append(i)
print(second_list_members)
