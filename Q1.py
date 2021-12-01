# Q1. Display float number with 2 decimal places using print()

a = 6.4536
 
# using "%" to print value till 2 decimal places
print ("The value of number till 2 decimal place(using %) is : ",end="")
print ('%.2f'%a)
 
# using format() to print value till 2 decimal places
print ("The value of number till 2 decimal place(using format()) is : ",end="")
print ("{0:.2f}".format(a))
 
# using round() to print value till 2 decimal places
print ("The value of number till 2 decimal place(using round()) is : ",end="")
print (round(a,2))


# Output : 

# The value of number till 2 decimal place(using %) is : 6.45
# The value of number till 2 decimal place(using format()) is : 6.45
# The value of number till 2 decimal place(using round()) is : 6.45
