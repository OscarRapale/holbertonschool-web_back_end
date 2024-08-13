#!/usr/bin/env python3


'''This function returns values form a list'''


import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Calculate the length of each sequence in an iterable.

    Parameters:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a sequence from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
