"""Generates a schedule based on the day of the week."""

import datetime

from utils.logger import get_logger


def get_schedule() -> str:
    """
    A function to generate a schedule based on the day of the week.

    :return: A list of tuples, each containing a time slot and a corresponding activity.
    """

    logger = get_logger()  # Initialize the logger
    logger.info("Generating a schedule based on the day of the week.")

    # Get the current day of the week
    day_of_week = datetime.datetime.today().weekday()

    # Define the unique parts of the schedule for each day of the week
    unique_schedule = {
        0: ["🏫🖋 Lectures and Library! :D", "🏫🖋 Lectures and Library! :D"],
        1: ["🏫🖋 Lectures and Library! :D", "🏫🖋 Lectures and Library! :D"],
        2: ["🏫🖋 Lectures and Library! :D", "💪🏋 Gym!"],
        3: ["🏫🖋 Lectures and Library! :D", "💪🏋 Gym!"],
        4: ["👽👽 Whatever you want, homie :)", "👽👽 Whatever you want, homie :)"],
        5: ["♟🏛 Chess Study", "💪🏋 Gym!"],
        6: ["💼💰 Tutoring Advertisement", "💪🏋 Gym!"],
    }

    final_schedule = [
        "- [ ] 08:00 - 09:00 🥫🍜 Breakfast, leave the house (maybe yoga?)",
        f"- [ ] 09:00 - 13:00 {unique_schedule[day_of_week][0]}",
        "- [ ] 13:00 - 14:00 🥫🍜 Lunch!!",
        f"- [ ] 14:00 - 18:00 {unique_schedule[day_of_week][1]}",
        "- [ ] 18:00 - 19:00 🥫🍜 Uh Oh - Dinner Moment",
        "- [ ] 19:00 - 20:00 📺🎬 Anime/Netflix",
        "- [ ] 20:00 - 21:00 💌💑 Time with Partner <3",
        "- [ ] 21:00 - 22:00 🚿🧼 Self-Care n' Hygiene",
        "- [ ] 22:00 - 23:00 📖🛋 Reading WOO",
        "- [ ] 23:00 - 00:00 🛌💤 Snooze Mode",
    ]

    # Convert schedule to a single string
    final_schedule_str = "\n".join(final_schedule)

    logger.info("Schedule generated successfully.")

    return final_schedule_str
