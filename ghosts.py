from agent import Agent

class Ghost(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.last_legal_moves = [0, 0, 0, 0]
    

    def get_frightened_move(self, legal_moves):
        pass
 
class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.last_legal_moves = [0, 0, 0, 0]
    
    def get_move(self, legal_moves,pacman):
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
            
        return move