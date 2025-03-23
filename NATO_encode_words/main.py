import pandas as pd
nato_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word:").upper()
nato_list = [nato_dict[letter] for letter in input_word]
print(nato_list)
