<div align="center">

# 🐦 Twitter Auto-Post Bot 🤖

[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Tweepy](https://img.shields.io/badge/tweepy-v4.10-blue)](http://docs.tweepy.org/en/latest/)
[![Schedule](https://img.shields.io/badge/schedule-v1.1.0-blue)](https://schedule.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Automate your Twitter presence with elegance and ease. Crafted for social media enthusiasts, digital marketers, and developers.
</div>

---

## 🌟 About The Project

This Python-based Twitter Auto-Post Bot automates tweeting, Credit to the Tweepy library for making this easy, this project enables scheduled and random tweets, offering a dynamic and engaging Twitter experience.

### 📁 Files Overview

- `schedule-daily-post-from-file.py`: Automates daily tweets, randomly selecting from `tweets.txt`.
- `tweeter-from-code.py`: Immediately tweets a pre-defined message with the current date.
- `tweeter-random-from-file.py`: Instantly posts a random tweet from `tweets.txt`.
- `tweets.txt`: Add your tweets here, one per line. They will be randomly selected and tweeted.
- `requirements.txt`: Lists all necessary Python packages.

### 📁 Upcoming Features
- `Adding Feature to Auto fetch from openAI api and tweet based on a prompt`.
- `Adding CLI`.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Tweepy (Twitter API)

### Installation

1. Clone the repo:
   ```sh
   git clone git@github.com:lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot.git
   ```
2. Install Python packages:
   ```sh
   pip install -r requirements.txt
   ```

### Setup

1. Obtain Twitter API credentials [here](https://developer.twitter.com/apps).
2. update `keys.py` file with your credentials:
    ```python
    bearer_token = "your_bearer_token"
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"
    ```
3. Customize `tweets.txt` with your tweets.

## 🔧 Usage

Run any script using Python:

```bash
python schedule-daily-post-from-file.py
```

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Contact
Project Link: [https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot)
