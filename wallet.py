class Alarm_no_money(Exception):
    pass

class Wallet(object):
    def __init__(self, money=0):
        self.money = money
    def add_money(self, money):
        self.money = self.money + money
    def spend_money(self, money):
        if (money>self.money):
            raise Alarm_no_money("No way to spend {}$, we do not have it!".format(money))
        self.money = self.money - money
    