from agent import Agent
import random

class Ghost(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.last_move = [0,0,0,0]
        self.last_legal_moves = [0, 0, 0, 0]
    

    def get_frightened_move(self, legal_moves):
        pass

    def get_random_moves(self, legal_moves):
        if legal_moves == self.last_legal_moves:
            return self.last_move
        
        move = [0, 0, 0, 0]
        legal_idx = [i for i, val in enumerate(legal_moves) if val == 1]
        move_idx = random.choice(legal_idx)
        
        move[move_idx] = 1
        self.last_move = move
        self.last_legal_moves = legal_moves
        return move
 
class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
    
    def get_move(self, legal_moves,pacman):
        if legal_moves == self.last_legal_moves:
            return self.last_move
        
        legal_idx = [i for i, val in enumerate(legal_moves) if val == 1]
        min_dist = 10000
        move = [0,0,0,0]
        for i in legal_idx:
            # up, right, down, left   
            if i == 0:
                if abs(self.y - 1 - pacman.y) + abs(self.x - pacman.x) < min_dist:
                    min_dist = abs(self.y - 1 - pacman.y) + abs(self.x - pacman.x)
                    move = [1,0,0,0]
            elif i == 1:
                if abs(self.y - pacman.y) + abs(self.x + 1 - pacman.x) < min_dist:
                    min_dist = abs(self.y - pacman.y) + abs(self.x + 1 - pacman.x)
                    move = [0,1,0,0]
            elif i == 2:
                if abs(self.y + 1 - pacman.y) + abs(self.x - pacman.x) < min_dist:
                    min_dist = abs(self.y + 1 - pacman.y) + abs(self.x - pacman.x)
                    move = [0,0,1,0]
            elif i == 3:
                if abs(self.y - pacman.y) + abs(self.x - 1 - pacman.x) < min_dist:
                    min_dist = abs(self.y - pacman.y) + abs(self.x - 1 - pacman.x)
                    move = [0,0,0,1]
        self.last_move = move
        self.last_legal_moves = legal_moves
        return move

class Pinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.last_legal_moves = [0, 0, 0, 0]
    
    def get_move(self, legal_moves,pacman):
        if legal_moves == self.last_legal_moves:
            return self.last_move
        if abs(self.x - pacman.x) + abs(self.y - pacman.y) > 8:
            return self.get_random_moves(legal_moves)
        legal_idx = [i for i, val in enumerate(legal_moves) if val == 1]
        min_dist = 10000
        move = [0,0,0,0]
        for i in legal_idx:
            # up, right, down, left   
            if i == 0:
                if abs(self.y - 4 - pacman.y) + abs(self.x - pacman.x) < min_dist:
                    min_dist = abs(self.y - 4 - pacman.y) + abs(self.x - pacman.x)
                    move = [1,0,0,0]
            elif i == 1:
                if abs(self.y - pacman.y) + abs(self.x + 4 - pacman.x) < min_dist:
                    min_dist = abs(self.y - pacman.y) + abs(self.x + 4 - pacman.x)
                    move = [0,1,0,0]
            elif i == 2:
                if abs(self.y + 4 - pacman.y) + abs(self.x - pacman.x) < min_dist:
                    min_dist = abs(self.y + 4 - pacman.y) + abs(self.x - pacman.x)
                    move = [0,0,1,0]
            elif i == 3:
                if abs(self.y - pacman.y) + abs(self.x - 4 - pacman.x) < min_dist:
                    min_dist = abs(self.y - pacman.y) + abs(self.x - 4 - pacman.x)
                    move = [0,0,0,1]
        self.last_move = move
        self.last_legal_moves = legal_moves
        return move