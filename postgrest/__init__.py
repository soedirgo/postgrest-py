import aiohttp


class Request:
    def __init__(self, url, session):
        self.session = session
        self.method = ''
        self.url = url
        self.params = []

    def __await__(self):
        return self.__aenter__().__await__()

    async def __aenter__(self):
        async with self.session.request(self.method, self.url, params=self.params) as response:
            return await response.json()

    async def __aexit__(self, exc_type, exc, tb):
        pass

    def select(self, column_query):
        self.method = 'GET'
        self.params.append(('select', column_query))
        return self


class Client:
    def __init__(self, rest_url):
        self.rest_url = rest_url
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    def from_table(self, table_name):
        url = f'{self.rest_url}/{table_name}'
        return Request(url, self.session)
