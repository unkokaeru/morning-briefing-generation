"""Contains functions for fetching data from lichess.org."""
from typing import cast

from utils.network_utils import fetch_api_data
from utils.logger import get_logger


def fetch_chess_puzzle(query: dict[str, str]) -> str:
    """
    Fetch a chess puzzle from lichess.org and return its details in a formatted string.

    :param query: A dictionary containing the query parameters for the API.
    :return: A string with the puzzle's FEN, rating, and solution.
    """

    logger = get_logger()  # Initialize the logger
    logger.info("Starting to fetch a chess puzzle.")

    url = "https://chess-puzzles.p.rapidapi.com/"
    headers = {
        "X-RapidAPI-Key": "90d069b03emsh494903ef45a4734p10d481jsn832ac943fdeb",
        "X-RapidAPI-Host": "chess-puzzles.p.rapidapi.com",
    }
    logger.info(f"Sending request to {url} with query parameters: {query}")

    puzzle_data = fetch_api_data(url, headers, query)

    if puzzle_data is None:
        logger.error("Failed to fetch puzzle data.")
        return "..."

    try:
        puzzle = cast(dict, puzzle_data["puzzles"][0])
        logger.info("Successfully retrieved puzzle data.")

        puzzle_details = (
            f"Here's a puzzle to think about today, it's a bit harder than your usual puzzles at a rating of {puzzle['rating']}. The puzzle ID is [{puzzle['puzzleid']}](https://lichess.org/training/{puzzle['puzzleid']}) in case you want a bit of a hint or you want to check your solution in a more visual way!\n"
            "\n"
            "```chessboard\n"
            f"fen: {puzzle['fen']}\n"
            "```\n"
            "\n"
            "Spoilers! Below is the solution, so try and put your solution below it first so you can check them - but only once you're confident!\n"
            "\n"
            "```spoiler-block\n"
            f"{puzzle['moves']}\n"
            "```"
        )

        logger.info("Puzzle data processed successfully.")
        return puzzle_details
    except (KeyError, IndexError):
        logger.error("Error processing puzzle data.")
        return "..."
