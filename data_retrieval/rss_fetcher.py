"""Fetches news articles from RSS feeds."""
from itertools import cycle, islice

import feedparser

from utils.logger import get_logger
from data_retrieval.openai_integration import prompt_gpt4_turbo
from config.cfg import OPENAI_API_KEY, NEWS_CONTEXT


def fetch_news(
    rss_urls: dict[str, list[str]], max_articles_per_category: int = 4
) -> str:
    """
    Fetches a limited number of news articles from multiple RSS feed URLs, alternating between sources, and converts them to natural language.

    :param rss_urls: A dictionary of RSS feed URLs, with the key being the category and the value being a list of URLs.
    :param max_articles_per_category: The maximum number of articles to fetch per category.
    :return: Natural language news articles.
    """

    markdown_output = ""
    logger = get_logger()  # Get the logger for the application
    logger.info("Starting to fetch news articles.")

    for category, urls in rss_urls.items():
        logger.info(f"Fetching news articles for {category}.")
        markdown_output += f"## {category}\n\n"
        seen_titles = set()  # Set to store titles for deduplication
        articles_count = 0

        # Create an iterator that cycles through the URLs
        url_cycle = cycle(urls)
        while articles_count < max_articles_per_category:
            url = next(url_cycle)  # Get the next URL in the cycle
            logger.info(f"Fetching news from {url}.")
            try:
                feed = feedparser.parse(url)
                if feed.bozo:
                    continue

                # Use islice to get an iterator for the first unseen entry
                entries = (
                    entry for entry in feed.entries if entry.title not in seen_titles
                )
                entry = next(islice(entries, 1), None)

                # If we have an unseen entry, process it
                if entry:
                    title = entry.title
                    link = entry.link
                    markdown_output += f"- [{title}]({link})\n"
                    seen_titles.add(title)
                    articles_count += 1
                    logger.info(f"Fetched news from {url}.")
            except Exception as e:
                logger.error(f"An error occurred while fetching news from {url}: {e}")
                continue  # Continue with the next URL if an error occurred

        logger.info(f"Fetched {articles_count} news articles for {category}.")
        markdown_output += "\n"

    # Converts the news into natural language using GPT-4
    logger.info("Converting news articles to natural language.")
    natural_language_news = prompt_gpt4_turbo(
        OPENAI_API_KEY, markdown_output, NEWS_CONTEXT
    )

    return natural_language_news
