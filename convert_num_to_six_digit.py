# Prog02: Create a program that ask the user to input a number (0-1000). Print 
# the number in 6 digit format. Add zeros at the beginning to complete the 6 
# digit.
# Example:
# Input: 143
# Output: 000143

# Pseudocode
# input number
# use ":d" formatting
# print the result

while True:
    try:    
        number = int(input("Enter a number from 0-1000: "))

        if number in range(0, 1001):
            six_digit_num = "%06d" % number
            break
        else:
            print("Choose a number between 0-1000 only!")

    except ValueError:
        print("Choose a number!")

print(f"Number in six digit format: {six_digit_num}")