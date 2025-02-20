
# Ask the user for a word
word = input("ecrivez un mot: ")

# Create a dictionary to store the indices of each letter
letter_indices = {}

# Iterate over the word and store the indices
for index, letter in enumerate(word):
    if letter not in letter_indices:
        letter_indices[letter] = []
    letter_indices[letter].append(index)

print(letter_indices)
