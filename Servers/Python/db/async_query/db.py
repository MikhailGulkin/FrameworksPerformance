import asyncpg


class Database():

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(
            database='SpeedTest',
            user='postgres',
            port='5431',
            password='1234',
            host='localhost',
        )
