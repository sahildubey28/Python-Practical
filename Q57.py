# Write a Python function to check whether the given integer is a prime number or not.

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))

# OUTPUT:-False
