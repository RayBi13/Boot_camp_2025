def create_letter_index_dict(word):
    """Creates a dictionary with letters as keys and lists of indexes as values."""
    lettre_index_dict = {}
    for index, letter in enumerate(word):
        if letter in lettre_index_dict:
            lettre_index_dict[letter].append(index)
        else:
            lettre_index_dict[letter] = [index]
    return lettre_index_dict

def main():
    word = input("Please enter a word: ").strip()
    letter_index_dict = create_letter_index_dict(word)
    print(letter_index_dict)

if __name__ == "__main__":
    main()