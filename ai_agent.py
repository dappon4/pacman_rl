from ghosts import Ghost, Blinky, Pinky, Inky, Clyde
from pacman import Pacman
from game import PacmanGame
from model import QTrainer, Linear_QNet
from collections import deque
import random
import pygame
import torch
import numpy as np

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class PacmanAI(Pacman):
    def __init__(self) -> None:
        super().__init__()
        self.memory = deque(maxlen = MAX_MEMORY)
        self.game = PacmanGame()
        
    def get_state(self):
        """
        normalized pacman x,
        normalized pacman y,
        normalized blinky x relative to pacman,
        normalized blinky y relative to pacman,
        normalized pinky x relative to pacman,
        normalized pinky y relative to pacman,
        normalized inky x relative to pacman,
        normalized inky y relative to pacman,
        normalized clyde x relative to pacman,
        normalized clyde y relative to pacman,
        pacman is powerd up,
        blinky is eaten,
        pinky is eaten,
        inky is eaten,
        clyde is eaten,
        """
    
    