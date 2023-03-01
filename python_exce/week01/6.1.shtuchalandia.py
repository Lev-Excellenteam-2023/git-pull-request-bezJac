def find_special_state():
    """
    Out of the states.txt file, print the name of the only US state that can be spelled using letters from a single row
    of a QWERTY keyboard.

    Args:
        None.

    Returns:
        None.
    """
    top_row = set('qwertyuiop')
    middle_row = set('asdfghjkl')
    bottom_row = set('zxcvbnm')

    with open("states.txt", 'r') as file:
        for line in file:
            line_set = set(line.rstrip('\n'))
            if (top_row.issuperset(line_set)) or (middle_row.issuperset(line_set)) or (bottom_row.issuperset(line_set)):
                print(line)
