#Scrivere la funzione ricorsiva myDeepCopy che prende in input una lista
#che potrebbe contenere al suo interno elementi di tipo lista che a loro
#volta potrebbero contenere elementi di tipo lista, e cosi` via. La funzione
#restituisce la deep copy della lista (no, non si puo` usare copy.deepcopy).

def myDeepCopy(lis):
    print(lis)
    lst = [myDeepCopy(l) if isinstance(l, list) else l for l in lis]
    return lst


print(myDeepCopy([1, 2, [3, [4]]]))
