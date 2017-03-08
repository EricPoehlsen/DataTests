import re


def alphabet_position(text):
    text = text.lower()
    text = re.subn("[^a-z]", "", text)[0]
    numbers = []
    for letter in text:
        numbers.append(str(ord(letter) - 96))

    return " ".join(numbers)
