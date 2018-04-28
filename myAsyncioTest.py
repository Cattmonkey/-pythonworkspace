# -*- coding: utf-8 -*-
"""
Created on  20180426

@author: yyx
"""

import time
import asyncio
import functools

now = lambda: time.time()

async def do_some_work(x, y):
    print('Waiting: ', y)
    await asyncio.sleep(y)
    return x + y
    # future.set_result(f'{y} Future is done!')

async def print_sum(x, y):
    result = await do_some_work(x, y)  # 协程print_sum不会继续往下执行，直到协程compute返回结果
    print("%s + %s = %s" % (x, y, result))
    # await print_sum(x, y+1)


def callback(t, future):
    print(f'Callback: {t} {future.result()}')

start = now()

# coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# future = asyncio.Future()
# asyncio.ensure_future(print_sum(1,2, future))
future = [asyncio.ensure_future(print_sum(1, 3)),
          asyncio.ensure_future(print_sum(1, 2))]
futures = asyncio.gather(*future)
futures.add_done_callback(functools.partial(callback, 2))
# print(task)
# task.add_done_callback(functools.partial(callback, 2))
# loop.run_until_complete(task)

# print(task)
try:
    # loop.run_forever()
    loop.run_until_complete(futures)
    # loop.close()
finally:
    loop.close()
print('TIME: ', now() - start)
