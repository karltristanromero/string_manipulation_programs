# Prog02: Create a program that ask the user to input a number (0-1000). Print 
# the number in 6 digit format. Add zeros at the beginning to complete the 6 
# digit.
# Example:
# Input: 143
# Output: 000143

# Pseudocode
# input number
# use zfill() to convert number into a 6 digit number
# print the result

number = int(input("Enter a number: "))

six_digit_num = "%06d" % number

print(f"Number in six digit format: {six_digit_num}")