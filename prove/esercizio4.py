import concurrent.futures

def creaIFile(filesTo,filesFrom,concurrency):
    futures = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executors:
        for fname1, fname2 in zip(filesTo,filesFrom):
            future=executors.submit(scriviFile,fname1,fname2)
            futures.add(future)
    for future in concurrent.futures.as_completed(futures):
        fileName,n=future.result()
        print("Il numero di caratteri del file {} è {}".format(fileName,n))



def scriviFile(fname1,fname2):
    f1=open(fname1,"w")
    f2=open(fname2,"r")
    nChar=0
    i=1
    try:
        while True:
            line=f2.readline()
            if not line:
                break
            elif i%2==1:
                f1.write(line)
                nChar=nChar+len(line)
            i=i+1
    except Exception as e:
        print(e)
        f1.close()
        f2.close()
    return (fname1,nChar)