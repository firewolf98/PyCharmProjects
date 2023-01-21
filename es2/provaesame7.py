from concurrent import futures

def worker(job):
    return job*job

def get_jobs(jobs):
    for x in jobs:
        yield x

def createFutures(list, concurrency):
    poolExecutor = set()
    with futures.ProcessPoolExecutor(max_workers = concurrency) as Executor:
        for job in get_jobs(list):
            future = Executor.submit(worker, job)
            poolExecutor.add(future)
    wait_for_end(poolExecutor)


def wait_for_end(poolExecutor):
    for result in futures.as_completed(poolExecutor):
        print(result.result())


if __name__ == '__main__':
    list = [1,2,3,4]
    createFutures(list,4)

