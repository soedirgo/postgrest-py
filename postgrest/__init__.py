import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://supabase.io') as response:
            print(f'Status: {response.status}')
            print(f'Content-type: {response.headers["content-type"]}')

            html = await response.text()
            print(f'Body: {html[:15]} ...')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
