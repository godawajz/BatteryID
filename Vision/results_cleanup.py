import ast
import re
from difflib import SequenceMatcher
from typing import Final


# find battery info method specifically tailored to OpenOCR formatted output.
# it currently returns in list format to allow for the possibility of multiple battery results.
def find_battery_info(text) -> list[list[str | float]]:
    to_append: str  = ""# the battery type to be added to the list
    item_processed: str = ""  # the transcription item after the word 'battery' is removed for easier ratio calculation
    max_ratio : float = 0.0  # used to find the closest match to the recognized batteries
    contains: bool = False  # is true if the transcription item matches a recognized battery over 70% of the time
    ratio: float  = 0.0  # the current working ratio in a loop
    RECOGNIZED_BATTERIES: Final[list[str]] = ['li-ion polymer', 'li-ion']
    relevant_info = []  # list of necessary battery information to be returned


    index = text.find('[') # OpenOCR stores lists as a string, with extra text. Remove extra text before list.
    if index != -1:
        transcriptions = ast.literal_eval(text[index:]) # extract list

        for item in transcriptions:
            item_processed = re.sub(r'\b' + re.escape('battery') + r'\b', '', item['transcription'],
                                    flags=re.IGNORECASE)

            for battery in RECOGNIZED_BATTERIES:
                contains, ratio = contains_ignore_case_spaces(item_processed, battery)
                if contains and ratio > max_ratio:
                    to_append = ("Battery type: " + battery)
                    max_ratio = ratio
            relevant_info.append([to_append, ratio])
    return relevant_info  # Empty if value not found


# Models may have discrepancies with spelling and capitalization.
# Checks if the arguments
def contains_ignore_case_spaces(text, pattern) -> tuple[bool, float]:
    text_processed = "".join(text.split()).casefold()
    pattern_processed = "".join(pattern.split()).casefold()
    battery_ratio = SequenceMatcher(None, text_processed, pattern_processed).ratio()
    return battery_ratio >= .7, battery_ratio