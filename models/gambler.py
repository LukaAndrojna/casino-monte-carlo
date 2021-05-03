from typing import List

from models.slotmachine import SlotMachine


class Gambler:
    def __init__(self, slot_machine: SlotMachine, credit: float=1000, pulls: int=100):
        self._slot_machine = slot_machine
        self._credit = credit
        self._pulls = pulls
        self._play = True
        self._games = list()
    
    def play(self):
        if self._play:
            self._credit, self._play = self._slot_machine.pull(self._credit)
        self._games.append(self._credit)
    
    def simulate(self) -> List:
        for _ in range(self._pulls):
            self.play()
        return self._games
