#!/usr/bin/env python3


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Takes 2 arguments and returns a tuple

    Args:
        k (str): string
        v (Union[int, float]): int or float

    Returns:
        Tuple[str, float]: returns a tuple
    '''
    square = pow(v, 2)
    mxd = (k, square)
    return mxd
