import random
from agent import Agent

class Pacman(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 280
        self.y = 260