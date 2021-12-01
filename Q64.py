# Write the program that prompts the user for a list of numbers and prints out the maximum and minimum of
# the numbers at the end when the user enters “done”. Write the program to store the numbers the user
# enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after

list=[]
while True:
    
    data=input('Enter the Input : ')
    if data == 'done':
        break
    else:
        list.append(data)
        

print(list)
print('The maximum number of list is ',max(list))
print('The minimum number of list is ',min(list))

# OUTPUT:-Enter the Input : done
# ['1234', '1256', '1897', '1368']
# The maximum number of list is  1897
# The minimum number of list is  1234 ///// giving correct answer


# Enter the Input : done
# ['12', '212', '32']
# The maximum number of list is  32
# The minimum number of list is  12
