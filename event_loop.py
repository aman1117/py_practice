import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Simulate a long-running I/O operation
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(4)
    print("Task 2 finished")

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(task1(), task2())

# Run the event loop
asyncio.run(main())
