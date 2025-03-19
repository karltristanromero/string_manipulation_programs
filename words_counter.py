# Prog07: Create a program that ask the user to input a complete statement. 
# Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# Pseudocode
# - input string statement
# - convert string statement into lists using 
# - set word_total
# - use for loop to iterate over the statement
# - append every index
# - print the word total

# Main Program

complete_statement = input("Enter your thoughts right now: ")

word_total = 0

for word in complete_statement.split():
    word_total += 1

print(f"Output: {word_total}")