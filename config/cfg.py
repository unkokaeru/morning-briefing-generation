"""Configuration file for the morning briefing application."""
import os

from rich.logging import RichHandler

# AI Prompting Configuration
MATHS_PROMPT = "Generate an interesting maths problem for a maths undergraduate student to solve in about five minutes. Use Markdown and Latex if needed. Do not provide a solution, just a final answer."
LUCK_PROMPT = "Give me a short good luck message! :D"
LUCK_CONTEXT = "You are a fun motivator!"
EMOJI_PROMPT = (
    "Give me some random emojis! :D - just return the emojis though, nothing else."
)
NEWS_CONTEXT = "You are a personal assistant briefing someone on the news, seamlessly transitioning between topics and including hyperlinks to news headline sources. Make sure that you give a response in just prose, and not in a list format."
CAL_CONTEXT = "You are a personal assistant briefing someone on their calendar events for the day, seamlessly transitioning between events and including just the time (in the format hh:mm) with each event description. Make sure that you give a response in just prose, and not in a list format."
EMAIL_CONTEXT = "You are a personal assistant briefing someone on their email subjects for the day, seamlessly transitioning between subjects. Make sure that you give a response in just prose, and not in a list format."
SCHEDULE_PROMPT = """
- [ ] 08:00 - 09:00: Breakfast
- [ ] 09:00 - 10:00: Library/Hobby
- [ ] 10:00 - 11:00: Library/Hobby
- [ ] 11:00 - 12:00: Library/Hobby
- [ ] 12:00 - 13:00: Library/Hobby
- [ ] 13:00 - 14:00: Lunch
- [ ] 14:00 - 15:00: Library/Gym
- [ ] 15:00 - 16:00: Library/Gym
- [ ] 16:00 - 17:00: Library/Gym
- [ ] 17:00 - 18:00: Library/Gym
- [ ] 18:00 - 19:00: Dinner
- [ ] 19:00 - 20:00: Anime
- [ ] 20:00 - 21:00: Partner Time
- [ ] 21:00 - 22:00: Self-Care/Hygiene
- [ ] 22:00 - 23:00: Reading Time
- [ ] 23:00 - 00:00: Sleep

Add the following activity, or activities, to the schedule:

"""
SCHEDULE_CONTEXT = "You are a program to replace hour slots with new given activities. Replace similar activities, e.g. replace 'Library/Hobby' with 'Maths Lecture' because it fits the library theme. Give the response in a list format, with each activity on a new line, as it was given to you: give nothing else in the response."

# RSS Feed URLs
RSS_URLS = {
    "Global News": [
        "http://feeds.bbci.co.uk/news/world/rss.xml",  # BBC World News
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",  # NY Times World News
        "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera English
        "https://www3.nhk.or.jp/rj/podcast/rss/english.xml",  # NHK World English
    ],
    "Lincoln News": [
        "https://www.lincolnshirelive.co.uk/news/?service=rss",  # Lincolnshire Live
        "https://thelincolnite.co.uk/feed/",  # The Lincolnite
    ],
    "Mathematical News": [
        "https://www.sciencedaily.com/rss/strange_offbeat.xml",  # ScienceDaily - Strange & Offbeat
        "https://www.sciencedaily.com/rss/top/science.xml",  # ScienceDaily - Top Science News
        "https://www.ams.org/rss/mathmoments.xml",  # AMS - Math Moments
        "https://www.ams.org/rss/conm.rss",  # AMS - Contemporary Mathematics
    ],
}

# ICS Calendar URLs
CAL_URLS = [
    "https://calendar.google.com/calendar/ical/wills%40fayers.com/private-60149c6c42b754d0c98bbcfc72cc47ef/basic.ics",
    "https://calendar.google.com/calendar/ical/c_417sngltsr9kp47l52c9978du0%40group.calendar.google.com/private-735f2692630830375e8a3007ee272360/basic.ics",
    "https://blackboard.lincoln.ac.uk/webapps/calendar/calendarFeed/bf8217b5a6ef45099542d518470fdb29/learn.ics",
    "https://timetable.lincoln.ac.uk/ical/8OzbTTa18Dagy6spCOpfPixa2aOdIJeyrPczNPOva3X89vnBIBPYMEKkYa3pTYdZAT14LfwGmAQ",
]

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(message)s",
    "datefmt": "[%X]",
    "handlers": [RichHandler(rich_tracebacks=True)],
}

# Chess Puzzle Configuration
CHESS_CONFIG = {"rating": "1500", "themesType": "ALL"}

# File Paths
HAIKU_PATH = "C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\Main User Facing Pages\\My Haikus.md"

# fetch API keys from .env file or prompt user to enter them manually
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", input("Enter your OpenAI API key: "))
OPEN_WEATHER_API_KEY = os.getenv(
    "OPEN_WEATHER_API_KEY", input("Enter your OpenWeather API key: ")
)

# Gmail API Credentials
CREDS_PATH = "C:\\Users\\wills\\Documents\\GitHub\\morning-briefing-generation\\config\\credentials.json"

# Where to save the generated markdown document
SAVE_LOCATION = "C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\Main User Facing Pages\\Day by day\\"
