"""Pracice with dictionary functions"""

__author__: str = "730824316"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary"""
    inverted_dict: dict[str, str] = {}
    for key in my_dictionary:
        if my_dictionary[key] in inverted_dict:
            raise KeyError(f"Duplicate value found!")
        inverted_dict[my_dictionary[key]] = key
    return inverted_dict


def count(given_list: list[str]) -> dict[str, int]:
    """Creating a dictionary to keep track of count of elements appearing in list"""
    idx: int = 0
    dict_created: dict[str, int] = {}

    while idx < len(given_list):
        if given_list[idx] in dict_created:
            dict_created[given_list[idx]] += 1
        else:
            dict_created[given_list[idx]] = 1
        idx += 1
    return dict_created


def favorite_color(favcol: dict[str, str]) -> str:
    """What color is most popular?"""

    popular_color: str = ""
    max_count_color: int = 0
    color_count: dict[str, int] = {}

    for key in favcol:
        value_in_favcol: str = favcol[key]
        if value_in_favcol in color_count:
            color_count[value_in_favcol] += 1
        else:
            color_count[value_in_favcol] = 1

    for color in color_count:
        value_in_color_count: int = color_count[color]
        if value_in_color_count > max_count_color:
            max_count_color = value_in_color_count
            popular_color = color

    return popular_color


def bin_len(list_of_strings: list[str]) -> dict[int, set[str]]:
    """Creating a dictionary that organizes strs in list by their length"""
    result: dict[int, set[str]] = {}
    for word in list_of_strings:
        length: int = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
