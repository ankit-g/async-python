import asyncio, time

async def main():
    print(f"{time.ctime()}, Hello!!!")
    await asyncio.sleep(1)
    print(f"{time.ctime()}, GoodBye!!!")

def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello From Thread!!!")

# get an event loop
loop = asyncio.get_event_loop()
print(loop)
# schedules the coroutine to be run on the loop.
# returned task can be used to monitor states of the task.
# this task can aslo be used to get the return values of the coroutine.
task = loop.create_task(main())
print(task)

#this runs the blocking code in a saparate thread
loop.run_in_executor(None, blocking)
# this blocks the main thread
loop.run_until_complete(task)

# returns all pending tasks in a set.
pending = asyncio.all_tasks(loop=loop)
for t in pending:
    task.cancel()

# gather all pending tasks and run thme untill complete.
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
print(loop)

