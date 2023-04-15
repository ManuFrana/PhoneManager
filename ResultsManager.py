import pickle

from tabulate import tabulate
from SmartPhone import SmartPhone


class ResultsManager:

    def __init__(self):
        self.fileName = 'savedPhones.pkl'

    def showAll(self):
        phones = self.getAllPhones()
        if not phones:
            print("\nSorry, there were no phones saved...")
            return
        print("\n----------Saved phones----------\n")
        columns = ['COLOR', 'MODEL', 'BRAND', 'S.O', 'MEMORY']
        rows = []
        for phone in phones:
            rows.append(phone.getAsArray())
        print(tabulate(rows, headers=columns, missingval='-', tablefmt='heavy_grid'))

    def showOnlySmartPhones(self):
        phones = self.getAllPhones()
        if not phones:
            print("\nSorry, there were no phones saved...")
            return
        print("\n----------Saved SmartPhones----------\n")
        columns = ['COLOR', 'MODEL', 'BRAND', 'S.O', 'MEMORY']
        rows = []
        for phone in phones:
            if phone.__class__ == SmartPhone:
                rows.append(phone.getAsArray())
        if not rows:
            print("\nSorry, there were no SmartPhones saved...")
            return
        print(tabulate(rows, headers=columns, missingval='-', tablefmt='heavy_grid'))

    def getAllPhones(self):
        phones = []
        try:
            with open(self.fileName, 'rb') as file:
                while True:
                    try:
                        phones.append(pickle.load(file))
                    except EOFError:
                        break

            file.close()
        except OSError:
            print("\nWOW, it seems that someone tried to delete our file... good thing we got it covered :)")
            return
        return phones

    def deleteAll(self):
        open(self.fileName, 'w').close()
        print("\nAll phones saved were deleted!")
