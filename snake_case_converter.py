# Prog10: Create a program that ask the user to input their fullname in 
# incorrect casing. Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

# Pseudocode
# - input full name in incorrect casing
# - convert full name to lower case using lower()
# - replace spaces with _ using replace()
# - print converted string

# Main Program

messy_full_name = input("Enter your full name in incorrect casing: ")

lower_full_name = messy_full_name.lower()
snake_case_name = lower_full_name.replace(" ", "_")

print(f"Output: {snake_case_name}")