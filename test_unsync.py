from unsync import unsync
from time import sleep
from time import ctime
from random import randint
import asyncio

@unsync
async def async_sleepy_gary(name: str) -> str:
    await asyncio.sleep(randint(1, 4))
    return f"{ctime()} {name}"

#@unsync(cpu_bound=True)
@unsync
def sleepy_gary(name: str) -> str:
    sleep(randint(1, 4))
    return f"{ctime()} {name}"


def main():

    tasks = []
    for i in range(5):
        tasks.append(sleepy_gary(f"{i}_th"))

    for i in range(5):
        tasks.append(async_sleepy_gary(f"{i}_async"))


    print([t.result() for t in tasks])

if __name__ == '__main__':
    main()
