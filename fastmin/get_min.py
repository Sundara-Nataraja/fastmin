from .exceptions import EmptyArray


def get_min(arr):
    """
    the get min function uses binary search algorithm inorder to get the minimum element

    Parameters
    ----------
    arr : a homogenous list of integers/floats

    Returns
    -------
    Minimum element from the given array

    Examples
    --------
    >>> get_min([3,2,1,1,2,3]) # doctest: +SKIP
    >>> 1
    """

    array_length = len(arr)
    if array_length == 0:
        raise EmptyArray

    first = 0
    last = array_length - 1
    mid = 0
    while first < last:
        mid = (first + last) // 2

        if arr[mid] < arr[mid + 1]:
            last = mid
        else:
            first = mid

        if mid == last - 1:
            mid = last
            break
    return arr[mid]
