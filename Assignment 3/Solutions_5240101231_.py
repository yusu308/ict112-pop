"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
text = "Programming"

# Reversed using slicing
reversed_text = text[::-1]

# Print the reversed string
print("Reversed string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    # Split the full name into a list of words
    name_parts = full_name.split()

    # Initialize an empty string to store the initials
    initials = ""

    # Loop through each part of the name and get the first letter
    for part in name_parts:
        initials += part[0].upper() + "."

    # Return the initials (remove the trailing dot)
    return initials[:-1]

# Input: User's full name
full_name = input("Enter your full name: ")

# Output: Initials in uppercase
print(get_initials(full_name))



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.h
"""
# Input string
text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
text = text.lower()

# Check if the string is equal to its reverse
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

# Python program to count the number of words in a sentence

# Get input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words using split()
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print("Number of words in the sentence:", word_count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
text = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_text = text.replace("is", "was")

# Print the modified string
print("Modified string:", modified_text)
