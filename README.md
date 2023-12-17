# Simple Morning Briefing Generation

## Description
Simple Morning Briefing Generation is a Python project that automates the creation of a morning briefing. Utilizing various APIs and manual data sources, this tool compiles a comprehensive markdown document. The briefing includes a range of data such as a daily haiku, weather updates, news headlines, calendar events, email summaries, chess puzzles, a custom good luck message, and random emojis. This is all customizable through the `morning-briefing-template.md` file.

## Features
- **Customizable Briefing:** Modify the `morning-briefing-template.md` to tailor the briefing content.
- **Comprehensive Data Gathering:** Pulls data from various APIs and manual sources.
- **User-friendly:** Simple setup and easy execution.

## Requirements
- Python Libraries: `os`, `datetime`, `pathlib`, `jinja2`, `logging`, `typing`, `requests`, `urllib3`, `icalendar`, `pickle`, `google.auth.transport.requests`, `google_auth_oauthlib.flow`, `googleapiclient.discovery`, `random`, `openai`, `itertools`, `feedparser`, `collections`, `rich.logging`.
- Optional: OpenAI and OpenWeather API keys for enhanced functionality.

## Installation
1. Clone the repository.
2. Configure the `cfg.py` file with LLM prompts, news URLs, calendar URLs, file paths, etc.
3. Set OpenAI and OpenWeather API keys as environment variables for full feature access (optional).

## Usage
Run the `main.py` script and follow the instructions. The program generates a morning briefing based on the configured template and sources.

## Contribution
Contributions are welcome! This project was created with the assistance of ChatGPT 4 and evaluated by my brother. Please feel free to suggest improvements, add features, or report issues.

## License
This project is under the MIT License.

## Contact
For any queries or contributions, please contact me at [wills@fayers.com](mailto:wills@fayers.com).