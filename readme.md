# Hangman Game (Adam Asmaca) with GUI (Tkinter)

This is a simple Hangman (Adam Asmaca) game implemented in Python using the Tkinter library for the graphical user interface. The game allows users to guess words from different dictionaries, including Turkish city names, Turkish names, and English vocabulary.

## Features

- Graphical interface built with `tkinter`
- Random word selection from an Excel file using `pandas`
- Multiple dictionaries to choose from:
  - Turkish cities and districts (il ve ilçe isimleri)
  - Turkish  names
  - 1000 common English words
- Hangman-style image progression for incorrect guesses
- Alphabet buttons (supports both Turkish and English letters)
- Game status tracking: remaining attempts, incorrect guesses, etc.
- Menu bar for starting a new game, switching dictionaries, and help/about dialogs

##  Requirements

- Python 3.x
- pandas
- An Excel file named `kelimeler.xlsx` with three columns of word lists
- A folder named `resimler/` containing 9 images named `aa0.png` to `aa8.png` and an icon named `icon.png`

##  How to Run

1. Make sure you have Python 3 and `pandas` installed.
2. Clone this repository or download the source code.
3. Place your `kelimeler.xlsx` file and `resimler` folder in the project directory.
4. Run the script:

```bash
python adamasmaca.py
