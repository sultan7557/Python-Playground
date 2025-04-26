# Quizzly - A Trivia Quiz Game

A Python-based trivia quiz game that fetches questions from the Open Trivia Database API and presents them in a clean GUI built with Tkinter.

![Quizzly Screenshot](quizzly-screenshot.png)

## Features

- Fetches True/False questions from the Trivia API
- Clean, modern UI with a responsive design
- Score tracking throughout the quiz
- Visual feedback for correct and incorrect answers
- Automatically advances to the next question

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Requests library (for API calls)

## Installation

1. Clone this repository or download the source code
2. Install the required packages:
   ```bash
   pip install requests
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## How It Works

- The application fetches 10 True/False questions from the Trivia API
- Questions are displayed one at a time in the GUI
- User selects True or False using the buttons
- Immediate feedback is given by changing the background color (green for correct, red for incorrect)
- Score is updated after each question
- The quiz automatically moves to the next question after a brief delay
- When all questions are answered, the game ends

## Customization

You can modify various aspects of the game:
- Change the number of questions by updating the "amount" parameter in data.py
- Modify the UI colors by changing the THEME_COLOR variable
- Add category filtering by updating the API parameters
- Implement difficulty selection options

## Project Structure

```
quizzly/
├── main.py            # Main application entry point
├── ui.py              # UI implementation using Tkinter
├── data.py            # Question data handling and API interaction
├── images/            # Button images and icons
│   ├── true.png       # True button image
│   └── false.png      # False button image
└── README.md          # Project documentation
```

## Credits

- Questions provided by [Open Trivia Database](https://opentdb.com/)
- Button images should be in the same directory as main.py

## License

This project is licensed under the MIT License - see the LICENSE file for details.
