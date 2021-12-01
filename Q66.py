# Python program to delete an element from a list by index which is given by the user.

print("Enter 10 Elements: ")
arr = []
for i in range(10):
    arr.append(input())

print("\nEnter the Value to Delete: ")
val = input()

arr.remove(val)
print(arr)

# # OUTPUT:-1
#           2
#           3
#           4
#           5
#           6
#           7
#           8
#           9
#           10

# Enter the Value to Delete:

# 5
# ['1', '2', '3', '4', '6', '7', '8', '9', '10']
