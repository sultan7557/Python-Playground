# NATO Phonetic Alphabet Converter

A simple Python application that converts any word or text to NATO phonetic alphabet code words.

## Description

This application allows users to input any word and receive the corresponding NATO phonetic alphabet representation. For example, "Hello" becomes "Hotel Echo Lima Lima Oscar".

## Features

- Converts any text input to NATO phonetic alphabet code words
- Case-insensitive input (automatically converts to uppercase)
- Easy-to-use command line interface
- Uses pandas for efficient data processing


4. Ensure you have the NATO phonetic alphabet CSV file in the correct location.

## Usage

Run the program:

python main.py



When prompted, enter the word you want to convert to NATO phonetic alphabet.

## Example

Enter a word: hello ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']


## File Structure

- `main.py` - The main Python script
- `nato_phonetic_alphabet.csv` - CSV file containing the NATO phonetic alphabet

## Data Format

The CSV file should have the following format:

letter,code A,Alfa B,Bravo ...


## Dependencies

- Python 3.6+
- pandas
