#!/usr/bin/env python3
""" A type-annotated function make_multiplier that takes a float multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and returns a float"""
    return (lambda x: multiplier*x)
