import random
import pygame
from agent import Agent
class Pacman(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 13
        self.y = 22
        self.spawn_x = self.x
        self.spawn_y = self.y
        self.powerup_duration = 0