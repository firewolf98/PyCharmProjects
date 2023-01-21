import collections


class Counter:
    def __init__(self,*names):
        self.anonymous= not bool(names)
        if self.anonymous:
            self.count=0
        else:
            for name in names:
                if not name.isidentifier():
                    raise ValueError("names must be valid identifiers")
                setattr(self,name,0)

    def __call__(self,event):
        if self.anonymous:
            self.count+=event.count
        else:
            count=getattr(self,event.name)
            setattr(self,event.name,count+event.count)

class Event:
    def __init__(self,name,count=1):
        if not name.isidentifier():
            raise ValueError("names must be valid identifiers")
        self.name=name
        self.count=count

class Multiplexer:
    ACTIVE,DORMANT=("ACTIVE","DORMANT")
    def __init__(self):
        self.callbacksForEvent=collections.defaultdict(list)
        self.state=Multiplexer.ACTIVE

    def connect(self,eventName,callback):
        if self.state==Multiplexer.ACTIVE:
            self.callbacksForEvent[eventName].append(callback)

    def disconnect(self,event,callback=None):
        if self.state==Multiplexer.ACTIVE:
            if callback is None:
                del self.callbacksForEvent[eventName]
            else:
                self.callbacksForEvent[eventName].remove(callback)

    def send(self,event):
        if self.state==Multiplexer.ACTIVE:
            for callback in self.callbacksForEvent.get(event.name,()):
                callback(event)


totalCounter=Counter()
carCounter=Counter("cars")
commercialCounter=Counter("vans","trucks")
multiplexer=Multiplexer()

for eventName,callback in (("cars",carCounter),("vans",commercialCounter),("trucks",commercialCounter)):
    multiplexer.connect(eventName,callback)
    multiplexer.connect(eventName,totalCounter)

