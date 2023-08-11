#!/usr/bin/env python3
""" Async coroutine """
from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ The coroutine for async comprehensing over async_generator,
        then return the 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
