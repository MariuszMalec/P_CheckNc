import time
import asyncio

# Synchronous function
def sync_task(name, delay):
    print(f"Start sync task {name}")
    time.sleep(delay)
    print(f"End sync task {name}")

# Asynchronous function
async def async_task(name, delay):
    print(f"Start async task {name}")
    await asyncio.sleep(delay)
    print(f"End async task {name}")

# Run synchronous tasks
def run_sync():
    print("\nRunning synchronous tasks...")
    start = time.time()
    sync_task("A", 2)
    sync_task("B", 2)
    end = time.time()
    print(f"Synchronous total time: {end - start:.2f} seconds")

# Run asynchronous tasks
async def run_async():
    print("\nRunning asynchronous tasks...")
    start = time.time()
    await asyncio.gather(
        async_task("A", 2),
        async_task("B", 2)
    )
    end = time.time()
    print(f"Asynchronous total time: {end - start:.2f} seconds")

if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())
