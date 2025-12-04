<div align="center">

# 🐦 Twitter Auto-Post Bot 🤖

[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Tweepy](https://img.shields.io/badge/tweepy-v4.14-blue)](http://docs.tweepy.org/en/latest/)
[![OpenAI](https://img.shields.io/badge/openai-v1.11.1-blue.svg)](https://platform.openai.com/docs/libraries)

[![Schedule](https://img.shields.io/badge/schedule-v1.2.1-blue)](https://schedule.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Automate your Twitter presence. Auto Post tweets from from openAI GPT4, from a file, from a string, schedule a new tweet to be posted daily or post the tweet instantly.
</div>

---

## 🌟 About The Project

This Python-based Twitter Auto-Post Bot automates tweeting, Credit to the Tweepy library for making this easy, this project enables scheduled and random tweets, offering a dynamic and engaging Twitter experience.

### 📁 Files Overview
#### Using OpenAI
##### Instantly:
- `src/instantly-tweet-from-openai.py`: Immediately tweets a tweet from openAI api response, currently using GPT4, but you can change the model in [functions.py](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot/blob/main/src/functions.py#L21)

- ###### Prompt defined [here](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot/blob/main/src/instantly-tweet-from-openai.py#L7) 

##### Schedule to auto post, tweet daily at a time:
- `src/schedule-daily-post-from-openai.py`: Automates daily tweets, Runs daily at a scheduled time and queries open ai api to create a tweet, the tweet returned is then automatically tweeted each day to fully automate twitter on auto pilot. By default the model is OPENAI GPT4 but you can change the model in [functions.py](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot/blob/main/src/functions.py#L21).
- ###### Prompt defined [here](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot/blob/main/src/schedule-daily-post-from-openai.py#L12) 
- ###### Schedule time defined [here](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot/blob/main/src/schedule-daily-post-from-openai.py#L20)

#### From File
- `src/schedule-daily-post-from-file.py`: Automates daily tweets, randomly selecting from `tweets.txt`. To change the schedule time [edit this](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot/blob/main/src/schedule-daily-post-from-file.py#L22).
- `src/tweeter-random-from-file.py`: Instantly posts a random tweet from `tweets.txt`.

###### Add your tweets to `data/tweets.txt`: one per line. They will be randomly selected and tweeted. 

#### Manually tweeting using script
`src/tweeter-from-code.py`: Immediately tweets a pre-defined message with the current date, but you can change this to whatever you like.

#### common files
- `config/keys.py`: Holds both the creds for openai and twitter api.
- `src/functions.py`: Shared functions for generating tweets from openai and tweet posting
- `requirements.txt`: Lists all necessary Python packages.

### ⭐ New: Command Line Interface (CLI)

The bot now includes a powerful CLI for easy management! See the [CLI Usage](#-cli-usage) section below.

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
2. update `config/keys.py` file with your credentials:
    ```python
   bearer_token = "GET_KEY_FROM_developer.twitter.com/apps"
   api_key = "GET_KEY_FROM_developer.twitter.com/apps"
   api_secret = "GET_KEY_FROM_developer.twitter.com/apps"
   access_token = "GET_KEY_FROM_developer.twitter.com/apps"
   access_token_secret = "GET_KEY_FROM_developer.twitter.com/apps"
   openai_key = "GET_YOUR_OPENAI_API_KEY_FROM_https://platform.openai.com/api-keys"
    ```
3. Customize `data/tweets.txt` with your tweets. (SKIP: If not using tweet from file)

## 🔧 Usage

### Option 1: Using the Web UI (Recommended)

The easiest way to use the bot is through the browser-based web interface. See the [Web UI Usage](#-web-ui-usage) section below.

### Option 2: Using the CLI

For command-line enthusiasts, see the [CLI Usage](#-cli-usage) section below for terminal-based commands.

### Option 3: Running Scripts Directly

Run any script using Python:

```bash
cd src/
python instantly-tweet-from-openai.py
```

## 🌐 Web UI Usage

The Web UI provides the easiest way to manage your Twitter bot through your browser.

### Starting the Web Interface

After installing dependencies with `pip install -r requirements.txt`, start the web server:

```bash
python web.py
```

The web interface will be available at: **http://localhost:5000**

Your browser should automatically open, or you can manually navigate to the URL.

### Web UI Features

#### Dashboard
- View bot status and scheduler state
- Test Twitter API credentials
- Quick access to all features
- Monitor scheduled jobs

#### Post Tweet
- **AI-Generated Tweets**: Generate tweets using OpenAI's GPT-4 with custom prompts
- **Random from File**: Post a random tweet from your tweets.txt library
- **Custom Tweet**: Write and post your own tweet with character counter

#### Manage Tweets
- View all tweets in your library
- Add new tweets to the library
- Edit existing tweets inline
- Delete unwanted tweets
- See library statistics

#### Schedule
- Schedule daily AI-generated tweets at specific times
- Schedule daily posts from your tweet library
- Monitor scheduler status in real-time
- Start/stop the scheduler
- View active scheduled jobs

### Web UI Tips

- The web server must remain running for scheduled tweets to work
- All times are in 24-hour format (HH:MM)
- Only one scheduler can run at a time
- The interface auto-refreshes scheduler status every 10 seconds

## 🎯 CLI Usage

The CLI provides a simple and intuitive interface for all bot operations.

### Installation

After installing dependencies with `pip install -r requirements.txt`, you can run the CLI:

```bash
python cli.py --help
```

### Available Commands

#### 1. Test Credentials

Test your Twitter API credentials:

```bash
python cli.py test
```

#### 2. Post a Tweet Instantly

**Post with AI (OpenAI):**
```bash
python cli.py post --ai
```

**Post with custom AI prompt:**
```bash
python cli.py post --ai --prompt "Create a tweet about Python programming"
```

**Post random tweet from file:**
```bash
python cli.py post --file
```

**Post custom text:**
```bash
python cli.py post --text "Hello Twitter! This is my custom tweet"
```

#### 3. Schedule Daily Tweets

**Schedule AI-generated tweets:**
```bash
python cli.py schedule-posts --ai --time "09:00"
```

**Schedule with custom prompt:**
```bash
python cli.py schedule-posts --ai --time "14:30" --prompt "Create a tweet about technology"
```

**Schedule tweets from file:**
```bash
python cli.py schedule-posts --file --time "12:00"
```

#### 4. Manage Tweets File

**List all tweets in file:**
```bash
python cli.py list-tweets
```

**Add a new tweet to file:**
```bash
python cli.py add-tweet
```

### CLI Tips

- All times are in 24-hour format (HH:MM)
- Press `Ctrl+C` to stop the scheduler
- The `--help` flag works with any command for more details
- Example: `python cli.py post --help`

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Contact
Project Link: [https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot](https://github.com/lewispour/Twitter-auto-Post-Bot---X.com---Tweepy-python-bot)

## ✉️ Status
- Last tested and still working on 04/12/2025 ✅
