#  Coroutine

Before learning coroutine, let see the [history of Process and Thread](https://www.liaoxuefeng.com/wiki/1016959663602400/1017631469467456). Coroutine is better than them in most cases.

Coroutine uses **event loop**, controls the timing of each tasks.

To learn more about **event loop**, check **nginx**.

Coroutine needs `async I/O`.

```python
import time
import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')

%time asyncio.run(main())

# # # # # # # # # #  output # # # # # # # # # # 

before await
worker_1 start
worker_1 done
awaited worker_1
worker_2 start
worker_2 done
awaited worker_2
Wall time: 3 s
```

In this example, all the function are `async`. However, we use `async / await` to make them run `sync`.

To run them in coroutine, we need to create `task` using `asyncio.create_task`.

```python

import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

%time asyncio.run(main())

# # # # # # # # # #  output # # # # # # # # # # 

before await
worker_1 start
worker_2 start
worker_1 done
awaited worker_1
worker_2 done
awaited worker_2
Wall time: 2.01 s
```

In this exemple, we did following thing:

1. run `asyncio.run(main())`: start event loop
2. create 2 tasks
3. run `await task1`: leave the `main`, enter `worker_1`
4. run `await asyncio.sleep(1)` in `worker_1`: leave `worker_1`, enter `worker_2`
5. run `await asyncio.sleep(2)` in `worker_2`: leave `worker_2`, enter `worker_1`
6.`work_1` finished: leave `worker_1`, enter `main`
7. run `print('awaited worker_1')`: leave `main`, enter `worker_2`
8. `worker_2` finished: leave `worker_2`, enter `main`

As we can see, `main`, `worker_1`, `worker_2` works together. One of them sleeps, we run one of the rest.

There is another way to run tasks:

```python
await asyncio.gather(task_1, task_2)
```

It's simpler.