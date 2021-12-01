# Q60. First, def a function, start_process, that takes one argument p. Then, if the start_process function receives an p equal to "Yes", it should return "Start Process" Alternatively, elif p is equal to "No", then the function should return "Start Process Aborted". Finally, if start_process gets anything other than those inputs, the function should return "Sorry for the input".

def start_process(p):
    if (p=="Yes" or p=="yes" or p=="YES"):
        return ("Start process")
    elif (p=="NO" or p=="no" or p=="No"):
        return ("Start process aborted")
    else:
        return ("Sorry for the input")

p= (input("Enter the input : "))
result = start_process(p)
print(result)


# Output:
# Enter the input : yes
# Start process
