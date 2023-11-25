import numpy as np
from vendingmachine import Jus, DataCola, VendingMachine
from tqdm import tqdm
from time import sleep

print("==============================================================")
print("= Set the max allowed number of drinks in the VendingMachine =")
print("=            to get some usefull info                        =")
print("==============================================================")
print("")
message = "Please set the max allowed number of drinks: "
maxAllowedNumberOfDrinksInside = int(input(message))
vendingmachine1 = VendingMachine(maxAllowedNumberOfDrinksInside)

# add 10 drinks to vendingmachine
print("Filling the vendingmachine ...")
for nDrinks in tqdm(range(maxAllowedNumberOfDrinksInside)):
    rnd1 = np.random.randint(2, size=1)
    sleep(0.01)
    if rnd1 == 0:
        # expired after 7 days
        vendingmachine1.addDrink(Jus(800))
    else:
        rnd2 = np.random.randint(2, size=1)
        if rnd2 == 0:
            # expired after 60 days
            vendingmachine1.addDrink(DataCola('can'))
        else:
            # expired after 30 days
            vendingmachine1.addDrink(DataCola('bottle'))
print(maxAllowedNumberOfDrinksInside, " different drinks are loaded")
print("")

# see time evolution
for days in range(100):
    if days % 20 == 0:
        # get total volume of drinks
        totalVolume = vendingmachine1.getTotalVolume()
        print("After {} days the total mass of not expired drinks is {} kg".format(days, totalVolume/100))
    vendingmachine1.addNewDay()
    # remove expired drinks
    vendingmachine1.autoRemoveExpiredDrinks()
print("-----the END-----")
