from multiprocessing import JoinableQueue, Queue, Process

def create_processes(codaLavori, codaRisultati, numProcessi):
    for _ in range(numProcessi):
        processo = Process(target=square, args=(codaLavori, codaRisultati))
        processo.daemon = True
        processo.start()

def add_jobs(codaLavori, numeri):
    for numero in numeri:
        codaLavori.put(numero)

def square(codaLavori, codaRisultati):
    numero = codaLavori.get()
    codaRisultati.put((numero, numero * numero))
    codaLavori.task_done()

if __name__ == '__main__':
    codaLavori = JoinableQueue()
    codaRisultati = Queue()
    numeri = [1, 2, 3, 4]

    create_processes(codaLavori, codaRisultati, 4)
    add_jobs(codaLavori, numeri)

    try:
        codaLavori.join()
    except KeyboardInterrupt:
        print('Keyobard interrupt')

    while not codaRisultati.empty():
        numero, quadrato = codaRisultati.get_nowait()
        print(numero, "^2 = ", quadrato, sep='')

    print('FINITO')