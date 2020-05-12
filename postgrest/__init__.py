import asyncio


async def hello():
    print('Hello,', end='')
    await asyncio.sleep(1)
    print(' world!')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
