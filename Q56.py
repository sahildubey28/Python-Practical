# Q56. Write a Python function to display all the multiples of 7 & 9 within the range 100 to 500.

nl=[]
for x in range(100, 500):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

# Output:

# 105,140,175,210,245,280,315,350,385,420,455,490
