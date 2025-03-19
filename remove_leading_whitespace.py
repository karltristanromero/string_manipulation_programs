# Prog01: Create a program that ask the user to input their fullname with 
# several space characters at the beginning. Print the input without the 
# spaces in the beginning. 
# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz

# Pseudocode
# Input full name with leading spaces
# remove the leading spaces with lstrip()
# print the processed input

# Main Program

full_name = input("Please enter your full name with leading spaces: ")

removed_left_spaces = full_name.lstrip()

print("I removed the spaces hehe")
print(removed_left_spaces)