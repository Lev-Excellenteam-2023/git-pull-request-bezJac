def group_by(func, iterable):
    """
        Groups elements in the `iterable` by the result of applying `func` to each element.

       Args:
           func: A function that takes an element from the `iterable` as input and returns a key to group by.
           iterable: An iterable containing the elements to group.

       Returns:
           A dictionary where the keys are the results of applying `func` to the elements in `iterable`
           and the values are lists of elements from `iterable` that correspond to each key.
    """
    dic = {}
    for element in iterable:
        key = func(element)
        if key in dic:
            dic[key] = [dic[key], element]
        else:
            dic[key] = element
    return dic
