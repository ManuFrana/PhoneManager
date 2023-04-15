
from Phone import Phone
from ResultsManager import ResultsManager
from SmartPhone import SmartPhone

class Menu:

    def showMenu(self):
        opt = self.getOption()
        while opt >= 6 or opt <= 0:
            opt = self.getOption()

        if opt == 1:
            phone = self.firstOption()
            self.shouldSavePhone(phone)
        elif opt == 2:
            self.secondOption()
        elif opt == 3:
            self.thirdOption()
        elif opt == 4:
            self.forthOption()
        elif opt == 5:
            print("\nByeee :(")
            exit(1)
        self.showMenu()


    def getOption(self):
        print('\nPhone registration December Labs')
        print("1 - Register new phone.")
        print("2 - Show all phones.")
        print("3 - Show only smartphones.")
        print("4 - Delete all smartphones saved.")
        print("5 - Exit.")
        opt = input("Please select your option: ")
        if not opt.isnumeric():
            print('\nOpps, wrong answer...')
            return -1
        return int(opt)

    def firstOption(self):
        color = str(input("\nPlease enter the color of the phone: "))
        model = str(input("Please enter the model of the phone: "))
        brand = str(input("Please enter the brand of the phone: "))
        isSmart = str(input("Does the phone have an S.O? [yY/nN]: "))
        if isSmart.lower() == 'y':
            so = str(input("Please enter the Operating System of the phone: "))
            memory = str(input("Please enter the memory size of the phone: "))
            smart = SmartPhone(color, model, brand, so, memory)
            return smart
        else:
            phone = Phone(color, model, brand)
            return phone

    def secondOption(self):
        ResultsManager().showAll()

    def thirdOption(self):
        ResultsManager().showOnlySmartPhones()

    def forthOption(self):
        opt = str(input('WARNING - Are you sure you want to delete all phones? There is no going back from this.. [yY/nN]: '))
        if opt.lower() == 'y':
            ResultsManager().deleteAll()
        else:
            print("\nPHEW, that was a closed one!")

    def shouldSavePhone(self, phone):
        print("\nThis is the phone you entered:\n")
        print(phone.show())
        print('\n')
        opt = str(
            input('QUESTION - Do you wish to save this phone in our records? [yY/nN]: '))
        if opt.lower() == 'y':
            phone.savePhone()
        else:
            print("\nOkay, discarding phone...")
