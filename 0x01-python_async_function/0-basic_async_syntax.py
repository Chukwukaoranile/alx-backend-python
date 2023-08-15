#!/usr/bin/env python3
'''Async function basics'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''A function that takes integer as args.'''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
