#!/usr/bin/env python3


'''function that returns a function that multiplies a float'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies its input by a specified multiplier.

    Parameters:
    multiplier (float): The multiplier to use in the created function.

    Returns:
    Callable[[float], float]: A function that multiplies its input by the specified multiplier.
    """

    def multiplier_function(value: float) -> float:
        """
        Multiply the input value by the specified multiplier.

        Parameters:
        value (float): The value to multiply.

        Returns:
        float: The result of multiplying the input value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
