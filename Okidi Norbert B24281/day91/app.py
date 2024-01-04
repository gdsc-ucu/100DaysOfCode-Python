import asyncio

async def long_running_task():
    try:
        print("Task Started---")
        await asyncio.sleep(10)
        print("Task Completed")
    
    except asyncio.CancelledError:
        print("Task Cancelled")

async def main():
    try:
        await asyncio.wait_for(long_running_task(),timeout=5)
    
    except asyncio.TimeoutError:
        print("Task Timeout after 5 seconds")

if __name__ == "__main__":
    asyncio.run(main())