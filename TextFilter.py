import re

def extract_numbers(text):
    # Extract all numbers from text
    numbers = re.findall(r'\d+', text)
    return numbers
