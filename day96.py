#async io
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())

# multiple program
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def say_hi():
    print("Hi")
    await asyncio.sleep(1)
    print("There")

async def main():
    asyncio.gather
    (
        await say_hello(),
        await say_hi()
    )
asyncio.run(main())