# Prog09: Create a program that ask the user to input their fullname in 
# incorrect casing. Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

# Pseudocode
# - input full name in incorrect casing
# - convert string into pascal casing using title() and replace()
# - print converted string

# Main Program

messy_full_name = input("Enter your full name in incorrect casing: ")

title_case_name = messy_full_name.title()
pascal_case_name = title_case_name.replace()