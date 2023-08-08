#!/usr/bin/env python3
""" A type-annotated function to_kv that takes a string """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and int/float and returns a tuple"""
    return (k, v ** 2)
