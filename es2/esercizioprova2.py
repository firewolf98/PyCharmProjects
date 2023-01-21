from concurrent import futures

def worker(n, value, pos):
    list = []
    for _ in range(n):
        list.append(value)
    return list, pos

def scriviTutti(nomi, n, concurrency):
    futuresPool = set()

    with futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
        for i, nome in enumerate(nomi):
            future = executor.submit(worker, (n//(10**i)), nome, i)
            futuresPool.add(future)
    wait_for(futuresPool)

def wait_for(futuresPool):
    ordinata = []
    for risultato in futures.as_completed(futuresPool):
        #print(risultato.result()[1])
        ordinata.insert(risultato.result()[1], risultato.result()[0])
    print(ordinata)



def main():
    scriviTutti(['anna', 'paolo', 'giovanni', 'antonio'], 1000, 4)

if __name__ == '__main__':
    main()