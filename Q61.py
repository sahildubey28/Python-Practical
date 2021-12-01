# Q61. First, def a function called calculate_distance, with one argument (choose any argument name you like). If the  type of the argument is either int or float, the function should return the absolute value of the function input.Otherwise, the function should return "No value". Check if it works calling the function with 9.6 and "what?".


def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No value")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)

# Output:
# Enter your Age 20
# Input is an integer number. Number =  20
# Enter any number 9.6
# Input is a float  number. Number =  9.6
# Enter the last number what?
# No value
