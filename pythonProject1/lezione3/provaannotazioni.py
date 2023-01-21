def func(nome: str,user:"username",età:int=23)->str:
    print("ciao",nome,"hai",età,"anni")
    return nome+""+str(età)


func("Luca","FireWolf")
print(func.__annotations__)