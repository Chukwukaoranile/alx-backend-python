#!/usr/bin/env python3
""" Annotate the below function’s parameters and return values """

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Duck typing """
    return [(i, len(i)) for i in lst]
