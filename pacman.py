import random

class Pacman:
    def __init__(self) -> None:
        self.x = 0
        self.y = 10
        self.prev_x = self.x
        self.prev_y = self.y
    
    def get_move(self, legal_moves):
        move = [0, 0, 0, 0]
        indices_with_1 = [i for i, val in enumerate(legal_moves) if val == 1]
        random_index = random.choice(indices_with_1)
        move[random_index] = 1
        return move