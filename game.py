import pygame
import time
from agent import Agent
from ghosts import Ghost, Blinky, Pinky, Clyde, Inky
from pacman import Pacman

BOARD =[
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 3, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
 [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 3, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

COOKIES = [
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 3, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
 [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 3, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

COOKIES_SET_TEST = {(1,1)}

COOKIES_SET = set([(i,j) for j in range(len(COOKIES)) for i in range(len(COOKIES[0])) if COOKIES[j][i] == 0])
POWERUPS_SET = set([(i,j) for j in range(len(BOARD)) for i in range(len(BOARD[0])) if BOARD[j][i] == 3])
#1: wall
#0: cookie
#2: ghost spawn
#3: power up

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20

GAME_SPEED = 10
POWERUP_DURATION = 50


class PacmanGame:
    def __init__(self, winndows_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT):
        self.board = BOARD
        self.cookies = COOKIES_SET
        self.powerups = POWERUPS_SET
        self.width = winndows_width
        self.height = window_height
        self.score = 0
        self.clock = pygame.time.Clock()
        self.pacman = Pacman()
        self.blinky = Blinky()
        self.pinky = Pinky()
        self.clyde = Clyde()
        self.inky = Inky()
        
        self.ghosts = [self.blinky, self.pinky,self.clyde,self.inky]
        self.ghost_colors = [(255,0,0),(255,0,180),(255,165,0),(173,216,230)]
        
    def reset(self):
        self.score = 0
        self.board = BOARD
        self.cookies = COOKIES_SET
        self.powerups = POWERUPS_SET
    
    def get_legal_moves(self,agent):
        moves = [1,1,1,1] # up, right, down, left
        
        # if agent is in between two blocks
        if agent.x % 1 == 0.5 or agent.y % 1 == 0.5:
            return agent.last_move
        else:
            agent.x = int(agent.x)
            agent.y = int(agent.y)
        
        # check if agent is in a cell 
        assert type(agent.x) == int and type(agent.y) == int
        
        # check if agent is in the spawn area of ghosts
        if self.board[agent.y][agent.x] == 2:
            return [1,0,0,0]
        
        # if agent is not at the edge of the board
        if 0 < agent.x < len(self.board[0]) - 1:
            if self.board[agent.y][agent.x - 1] == 1:
                moves[3] = 0
            if self.board[agent.y][agent.x + 1] == 1:
                moves[1] = 0
        
        # if agent is not at the edge of the board
        if 0 < agent.y < len(self.board) - 1:
            if self.board[agent.y - 1][agent.x] == 1:
                moves[0] = 0
            if self.board[agent.y + 1][agent.x] == 1 or self.board[agent.y - 1][agent.x] == 2:
                moves[2] = 0
        
        # ghosts cannot move backwards
        if isinstance(agent,Ghost):
            last_idx = agent.last_move.index(1)
            map_counter_movement = {0:2,1:3,2:0,3:1}
            moves[map_counter_movement[last_idx]] = 0
        
        return moves
    
    def draw_misc(self,window):
        # draw cookies
        for cookie in self.cookies:
            pygame.draw.circle(window, (255, 255, 0), (cookie[0] * BLOCK_SIZE + BLOCK_SIZE // 2, cookie[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 5)
        # draw powerups
        for powerup in self.powerups:
            pygame.draw.circle(window, (255, 0, 0), (powerup[0] * BLOCK_SIZE + BLOCK_SIZE // 2, powerup[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
    
    def draw_pacman(self,window):
        # draw pacman
        pygame.draw.circle(window, (255, 255, 0), (self.pacman.x * BLOCK_SIZE + BLOCK_SIZE // 2, self.pacman.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
    
    def draw_ghosts(self,window):
        # if pacman is not powered up
        if self.pacman.powerup_duration == 0:
            for ghost, color in zip(self.ghosts,self.ghost_colors):
                pygame.draw.circle(window, color, (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        
        # if pacman is powered up
        elif self.pacman.powerup_duration > 0:
            for ghost in self.ghosts:
                pygame.draw.circle(window, (0, 0, 255), (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2) 
    
    def draw_black_rect(self,window):
        # draw black rectangle to erase previous position of pacman and ghosts
        pygame.draw.rect(window, (0, 0, 0), (self.pacman.prev_x * BLOCK_SIZE, self.pacman.prev_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for ghost in self.ghosts:
            pygame.draw.rect(window, (0, 0, 0), (ghost.prev_x * BLOCK_SIZE, ghost.prev_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    def update_window(self, window):
        self.draw_black_rect(window)
        self.draw_misc(window)
        self.draw_ghosts(window)
        self.draw_pacman(window)
        pygame.display.flip()
    
    def display_score(self,window):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (650, self.height // 2)
        window.blit(text, textRect)
    
    def move_agent(self,agent,move):
        # save previous position of agent
        agent.prev_x = agent.x
        agent.prev_y = agent.y
        
        if move == [1,0,0,0]: # up
            agent.y -= 0.5
        elif move == [0,1,0,0]: # right
            agent.x += 0.5
        elif move == [0,0,1,0]: # down
            agent.y += 0.5
        elif move == [0,0,0,1]: # left
            agent.x -= 0.5

        # if agent is at the left edge of the board
        if agent.x == -0.5:
            agent.x = len(self.board[0]) - 0.5
        # if agent is at the right edge of the board
        elif agent.x == len(self.board[0]) - 0.5:
            agent.x = 0.5
        
        agent.last_move = move
    
    def play_step(self,window):
        # move pacman
        move = self.pacman.get_move(self.get_legal_moves(self.pacman))
        self.move_agent(self.pacman,move)
        
        # if pacman is at the same position as a cookie
        if (self.pacman.x,self.pacman.y) in self.cookies:
            # remove cookie from set
            self.cookies.remove((self.pacman.x,self.pacman.y))
            
            # if all cookies are eaten end game
            if len(self.cookies) == 0:
                return True
            self.score += 10
        
        # if pacman is at the same position as a powerup
        if (self.pacman.x,self.pacman.y) in self.powerups:
            # remove powerup from set
            self.powerups.remove((self.pacman.x,self.pacman.y))
            # set timer for powerup
            self.pacman.powerup_duration = POWERUP_DURATION
            # switch direction of ghosts
            for ghost in self.ghosts:
                ghost.switch_dir = True
        
        for ghost in self.ghosts:
            move = ghost.get_move(self.get_legal_moves(ghost),self.pacman)
            self.move_agent(ghost,move)
            if (self.pacman.x,self.pacman.y) == (ghost.x,ghost.y):
                if self.pacman.powerup_duration == 0:
                    return True
                else:
                    self.score += 100
                    # TODO: reset ghost position
        
        # if pacman is powered up   
        if self.pacman.powerup_duration > 0:
            # decrease powerup duration
            self.pacman.powerup_duration -= 1
            
            # if powerup duration is over switch direction of ghosts
            if self.pacman.powerup_duration == 1:
                for ghost in self.ghosts:
                    ghost.switch_dir = True
        
        self.display_score(window)
        self.update_window(window)
        self.clock.tick(GAME_SPEED)

        return False
    
    def setup_board(self):
        # Set up the game window
        window_width = 800
        window_height = 700
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Pacman Game")
        

        for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] == 1:
                        pygame.draw.rect(window, (0, 0, 255), (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    elif self.board[row][col] == 2:
                        pygame.draw.rect(window, (255, 0, 0), (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    elif self.board[row][col] == 3:
                        pygame.draw.circle(window, (255, 0, 255), (col * BLOCK_SIZE + BLOCK_SIZE // 2, row * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 5)
        
        pygame.display.update()
        
        # Game loop
        done = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.pacman.next_move = [1,0,0,0]
                    elif event.key == pygame.K_RIGHT:
                        self.pacman.next_move = [0,1,0,0]
                    elif event.key == pygame.K_DOWN:
                        self.pacman.next_move = [0,0,1,0]
                    elif event.key == pygame.K_LEFT:
                        self.pacman.next_move = [0,0,0,1]

            done = self.play_step(window)
            if done:
                break
        
        time.sleep(2)
        pygame.quit()
        

if __name__ == "__main__":
    pygame.init()
    game = PacmanGame()
    game.setup_board()
