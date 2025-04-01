import ast
from difflib import SequenceMatcher


# find battery info method specifically tailored to OpenOCR formatted output.
def find_battery_info(text):
    relevant_info = []
    index = text.find('[') # OpenOCR stores lists as a string, with extra text. Remove extra text before list.
    if index != -1:
        transcriptions = ast.literal_eval(text[index:]) # extract list
        for item in transcriptions:
            if contains_ignore_case_spaces(item['transcription'], 'li-ion polymer'):
                relevant_info.append("Battery type: " + 'Li-Ion Polymer')
    return relevant_info  # Empty if value not found


# Models may have discrepencies with spelling and capitalization.
#
def contains_ignore_case_spaces(text, pattern):
    text_processed = "".join(text.split()).casefold()
    pattern_processed = "".join(pattern.split()).casefold()
    return SequenceMatcher(None, text_processed, pattern_processed).ratio() >= .7