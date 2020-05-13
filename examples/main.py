#!/usr/bin/env python3

import asyncio

from postgrest import Client


async def main():
    async with Client('https://hacks.soedirgo.dev/postgrest') as client:
        response = await client.from_table('todos').select('*')
        print(response)


if __name__ == '__main__':
    asyncio.run(main())
