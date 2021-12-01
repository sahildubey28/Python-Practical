# Q65. Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers.

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
