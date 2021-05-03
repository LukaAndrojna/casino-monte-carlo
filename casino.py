import pandas as pd
import matplotlib.pyplot as plt

from models.gambler import Gambler
from models.slotmachine import SlotMachine


def simulation(gamblers: int, credit: float, pulls: int):
    slot_machine = SlotMachine()
    gamblers_list = [Gambler(slot_machine=slot_machine, credit=credit, pulls=pulls) for _ in range(gamblers)]

    simulation_map = {f'gambler_{i}': gamblers_list[i].simulate() for i in range(gamblers)}
    df = pd.DataFrame(simulation_map)

    plt.plot(df, alpha=0.5)
    plt.show()

def main():
    gamblers = 1000
    credit = 100
    pulls = 1000

    simulation(
        gamblers=gamblers,
        credit=credit,
        pulls=pulls
    )

if __name__ == '__main__':
    main()