"""Contains utility functions for network requests."""
from typing import Dict, Optional

import requests
import urllib3
from time import sleep

from utils.logger import get_logger


def fetch_api_data(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None,
    max_retries: int = 3,
) -> Optional[Dict[str, str]]:
    """
    Fetch data from the given API URL with retries and return JSON data.

    :param url: The URL of the API to fetch data from.
    :param headers: A dictionary of headers to send with the request.
    :param params: A dictionary of parameters to send with the request.
    :param max_retries: Maximum number of retries for the request.
    :return: The JSON data returned from the API, or None if all attempts fail.
    """

    logger = get_logger()  # Get the logger for the application
    urllib3.disable_warnings(
        urllib3.exceptions.InsecureRequestWarning
    )  # Disable SSL warnings

    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as errh:
            logger.error(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            logger.error(f"Error Connecting: {errc}")
            retry_count += 1
            sleep(2**retry_count)  # Exponential backoff
        except requests.exceptions.Timeout as errt:
            logger.error(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            logger.error(f"Error: {err}")

    logger.error("Max retries exceeded. Request failed.")
    return None
