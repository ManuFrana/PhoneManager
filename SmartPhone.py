from Phone import Phone


class SmartPhone(Phone):

    def __init__(self, color, model, brand, so, memory):
        super().__init__(color, model, brand)
        self.so = so
        self.memory = memory

    def show(self):
        text = super().show()
        text += "\nS.O: " + self.so
        text += "\nMEMORY: " + self.memory
        return text

    def getAsArray(self):
        row = super().getAsArray()
        row.append(self.so)
        row.append(self.memory)
        return row