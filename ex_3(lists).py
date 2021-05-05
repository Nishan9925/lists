# Given a Python list of numbers. Turn every item of a list into its square

numbers = [4, 5, 3]
for i in range(len(numbers)):
    numbers[i] *= numbers[i]
print(numbers)
