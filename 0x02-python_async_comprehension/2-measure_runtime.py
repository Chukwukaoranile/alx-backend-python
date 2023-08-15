#!/usr/bin/env python3
""" Async coroutine """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """  A measure_runtime coroutine for async_comprehension """

    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
