# -*- coding: UTF-8 -*-
import asyncio
from time import time

import aiohttp
import requests


def do_requests():
    resp = requests.get('https://www.yahoo.com.tw/')
    print(f'https://www.yahoo.com.tw/ => {resp.status_code}')


def block_waiting_requests():
    t_start = time()
    for _ in range(0, 10):
        do_requests()
    print(f'blocking requests taken: {time() - t_start:.2f} secs')
    # 大約需要7.75秒執行時間


def do_async_requests(session):
    return session.get('https://www.yahoo.com.tw/')


async def waiting_requests():
    t_start = time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(0, 10):
            tasks.append(do_async_requests(session))

        results = await asyncio.gather(*tasks)
        for r in results:
            print('https://www.yahoo.com.tw/', r.status)
    print(f'async requests taken: {time() - t_start:.2f} secs')
    # 大約需要1秒執行時間


if __name__ == '__main__':
    block_waiting_requests()
    asyncio.run(waiting_requests())
