import asyncio

async def foo():

    await asyncio.sleep(1)

    print("Foo")

async def bar():

    await asyncio.sleep(2)

    print("Bar")

async def main():

    task1 = asyncio.create_task(foo())

    task2 = asyncio.create_task(bar())

    await asyncio.gather(task1, task2)

asyncio.run(main())

