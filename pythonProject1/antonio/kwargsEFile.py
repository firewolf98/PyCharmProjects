def c(**kwargs):
    print(kwargs)
    file = open(kwargs.get("file"), "w")
    file.write("ciao")
    file.close()
    f = open("aaa", "r")
    print(f.readline())

d = {"ciao":"aaa", "aaaa":"qwqw"}

c(d)