#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coroutine
import asyncio


async def ping_server():
    print("this is test ping server")


async def ping_local():
    return await ping_server()


# use async def instead of coroutine
@asyncio.coroutine
def load_file(path):
    with open(path, 'r') as f:
        print(f.readlines())


## JavaScript Promises
## pass coroutine to event loop

print(asyncio.iscoroutinefunction(ping_server))
print(asyncio.iscoroutine(ping_server()))


## eventloop is for execution async functions

async def speak_async():
    print('OMG asynchronicity!')


loop = asyncio.get_event_loop()
loop.run_until_complete(speak_async()) # it is blocking
loop.close()

# Parallelism
# Multiprocessing