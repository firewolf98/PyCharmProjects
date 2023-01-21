from multiprocessing import Process
from multiprocessing import JoinableQueue
from multiprocessing import  Queue
from os import getpid
import time
def worker(jobs, report):

    while True:
        job = jobs.get()
        print("Processo ", getpid(), " job: ", job)
        report.put(job * job)
        time.sleep(2)
        jobs.task_done()



def create_process(jobs, report):
    for _ in range(4):
        process = Process(target=worker, args=(jobs, report))
        process.daemon = True
        process.start()

def create_jobs(numeri, jobs):
    for n in numeri:
        jobs.put(n)

def waitForComplete(jobs,report):
    jobs.join()

    while not report.empty():
        print(report.get_nowait())

if __name__ == '__main__':
    numeri = []
    for x in range(4):
        numeri.insert(0, x)
    print(numeri)
    report = JoinableQueue()
    jobs = JoinableQueue()

    create_process(jobs, report)

    create_jobs(numeri, jobs)
    time.sleep(2)
    waitForComplete(jobs, report)



