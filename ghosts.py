from agent import Agent
import random

class Ghost(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.x = 13
        self.y = 12
        self.last_legal_moves = [0, 0, 0, 0]
        self.switch_dir = False
    
    def get_opposite_move(self, move):
        map_counter_movement = {0:2,1:3,2:0,3:1}
        idx = map_counter_movement[move.index(1)]
        new_move = [0,0,0,0]
        new_move[idx] = 1
        return new_move
    
    def get_frightened_move(self, legal_moves):
        return self.get_scatter_moves(legal_moves)

    def get_scatter_moves(self, legal_moves):
        if legal_moves == self.last_legal_moves:
            return self.last_move
        
        move = [0, 0, 0, 0]
        legal_idx = [i for i, val in enumerate(legal_moves) if val == 1]
        move_idx = random.choice(legal_idx)
        
        move[move_idx] = 1
        self.last_legal_moves = legal_moves
        return move

    def get_chase_moves(self, legal_moves, target_x, target_y):
        legal_idx = [i for i, val in enumerate(legal_moves) if val == 1]
        min_dist = 10000
        move = [0,0,0,0]
        
        for i in legal_idx:
            # up, right, down, left   
            if i == 0:
                if abs(self.y - 1 - target_y) + abs(self.x - target_x) < min_dist:
                    min_dist = abs(self.y - 1 - target_y) + abs(self.x - target_x)
                    move = [1,0,0,0]
            elif i == 1:
                if abs(self.y - target_y) + abs(self.x + 1 - target_x) < min_dist:
                    min_dist = abs(self.y - target_y) + abs(self.x + 1 - target_x)
                    move = [0,1,0,0]
            elif i == 2:
                if abs(self.y + 1 - target_y) + abs(self.x - target_x) < min_dist:
                    min_dist = abs(self.y + 1 - target_y) + abs(self.x - target_x)
                    move = [0,0,1,0]
            elif i == 3:
                if abs(self.y - target_y) + abs(self.x - 1 - target_x) < min_dist:
                    min_dist = abs(self.y - target_y) + abs(self.x - 1 - target_x)
                    move = [0,0,0,1]

        self.last_legal_moves = legal_moves
        return move

    
 
class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 13
        self.y = 12
        self.spawn_x = self.x
        self.spawn_y = self.y
    
    def get_move(self, legal_moves,pacman):
        if self.switch_dir:
            self.switch_dir = False
            return self.get_opposite_move(self.last_move)
        elif pacman.powerup_duration > 0:
            return self.get_frightened_move(legal_moves)
        elif legal_moves == self.last_legal_moves:
            return self.last_move
        else:
            return self.get_chase_moves(legal_moves, pacman.x, pacman.y)


class Pinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 14
        self.y = 12
        self.spawn_x = self.x
        self.spawn_y = self.y
    
    def get_move(self, legal_moves,pacman):
        if self.switch_dir:
            self.switch_dir = False
            return self.get_opposite_move(self.last_move)
        elif pacman.powerup_duration > 0:
            return self.get_frightened_move(legal_moves)
        elif legal_moves == self.last_legal_moves:
            return self.last_move
        elif abs(self.x - pacman.x) + abs(self.y - pacman.y) > 8:
            return self.get_scatter_moves(legal_moves)
        else:
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
            return self.get_chase_moves(legal_moves, target_x, target_y)

class Clyde(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 13
        self.y = 13
        self.spawn_x = self.x
        self.spawn_y = self.y
    
    def get_move(self, legal_moves,pacman):
        if self.switch_dir:
            self.switch_dir = False
            return self.get_opposite_move(self.last_move)
        elif pacman.powerup_duration > 0:
            return self.get_frightened_move(legal_moves)
        elif legal_moves == self.last_legal_moves:
            return self.last_move
        elif abs(self.x - pacman.x) + abs(self.y - pacman.y) > 8:
            return self.get_scatter_moves(legal_moves)
        else:
            return self.get_chase_moves(legal_moves, pacman.x, pacman.y)

class Inky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.x = 14
        self.y = 13
        self.spawn_x = self.x
        self.spawn_y = self.y
        self.frames_elapsed = 0
        self.curr_agent = None
    
    def get_move(self, legal_moves,pacman):
        
        if self.frames_elapsed == 0:
            self.curr_agent = random.choice([Blinky(), Pinky(), Clyde()])
        
        self.curr_agent.x = self.x
        self.curr_agent.y = self.y
        self.curr_agent.last_move = self.last_move
        self.curr_agent.last_legal_moves = self.last_legal_moves
        self.curr_agent.switch_dir = self.switch_dir
        self.frames_elapsed = (self.frames_elapsed + 1) % 50
        
        move = self.curr_agent.get_move(legal_moves, pacman)
        self.switch_dir = self.curr_agent.switch_dir
        return move