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

    def get_scatter_moves(self, legal_moves):
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
        else:
            return self.get_chase_moves(legal_moves, pacman)
        
    def get_chase_moves(self, legal_moves, pacman):
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
        elif abs(self.x - pacman.x) + abs(self.y - pacman.y) > 8:
            return self.get_scatter_moves(legal_moves)
        else:
            return self.get_chase_moves(legal_moves, pacman)
        
    
    def get_chase_moves(self, legal_moves, pacman):
        legal_idx = [i for i, val in enumerate(legal_moves) if val == 1]
        min_dist = 10000
        move = [0,0,0,0]
        target_x = pacman.x
        target_y = pacman.y
        
        if pacman.last_move[0] == 1:
            target_y -= 4
        elif pacman.last_move[1] == 1:
            target_x += 4
        elif pacman.last_move[2] == 1:
            target_y += 4
        elif pacman.last_move[3] == 1:
            target_x -= 4
            
        for i in legal_idx:
            # up, right, down, left   
            if i == 0:
                if abs(self.y - 4 - target_y) + abs(self.x - target_x) < min_dist:
                    min_dist = abs(self.y - 4 - target_y) + abs(self.x - target_x)
                    move = [1,0,0,0]
            elif i == 1:
                if abs(self.y - target_y) + abs(self.x + 4 - target_x) < min_dist:
                    min_dist = abs(self.y - target_y) + abs(self.x + 4 - target_x)
                    move = [0,1,0,0]
            elif i == 2:
                if abs(self.y + 4 - target_y) + abs(self.x - target_x) < min_dist:
                    min_dist = abs(self.y + 4 - target_y) + abs(self.x - target_x)
                    move = [0,0,1,0]
            elif i == 3:
                if abs(self.y - target_y) + abs(self.x - 4 - target_x) < min_dist:
                    min_dist = abs(self.y - target_y) + abs(self.x - 4 - target_x)
                    move = [0,0,0,1]
        self.last_move = move
        self.last_legal_moves = legal_moves
        return move