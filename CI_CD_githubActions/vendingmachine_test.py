from vendingmachine import VendingMachine, Jus, DataCola, noFreeSpaceInVendingMachine
import pytest

jus1 = Jus(1000)

@pytest.fixture
def datacola1():
    return(DataCola('can'))
datacola1 = DataCola('can')

# I: Test drink expiration
def test_drinkExpiration():
    days = datacola1.daysBeforeExpiration
    datacola1.addNewDay()
    assert(datacola1.daysBeforeExpiration) == days - 1

# Create and fill in vendingmachine 100% with drinks (10 places for drinks)
vendingmachine1 = VendingMachine()
for nDrinks in range(5):
    vendingmachine1.addDrink(Jus(1000))
    vendingmachine1.addDrink(DataCola('can'))

# II: UNIT testing of the exception (no more place for drinks in vendingmachine)
def test_freeSpaceForDrinks():
    with pytest.raises(noFreeSpaceInVendingMachine):
        vendingmachine1.addDrink(Jus(1000))

# III: Check if all expired in 20 days drinks are removed
def test_removeExpiredDrinks():
    for i in range (20):
        for j in range( vendingmachine1.numberOfDrinksInside ):
            vendingmachine1.contentOfVendingMachine[j].addNewDay()
    vendingmachine1.autoRemoveExpiredDrinks()
    assert(vendingmachine1.numberOfDrinksInside) == 5
