import functools

def coroutine(funct):
    @functools.wraps(funct)
    def wrapper(*args, **kwd):
        gen=funct(*args, **kwd)
        next(gen)
        return gen
    return wrapper

@coroutine
def attacca(suffisso, myFile):
    while True:
        stringa=yield
        if stringa:
            if stringa[len(stringa)-len(suffisso): len(stringa)]==suffisso:
                return
            else:
                stringa=stringa+suffisso
                with open(myFile, 'a') as f:
                    print("Scrivo sul file {} la stringa {}".format(myFile,stringa))
                    f.write("\n"+stringa)

def i_o(myFile, suffisso):
    att=attacca(suffisso,myFile)
    f=open(myFile, 'r')
    text=f.read()
    for word in text.split():
        try:
            att.send(word)
        except StopIteration:
            print("La coroutine ha smesso di ricevere parole")
            return


def main():
    print("Invochiamo la funzione i_o")
    i_o("File","ssimi")

if __name__=='__main__':
    main()




     
    
       
        
        
                
        
