import re


def phone(strng, num):
    """ This is a solution for a codewars.com kata
    https://www.codewars.com/kata/56baeae7022c16dd7400086e/

    Args:
        strng (str): A badly malformed phonebook separated by linebreaks
        num (str): the number

    Returns:
        str: a nice entry or error message


    SPOILERS AHEAD
    """

    book = strng.split("\n")
    result = None
    for entry in book:
        if num in entry:
            if result:
                result = "Error => Too many people: {num}".format(num=num)
                break
            name_tag = re.findall("<[a-zA-Z' ]*>", entry)
            entry = entry.replace(name_tag[0], "")
            entry = entry.replace(num, "")
            entry = entry.replace("_", " ")
            entry = re.subn("[^a-zA-Z0-9.\- ]", "", entry)
            entry = re.subn("  ", " ", entry[0])
            address = entry[0].strip()
            name = re.subn("[<>]", "", name_tag[0])[0]
            result = "Phone => {num}, Name => {name}, Address => {address}"
            result = result.format(
                num=num,
                name=name,
                address=address
            )
    if not result:
        result = "Error => Not found: {num}".format(num=num)

    return result
