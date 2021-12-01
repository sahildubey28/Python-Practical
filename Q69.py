# Q69. Write a Python program to find all the values in a list are greater than a given number.

def test(nums, n):
   return(all(x > n for x in nums))      

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("list numbers :",nums)
n = 12
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))
n = 5
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))


# Output:

# list numbers : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Check whether all numbers of the said list greater than 12
# False

# Check whether all numbers of the said list greater than 5
# True
