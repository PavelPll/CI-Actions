from vendingmachine import VendingMachine, Jus, DataCola, noFreeSpaceInVendingMachine
import pytest

# Initialize two drink instances jus1 and datacola1
jus1 = Jus(1000)
@pytest.fixture
def datacola1():
    return(DataCola('can'))
datacola1 = DataCola('can')

# I: Test drink expiration for datacola1
def test_drinkExpiration():
    days_left = datacola1.daysBeforeExpiration
    datacola1.addNewDay()
    assert(datacola1.daysBeforeExpiration) == days_left - 1

# Create vendingmachine and fill it in with drinks (add 10 drinks to 10 places for drinks)
vendingmachine1 = VendingMachine()
for nDrinks in range(5):
    vendingmachine1.addDrink(Jus(1000))
    vendingmachine1.addDrink(DataCola('can'))

# II: UNIT testing of the exception (no more place for drinks in vendingmachine)
def test_freeSpaceForDrinks():
    with pytest.raises(noFreeSpaceInVendingMachine):
        vendingmachine1.addDrink(Jus(1000))

# III: Check if all drinks out of 10, expired in a certain number of days, are removed
@pytest.mark.parametrize("days,NOTremoved",[(1,10),(8,5),(61,0)])
# Jus(1000) expired after 7 days
# DataCola('can') expired after 60 days
def test_removeExpiredDrinks(days, NOTremoved):
    vendingmachine2 = VendingMachine()
    # add 10 drinks to vendingmachine
    for nDrinks in range(5):
        vendingmachine2.addDrink(Jus(1000)) # expired after 7 days
        vendingmachine2.addDrink(DataCola('can')) # expired after 60 days
    # wait for days=days days
    for i in range (days):
        for j in range( vendingmachine1.numberOfDrinksInside ):
            vendingmachine2.contentOfVendingMachine[j].addNewDay()
    # remove expired drinks
    vendingmachine2.autoRemoveExpiredDrinks()
    # check whether all expired drinks are removed
    assert(vendingmachine2.numberOfDrinksInside) == NOTremoved
