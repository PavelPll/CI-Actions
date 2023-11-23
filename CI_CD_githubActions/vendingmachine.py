class noFreeSpaceInVendingMachine(Exception):
    pass

class Drink:
    def __init__(self, volume, daysBeforeExpiration):
        self.volume = volume
        self.daysBeforeExpiration = daysBeforeExpiration
    def addNewDay(self):
        self.daysBeforeExpiration = self.daysBeforeExpiration - 1


# +
class Jus(Drink):
    def __init__(self, volume):
        self.daysBeforeExpiration = 7

class DataCola(Drink):
    def __init__(self, beverageContainerType):
        self.beverageContainerType = beverageContainerType
        if (self.beverageContainerType == 'can'): 
            self.volume = 330
            self.daysBeforeExpiration = 60
        if (self.beverageContainerType == 'bottle'): 
            self.volume = 500
            self.daysBeforeExpiration = 30






class VendingMachine(Drink):
    def __init__(self):
        self.contentOfVendingMachine = []
        self.numberOfDrinksInside = 0
        self.maxAllowedNumberOfDrinksInside = 10
    def addDrink(self, Drink):
        if (self.numberOfDrinksInside<self.maxAllowedNumberOfDrinksInside):
            self.contentOfVendingMachine.append(Drink)
            self.numberOfDrinksInside = self.numberOfDrinksInside + 1
        else:
            raise noFreeSpaceInVendingMachine("All {} places for drinks are occupied!".format(self.maxAllowedNumberOfDrinksInside))
    def removeOneDrink(self, i):
        self.contentOfVendingMachine.pop(i)
        self.numberOfDrinksInside = self.numberOfDrinksInside - 1
    def autoRemoveExpiredDrinks(self):
        self.contentOfVendingMachine = [drink for drink in self.contentOfVendingMachine if (drink.daysBeforeExpiration>=0)]
        self.numberOfDrinksInside = len(self.contentOfVendingMachine)
    def addNewDay(self):
        for drink in self.contentOfVendingMachine:
            drink.daysBeforeExpiration = drink.daysBeforeExpiration - 1



# All unit tests see in vendingmachine_test.py file
# This is the first try before writung unit tests in a proper way
# Not executed during import
# All unit tests see in vendingmachine_test.py file
if __name__ == "__main__":
    jus1 = Jus(1000)
    print(jus1.daysBeforeExpiration)
    jus1.addNewDay()
    print(jus1.daysBeforeExpiration)
    datacola1 = DataCola('can')
    print(datacola1.daysBeforeExpiration)

    d1 = VendingMachine()
    d1.addDrink(jus1)
    d1.addDrink(datacola1)
    print(d1.numberOfDrinksInside)
    for i in range (20):
        d1.contentOfVendingMachine[0].addNewDay()
        d1.contentOfVendingMachine[1].addNewDay()
    print(d1.numberOfDrinksInside)
    d1.autoRemoveExpiredDrinks()
    print(d1.numberOfDrinksInside)
