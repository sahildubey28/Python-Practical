# Q62. Python program to display the sum of input (n) numbers using a list.

list = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number = '))
    list.append(numbers)
print("Sum of elements in given list is :", sum(list))

# Output:
# How many numbers: 3
# Enter number = 1
# Enter number = 2
# Enter number = 3
# Sum of elements in given list is : 6
