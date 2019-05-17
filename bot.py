from random import shuffle
from random import choice


class Bot:
    def __init__(self):
        self.thrown = []
        self.player_thrown = []

    def throw_hand(self):
        return self._random_choice()

    def _random_choice(self):
        choices = []

        for i in range(4):
            choices.append("paper")
            choices.append("rock")
            choices.append("scissors")

        for i in range(10):
            shuffle(choices)

        x = choice(choices)
        self.thrown.append(x)

        print(f"{x[0:1].upper()}-", end='', flush=True)
        return x
