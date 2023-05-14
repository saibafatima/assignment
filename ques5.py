# Q5. Write a program to filter count vowels in the below-given string.
# string = "I want to become a data scientist"

string = "I want to become a data scientist"
vowels = "aeiouAEIOU"  # List of vowels
vowel_count = 0  # Counter for vowels

for char in string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)
