def concat(*args,sep):
    return sep.join(args)

print(concat("ciao","a","tutti",sep="/"))
print(concat("ciao","a","tutti",sep="."))