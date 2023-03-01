import math


def full_names(first_names, last_names, min_length=-math.inf):
    """
    Return a list of full names created by joining each first name in the first_names list with
    each last name in the last_names list, capitalizing the first letters of each name, and
    filtering out any names with a length less than min_length (which defaults to negative infinity).

    Args:
        first_names (list): A list of first names (str).
        last_names (list): A list of last names (str).
        min_length (int, optional): The minimum length of full names to be included in the output.
                                    Defaults to negative infinity.

    Returns:
        A list of full names (str) created by joining each first name in first_names with each last name in last_names.
    """
    join_names = lambda first, last: (first + " " + last).title()
    full_list = [join_names(first, last) for first in first_names for last in last_names]

    length_check = lambda name: len(name) >= min_length
    return list(filter(length_check, full_list))
