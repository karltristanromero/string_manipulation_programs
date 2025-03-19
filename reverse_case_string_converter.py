# Prog06: Create a program that ask the user to input their fullname in 
# incorrect casing. Print each character of the input in reverse casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz

# Pseudocode
# - input fullname in incorrect casing
# - convert the casing using swapcase()
# - print the converted string

# Main Program

messy_full_name = input("Enter your full name in incorrect casing: ")

reverse_case_name = messy_full_name.swapcase()

print(f"I swapped the cases for you: {reverse_case_name}")
