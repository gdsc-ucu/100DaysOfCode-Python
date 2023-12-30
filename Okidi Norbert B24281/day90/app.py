import asyncio

async def async_task(task_name, should_raise):
    if should_raise:
        raise ValueError(f"Error in {task_name}")
    else:
        print(f"{task_name} completed successfully")

async def main():
    tasks = [
        async_task("Task 1", False),
        async_task("Task 2", True),
        async_task("Task 3", False)
    ]

    try:
        await asyncio.gather(*tasks)
    except ValueError as e:
        print(f"Caught exception: {e}")

if __name__ == "__main__":
    asyncio.run(main())