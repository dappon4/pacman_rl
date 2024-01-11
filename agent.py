import random

class Agent:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.last_move = [1,0,0,0]
        self.prev_x = 0
        self.prev_y = 0
    
    def get_move(self, legal_moves):
        move = [0, 0, 0, 0]
        indices_with_1 = [i for i, val in enumerate(legal_moves) if val == 1]
        random_index = random.choice(indices_with_1)
        move[random_index] = 1
        
        self.last_move = move
        return move