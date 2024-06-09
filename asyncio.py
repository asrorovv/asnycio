import asyncio

async def greet(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Good bye {name}")

async def main():
    await greet("Muhammadxon")
    await greet("Maqsudbek")
    await greet("Hasanjon")

asyncio.run(main())

