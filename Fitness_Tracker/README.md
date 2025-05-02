# Exercise Tracking App

A Python application that logs your workouts automatically by analyzing natural language descriptions of your exercises. This app uses Nutritionix API to interpret exercise descriptions and calculate calories burned, then logs the data to a Google Sheet via Sheety API.

## Features

- Natural language exercise input (e.g., "ran 3 km and walked for 4 miles")
- Automatic calculation of:
  - Exercise duration
  - Calories burned
- Seamless logging to Google Sheets
- Date and time tracking for all exercises

## Technologies Used

- Python 3
- Nutritionix API (exercise analysis)
- Sheety API (Google Sheets integration)
- python-dotenv (environment variable management)

## Setup Instructions

### Prerequisites

- Python 3.7+
- Nutritionix API credentials
- Sheety API endpoint and token
- Google Sheet configured with Sheety


### Setting up Google Sheets

1. Create a Google Sheet with the following columns:
   - Date
   - Time
   - Exercise
   - Duration
   - Calories

2. Connect your sheet to Sheety to get an API endpoint
3. Update your `.env` file with the Sheety endpoint

## Usage

Run the script and enter your exercise when prompted:

```
python main.py
```

Example input:
```
What exercise did you do today? Ran 5km and did yoga for 30 minutes
```

The app will:
1. Parse your exercise description
2. Calculate duration and calories for each exercise
3. Log the information to your Google Sheet


## API Documentation

- [Nutritionix API Documentation](https://developer.nutritionix.com/docs/v2)
- [Sheety API Documentation](https://sheety.co/docs/requests)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Nutritionix for providing the natural language exercise processing API
- Sheety for the Google Sheets API integration

---

*Note: This project was created for educational purposes and personal use.*