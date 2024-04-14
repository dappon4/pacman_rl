import random
import pygame
from agent import Agent
class Pacman(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 13
        self.y = 22
        self.powerup_duration = 0
        self.next_move = [0, 1, 0, 0]
    
    def get_move(self, legal_moves):
        return self.get_player_move(legal_moves)
    
    def get_player_move(self, legal_moves):
        move = [0, 0, 0, 0]
        idx = self.next_move.index(1)
        if legal_moves[idx] != 1:
            idx = self.last_move.index(1)
            if legal_moves[idx] != 1:
                map_counter_movement = {0:2,1:3,2:0,3:1}
                last_idx = self.last_move.index(1)
                legal_moves[map_counter_movement[last_idx]] = 0
            
                idx = random.choice([i for i, val in enumerate(legal_moves) if val == 1])
                move[idx] = 1
                return move
            else:
                return self.last_move
        else:
            return self.next_move