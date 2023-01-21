def func(a, b, c, **op):
    if (op.get("operazione") == "+"):
        print(a + b + c)
    elif (op.get("operazione")=="*"):
        print(a * b * c)
    else:
        print("operazione non valida")


func(1, 2, 3, operazione="+")
func(1, 2, 3, operazione="*")
func(1, 2, 3, operazione="/")
