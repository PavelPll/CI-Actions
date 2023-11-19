from wallet import Wallet, Alarm_no_money
import pytest

# Define the specific wallet with 100$ inside
@pytest.fixture
def walletS():
    return(Wallet(100))

#UNIT testing of the specific wallet
def test_walletS(walletS):
    walletS.add_money(50)
    walletS.spend_money(150)
    assert(walletS.money) == 0 

# UNIT testing of the exception (spend more money than we have)
def test_exception(walletS):
    walletS.add_money(50)
    with pytest.raises(Alarm_no_money):
        walletS.spend_money(100+50+1)