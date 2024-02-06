"""Generates a workout based on the day of the week, based on the Alberto Nuñez Upper Lower Program"""

from datetime import datetime
from typing import List

from utils.logger import get_logger


def get_workout() -> List[str] | None:
    """
    A function to get a workout based on the day of the week, based on the Alberto Nuñez Upper Lower Program.

    :return: A list of strings, each string being a line of the workout.
    """

    logger = get_logger()  # Initialize the logger
    logger.info("Starting to get a workout.")

    # Get the day of the week
    day = datetime.today().weekday()
    logger.info(f"Today is day {day} of the week.")

    # Get the workout based on the day of the week
    if day == 2:
        workout = [
            "| Seated Front Raise (Dumbbell)              | 1    | 10-15  | @10   |",
            "| Seated Anterior Delt Press                 | 3    | 06-10  | @7-10 |",
            "| Standing Lateral Raise (Cable)             | 3    | 10-17  | @8-10 |",
            "| Standing Overhead Tricep Extension (Cable) | 3    | 10-15  | @10   |",
            "| Prone Rear Delt Fly (Dumbbell)             | 1    | 10-15  | @10   |",
            "| Prone Rear Delt Row (Cable)                | 3    | 06-10  | @7-10 |",
            "| Standing Bicep Curl (Cable)                | 3    | 10-17  | @10   |",
        ]
    elif day == 3:
        workout = [
            "| Glute Bridge (Barbell)      | 1    | 10-15  | @10   |",
            "| Romanian Deadlift (Barbell) | 2    | 06-10  | @7-8  |",
            "| Hip Dominant Leg Press      | 2    | 06-10  | @7-9  |",
            "| Seated Leg Curl             | 2    | 06-10  | @8-10 |",
            "| Seated Calf Raise           | 2    | 06-10  | @8-10 |",
        ]
    elif day == 5:
        workout = [
            "| Bench Press (Dumbbell)         | 2    | 06-10  | @7-10 |",
            "| Lat Dominant Row (Cable)       | 2    | 06-10  | @7-10 |",
            "| Incline Bench Press (Dumbbell) | 2    | 06-10  | @7-10 |",
            "| Neutral Grip Lat Pulldown      | 2    | 06-10  | @7-10 |",
            "| Tricep Extension (Cable)       | 2    | 10-15  | @10   |",
            "| Hammer Curl (Cable)            | 2    | 10-15  | @10   |",
        ]
    elif day == 6:
        workout = [
            "| Quad Dominant Leg Press           | 2    | 06-10  | @7-9  |",
            "| Leg Extension                     | 2    | 10-15  | @10   |",
            "| Sissy Squat                       | 2    | 1+     | @9-10 |",
            "| Standing Lateral Raise (Dumbbell) | 3    | 10-15  | @10   |",
            "| Straight Leg Calf Raise           | 2    | 06-10  | @7-9  |",
            "| Abs Crunch (Cable)                | 2    | 06-10  | @7-9  |",
        ]
    else:
        logger.info("Skipping workout generation - rest day.")
        return None

    logger.info("Completed getting the workout.")

    workout = (
        "| Exercise                                   | Sets | Reps   | RPE   |\n| ------------------------------------------ | ---- | ------ | ----- |\n"
        + "\n".join(workout)
    )
    return workout
