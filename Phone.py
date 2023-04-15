import pickle

class Phone:

    def __init__(self, color, model, brand):
        self.color = color
        self.model = model
        self.brand = brand

    def show(self):
        text = "COLOR: " + self.color
        text += "\nMODEL: " + self.model
        text += "\nBRAND: " + self.brand
        return text

    def savePhone(self):
        fileName = 'savedPhones.pkl'
        with open(fileName, 'ab') as file:
            pickle.dump(self, file)
            print("\nPhone successfully saved to our records :)")

    def getAsArray(self):
        return [self.color, self.model, self.brand]

