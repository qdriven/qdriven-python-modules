#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio


# https://realpython.com/async-io-python/

async def py34_coro():
    """Generator-based coroutine"""
    # No need to build these yourself, but be aware of what they are
    s = await stuff()
    return s


async def py35_coro():
    """Native coroutine, modern syntax"""
    s = await stuff()
    return s


async def stuff():
    return 0x10, 0x20, 0x30


if __name__ == '__main__':
    py35_coro()
    py34_coro()
