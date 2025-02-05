x = input()  # Input string
distinct_characters = set(x)  # Create a set of distinct characters
if len(distinct_characters) % 2 == 0:  # Check if the count is even
    print('CHAT WITH HER!')
else:  # Otherwise, it is odd
    print('IGNORE HIM!')