#!/usr/bin/env python3
'''Async function task'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Import wait_random from 0-basic_async_syntax"""
    return asyncio.create_task(wait_random(max_delay)
