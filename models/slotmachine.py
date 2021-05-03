from random import random


class SlotMachine:
    def __init__(self, money: float=1e6, fee: float=1, p: float=0.09, pay_out: float=10):
        self._money = money
        self._fee = fee
        self._p = p
        self._pay_out = pay_out

    def pull(self, gambler_credit: float) -> (float, bool):
        if gambler_credit < self._fee:
            return gambler_credit, False
        
        self._money += self._fee
        gambler_credit -= self._fee

        if random() < self._p:
            gambler_credit += 10

        return gambler_credit, True
