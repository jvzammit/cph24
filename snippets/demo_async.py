import asyncio
import time


async def say_hello(x: int):
    await asyncio.sleep(1)  # simulate I/O blocking call
    print(f"{time.strftime('%X')} - Hello world {x}")


async def main():
    print(f"{time.strftime('%X')} - Started")
    # asyncio.TaskGroup runs multiple instances of say_hello concurrently
    async with asyncio.TaskGroup() as task_group:
        for i in range(5):
            task_group.create_task(say_hello(i))


# To run the async function in an event loop
asyncio.run(main())
