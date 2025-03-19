# Prog05: Create a program that ask the user to input their fullname in 
# incorrect casing. Print the input in proper casing.
# Example:
# Input: jUAn DEla CrUZ
# # Output: Juan Dela Cruz

# Pseudocode
# - input full name in inproper casing
# - convert string to proper casing using title()
# - print the converted string

# Main Program 

messy_full_name = input("Enter your full name in incorrect casing: ")

ordered_full_name = messy_full_name.title()

print()
print(f"I cleaned up your messy name for you: {ordered_full_name}")