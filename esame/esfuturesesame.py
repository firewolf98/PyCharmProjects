import concurrent.futures

def creaIFile(filesTo,filesFrom,concurrency):
    futures=set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executors:
        for fname1,fname2 in zip(filesTo,filesFrom):
            future=executors.submit(scriviFile,fname1,fname2)
            futures.add(future)
    for future in concurrent.futures.as_completed(futures):
        fileName,n=future.result()
        print("Il numero di caratteri nel file {} è {}".format(fileName,n))

def scriviFile(fname1,fname2):
    f1=open(fname1,'w')
    f2=open(fname2,'r')
    nChar=0
    i=i+1
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
    return(fname1,nChar)

def main():


    filesTo =['CopiaFile1' ,'CopiaFile2' ,'CopiaFile3' ,'CopiaFile4' ,'CopiaFile5']
    filesFrom =['file1' ,'file2' ,'file3' ,'file4' ,'file5']



    creaIFile(filesTo, filesFrom ,2)





if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):

Il numero di caratteri scritti nel file CopiaFile1 e` 6056
Il numero di caratteri scritti nel file CopiaFile3 e` 70
Il numero di caratteri scritti nel file CopiaFile4 e` 48
Il numero di caratteri scritti nel file CopiaFile5 e` 158
Il numero di caratteri scritti nel file CopiaFile2 e` 4741
"""