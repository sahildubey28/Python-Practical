# Q8. Given two integer numbers return their sum. If the sum is greater than 100, then return their product.

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

sum = n1+n2

if sum > 100:
    print("Product = ",n1*n2)
else:
    print("Sum = ",sum)


# Output: 

# Enter a number: 10
# Enter another number: 10
# Sum = 20
