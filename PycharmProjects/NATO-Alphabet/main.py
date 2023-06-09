import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        spelled_word = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(spelled_word)


generate_phonetic()
