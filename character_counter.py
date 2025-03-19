# Prog08: Create a program that ask the user to input their fullname. Print 
# the number of characters in the input.
# Example:
# Input: Juan Dela Cruz
# Output: 14

# Pseudocode
# - input fullname
# - set char_counter
# - count number of characters using for loop
# - print the number of characters

# Main Program

full_name = input("Enter your full name: ")

char_count = 0
for char in full_name:
    char_count += 1 

print(f"Output: {char_count}")