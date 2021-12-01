# Q9. Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum

def sum_thrice(x, y, z):

    sum = x + y + z
  
    if x != y != z:
      sum = sum * 4
    return sum

print("Value = ",sum_thrice(1, 2, 3))


# Output : 

# value = 24
