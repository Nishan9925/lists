# Concatenate two lists index-wise.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = ''
for i in range(len(list1)):
    if i==len(list1)-1:
        result += list1[i] + list2[i]
    else:
        result += list1[i] + list2[i] + " "


print(result)

