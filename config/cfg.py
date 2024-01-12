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
SCHEDULE_PROMPT = (
"""
- [ ] 06:00 - 06:30 🌅 Wake up and Breakfast **at home**
- [ ] 06:30 - 07:00 🚶‍♂️ Morning Walk **outside**
- [ ] 07:00 - 08:30 🏋️‍♂️ Train Calisthenics at the Gym **at the gym**
- [ ] 08:30 - 09:00 🧹 Quick Tidy Up **at home**
- [ ] 09:00 - 10:00 📰 Morning Briefing Read and Act on Dailies **at home**
- [ ] 10:00 - 11:00 📚 Read Mathematical Texts **at the library, first floor**
- [ ] 11:00 - 11:30 🥪 Quick Lunch Preparation and Eating **at home, unless I've prepared something**
- [ ] 11:30 - 12:30 💻 Work on Programming Projects **at the Isaac Newton Building**
- [ ] 12:30 - 13:00 📈 Implement Basic Marketing Strategy for Tutoring Services **at a café**
- [ ] 13:00 - 13:30 ♟️ Chess Activities (Learn Openings) **outside, or at the library, ground floor**
- [ ] 13:30 - 14:00 ♟️ Solve Chess Puzzles **outside, or at the library, ground floor**
- [ ] 14:00 - 15:00 🔍 Random Research **at the library, third floor**
- [ ] 15:00 - 16:00 💻📚 Continue Programming Projects (or More Math Reading) **at the Isaac Newton Building**
- [ ] 16:00 - 16:30 ♟️ Play a Chess Game **outside, or at the library, ground floor**
- [ ] 16:30 - 17:00 🇯🇵 Japanese Study (Genki I, Hiragana, Basic Kanji and Katakana) **at the library, second floor**
- [ ] 17:00 - 18:00 🍳 Culinary Study and Dinner Preparation **at home**
- [ ] 18:00 - 18:30 🍜📺 Dinner while Watching Anime **at home**
- [ ] 18:30 - 19:30 ❤️ Quality Time with Partner **at home**
- [ ] 19:30 - 20:00 🧘‍♂️ Meditation **at home**
- [ ] 20:00 - 21:00 🛋️ Relaxation / Free Time **at home**
- [ ] 21:00 - 21:30 🌜 Bedtime Routine **at home**
- [ ] 21:30 - 23:59 💤 Sleep **at home**

Add the following activity, or activities, to the schedule:

"""
)
SCHEDULE_CONTEXT = "You are a program that adjusts a given schedule to fit in new activities. You are given a schedule, and a new activity (or multiple activities). You must add the new activity to the schedule by moving and editing activities to make room for the new activity, and return the new schedule. If it's a similar activity, feel free to just replace it - the new activities take priority. Use the same format given for the response."

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
