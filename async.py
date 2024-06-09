
from datetime import datetime
import asyncio

async def data():

    print(f"Start! at {datetime.now()}")
    await asyncio.sleep(2)
    print(f"End! at {datetime.now()}")
    return {'data': 1}

async def numbers():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(data)
    task2 = asyncio.create_task(numbers())
    x = await task1
    print(x)
    await task2

asyncio.run(main())