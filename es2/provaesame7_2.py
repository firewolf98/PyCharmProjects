import multiprocessing
import time
def worker(queue, results):
    while True:
        job = queue.get()
        results.put(job*job)
        queue.task_done()

def createprocess(queue, concurrency, result):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker,args=(queue, result))
        process.daemon = True
        process.start()

def createjobs(queue, list):
    for x in list:
        queue.put(x)

def wait_for(queue, result):
    queue.join()
    while not result.empty():
        print(result.get_nowait())

if __name__ == '__main__':
    queue = multiprocessing.JoinableQueue()
    list = [1, 2, 3, 4]
    createjobs(queue, list)

    result = multiprocessing.Queue()

    createprocess(queue,4, result)

    wait_for(queue, result)