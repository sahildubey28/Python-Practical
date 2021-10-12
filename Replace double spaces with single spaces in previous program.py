string = input("Enter String: ")
while '  ' in string:
    string = string.replace('  ', ' ')
    print("changed string = " + string)

# Output: Enter String: Sahil Dubey
#         changed string = Sahil Dubey
