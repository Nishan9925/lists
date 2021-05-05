# Write a program that will calculate sum of lists members.

list1 = [2, 3, 3, 5, 5]
list2 = [4, 5, 14]
sum = 0
for value in list1 + list2:
    sum += value
print(sum)
