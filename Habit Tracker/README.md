# Reading Habit Tracker

A Python application that helps you track your daily reading habits using Pixela's visual tracking API. Monitor how many pages you read each day with beautiful graphs and visual progress tracking.

![Pixela Graph Example](screenshot.png)

## Features

- Track daily reading progress (pages read)
- Visual representation of your reading habits
- Add, update, and delete tracking data
- View your progress through a public or private URL
- Color-coded activity graph similar to GitHub's contribution chart

## Requirements

- Python 3.x
- 

requests

 library
- `python-dotenv` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/reading-habit-tracker.git
   cd reading-habit-tracker
   ```

2. Install required packages:
   ```
   pip install requests python-dotenv
   ```

3. Create a `.env` file with your credentials:
   ```
   PIXELA_TOKEN=your_secret_token_here
   PIXELA_USERNAME=your_username_here
   ```

## Usage

### First-time Setup

1. Run the script with the `--setup` flag to create your Pixela account and reading graph:
   ```
   python main.py --setup
   ```

2. After setup, you can visit your graph at:
   ```
   https://pixe.la/v1/users/[username]/graphs/graph1.html
   ```
   
## Code Structure

The application consists of several modules:

- 

main.py

: Main script that handles user commands
- `pixela_api.py`: Handles all interactions with the Pixela API
- `util.py`: Utility functions for date formatting and validation

## How It Works

The application uses the [Pixela API](https://pixe.la/v1) to:

1. Create a user account (one-time setup)
2. Create a graph to track reading (one-time setup)
3. Post daily reading data to the graph
4. Visualize your reading habits over time

Each pixel on the graph represents one day, with the color intensity showing how many pages you read.

## Customization

You can customize your tracking by editing the graph parameters in the code:

- `name`: Graph title
- `unit`: What you're tracking (pages, minutes, books, etc.)
- `color`: Graph color (shibafu (green), momiji (red), sora (blue), etc.)
- `type`: Data type (int, float)

## License

MIT License

## Acknowledgements

- [Pixela API](https://pixe.la/) for providing the tracking visualization service
- Inspired by GitHub's contribution graph

---

This project helps build consistent reading habits by providing visual feedback on your daily progress. Happy reading!
