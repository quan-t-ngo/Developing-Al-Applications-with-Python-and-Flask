# Emotion Detection Application

## Project Overview

This project implements an Emotion Detection application using the IBM Watson NLP library. The application analyzes a user's text input and predicts the emotions expressed in the text. It identifies the following emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

The application also determines the dominant emotion with the highest confidence score.

## Features

* Detects emotions from user-provided text.
* Returns confidence scores for five basic emotions.
* Identifies the dominant emotion.
* Provides a simple API that can be integrated into a Flask web application.

## Project Structure

```
EmotionDetection/
│
├── emotion_detection.py
├── server.py
├── static/
│   ├── index.html
│   └── mywebscript.js
├── templates/
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.8 or later
* IBM Watson NLP Library
* Flask

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

Run the Flask application:

```bash
python server.py
```

Open your browser and navigate to:

```
http://localhost:5000
```

Enter any English sentence into the text box and click the **Analyze Emotion** button to view the detected emotions.

## Example

**Input**

```
I am extremely happy today because I got promoted!
```

**Output**

```
{
    "anger": 0.01,
    "disgust": 0.00,
    "fear": 0.02,
    "joy": 0.95,
    "sadness": 0.02,
    "dominant_emotion": "joy"
}
```

## Author

Quan Ngo

## License

This project is developed for educational purposes as part of the IBM Skills Network course.
