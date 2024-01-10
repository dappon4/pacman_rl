class Pacman:
    def __init__(self) -> None:
        self.x = 13
        self.y = 16
        self.prev_x = self.x
        self.prev_y = self.y
    
    def get_move(self,legal_moves):
        move = [0,0,0,0]
        first_idx = legal_moves.index(1)
        move[first_idx] = 1
        
        return move
    
    def move(self,legal_moves):
        self.prev_x = self.x
        self.prev_y = self.y
        # up, right, down, left
        move = self.get_move(legal_moves)
        if move == [1,0,0,0]:
            self.y -= 1
        elif move == [0,1,0,0]:
            self.x += 1
        elif move == [0,0,1,0]:
            self.y += 1
        elif move == [0,0,0,1]:
            self.x -= 1