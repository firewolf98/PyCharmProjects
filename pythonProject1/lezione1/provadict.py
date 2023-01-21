def funz():
    d={"it":"Italia","ch":"Svizzera"}
    print(d)
    s=[("it","Italia"),("ch","Svizzera")]
    d1=dict(s)
    print(d1)
    d1["de"]="Germania"
    print(d1)
    print(d1.keys())
    print(d1.values())
    print(d1.items())
    d.clear()
    print(d)
    print(d1.get("it"))
    print(d1.pop("de"))
    print(d1)
    d1["de"]="Inghilterra"
    print(d1)
    d2={"de":"Germania"}
    d1.update(d2)
    print(d1)

funz()