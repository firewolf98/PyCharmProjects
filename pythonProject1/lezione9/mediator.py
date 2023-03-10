import collections


class Form:
    def __init__(self):
        self.create_widgets()
        self.create_mediator()

    def create_widgets(self):
        self.nameText=Text()
        self.emailText=Text()
        self.okButton=Button("OK")
        self.cancelButton=Button("Cancel")

    def create_mediator(self):
        self.mediator=Mediator(((self.nameText,self.update_ui),(self.emailText,self.update_ui),(self.okButton,self.clicked),(self.cancelButton,self.clicked)))
        self.update_ui()

    def update_ui(self,widget=None):
        self.okButton.enabled=(bool(self.nameText.text) and bool(self.emailText.text))

    def clicked(self,widget):
        if widget==self.okButton:
            print("OK")
        elif widget==self.cancelButton:
            print("Cancel")

class Mediator:
    def __init__(self,widgetCallablePairs):
        self.callablesForWidget=collections.defaultdict(list)
        for widget,caller in widgetCallablePairs:
            self.callablesForWidget[widget].append(caller)
            widget.mediator=self

    def on_change(self,widget):
        callables=self.callablesForWidget.get(widget)
        if callables is not None:
            for caller in callables:
                caller(widget)
        else:
            raise AttributeError("No on_change() methos registered for {}".format(widget))

class Mediated:
    def __init__(self):
        self.mediator=None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)

class Button(Mediated):
    def __init__(self,text=""):
        super.__init__()
        self.enabled=True
        self.text=text

    def click(self):
        if self.enabled:
            self.on_change()

class Text(Mediated):
    def __init__(self,text=""):
        super.__init__()
        self.__text=text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self,text):
        if self.text!=text:
            self.__text=text
            self.on_change()

def main():
    form=Form()
    test_user_interaction_with(form)

def test_user_interaction_with(form):
    form.okButton.click()
    print(form.okButton.enabled)
    form.nameText.text="Fred"
    print(form.okButton.enabled)
    form.emailText.text="fred@bloggers.com"
    print(form.okButton.enabled)
    form.okButton.click()
    form.emailText.text=""
    print(form.okButton.enabled)
    form.cancelButton.click()

if __name__=="__main__":
    main()
