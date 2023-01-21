class provaself():
    a=3
    def method(self):
        self.a=4



x=provaself()
print(x.a)
x.method()
print(x.a)
y=provaself()
print(y.a)
print(provaself.a)
