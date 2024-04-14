import pygame
import time
from agent import Agent
from ghosts import Ghost, Blinky, Pinky, Clyde, Inky
from pacman import Pacman
import numpy as np
import random

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

COOKIES = np.array([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])

COOKIES_SET_TEST = {(1,1)}

COOKIES_SET = set([(i,j) for j in range(len(COOKIES)) for i in range(len(COOKIES[0])) if COOKIES[j][i] == 1])
POWERUPS_SET = set([(i,j) for j in range(len(BOARD)) for i in range(len(BOARD[0])) if BOARD[j][i] == 3])
PATH_SET = set([(i,j) for j in range(len(BOARD)) for i in range(len(BOARD[0])) if BOARD[j][i] == 0])
#1: wall
#0: cookie
#2: ghost spawn
#3: power up

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
BLOCK_SIZE = 20

GAME_SPEED = 200
POWERUP_DURATION = 50


class PacmanGame:
    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT, pacman = Pacman()):
        self.board = BOARD
        self.board_width = len(self.board[0])
        self.board_height = len(self.board)
        self.cookies = COOKIES_SET.copy()
        self.cookie_board = np.copy(COOKIES)
        self.powerups = POWERUPS_SET.copy()
        self.score = 0
        self.clock = pygame.time.Clock()
        self.pacman = pacman
        self.blinky = Blinky()
        self.pinky = Pinky()
        self.clyde = Clyde()
        self.inky = Inky()
        
        self.window_height = window_height
        self.ghosts = [self.blinky, self.pinky,self.clyde,self.inky]
        self.ghost_colors = [(255,0,0),(255,0,180),(255,165,0),(173,216,230)]
        
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Pacman Game")
        
    def reset(self):
        self.score = 0
        self.board = BOARD
        self.cookies = COOKIES_SET.copy()
        self.powerups = POWERUPS_SET.copy()
        
        self.draw_black_rect()
        self.pacman.x, self.pacman.y = random.choice(list(PATH_SET))
        self.pacman.powerup_duration = 0
        self.pacman.next_move = [0,0,0,0]
        legal_moves = self.get_legal_moves(self.pacman)
        try:
            idx = random.choice([i for i, val in enumerate(legal_moves) if val == 1])
            self.pacman.next_move[idx] = 1
        except IndexError:
            print("index error at pacman reset")
            print(self.pacman.x,self.pacman.y)
            exit()
        
        for ghost in self.ghosts:
            pygame.draw.rect(self.window,(0, 0, 0), (ghost.x * BLOCK_SIZE, ghost.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            
            ghost.x = ghost.spawn_x
            ghost.y = ghost.spawn_y
            ghost.state = "alive"
            ghost.switch_dir = False
            ghost.last_legal_moves = [0,0,0,0]
            
        
    
    def get_legal_moves(self,agent):
        assert int(agent.x) == agent.x and int(agent.y) == agent.y
        
        moves = [1,1,1,1] # up, right, down, left
        agent.x, agent.y = int(agent.x), int(agent.y)
        # check if agent is in the spawn area of ghosts
        if self.board[agent.y][agent.x] == 2:
            if isinstance(agent,Ghost):
                agent.state = "alive"
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
    
    def draw_misc(self):
        # draw cookies
        for cookie in self.cookies:
            pygame.draw.circle(self.window, (255, 255, 0), (cookie[0] * BLOCK_SIZE + BLOCK_SIZE // 2, cookie[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 5)
        # draw powerups
        for powerup in self.powerups:
            pygame.draw.circle(self.window, (255, 0, 0), (powerup[0] * BLOCK_SIZE + BLOCK_SIZE // 2, powerup[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
    
    def draw_pacman(self):
        # draw pacman
        pygame.draw.circle(self.window, (255, 255, 0), (self.pacman.x * BLOCK_SIZE + BLOCK_SIZE // 2, self.pacman.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
    
    def draw_ghosts(self):
        # if pacman is not powered up
        if self.pacman.powerup_duration == 0:
            for ghost, color in zip(self.ghosts,self.ghost_colors):
                if ghost.state == "alive":
                    pygame.draw.circle(self.window, color, (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
                elif ghost.state == "eaten":
                    pygame.draw.circle(self.window, (255, 255, 255), (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 4)
        
        # if pacman is powered up
        elif self.pacman.powerup_duration > 0:
            for ghost in self.ghosts:
                if ghost.state == "alive":
                    pygame.draw.circle(self.window, (0, 0, 255), (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2) 
                elif ghost.state == "eaten":
                    pygame.draw.circle(self.window, (255, 255, 255), (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 4)
    
    def draw_black_rect(self):
        # draw black rectangle to erase previous position of pacman and ghosts
        pygame.draw.rect(self.window, (0, 0, 0), (self.pacman.prev_x * BLOCK_SIZE, self.pacman.prev_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for ghost in self.ghosts:
            pygame.draw.rect(self.window, (0, 0, 0), (ghost.prev_x * BLOCK_SIZE, ghost.prev_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    def update_window(self):
        self.draw_black_rect()
        self.draw_misc()
        self.draw_ghosts()
        self.draw_pacman()
        pygame.display.flip()
        self.clock.tick(GAME_SPEED)
    
    def display_score(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (650, self.window_height // 2)
        self.window.blit(text, textRect)
    
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
    
    def play_intermediate(self):
        done = False
        reward = 0
        for ghost in self.ghosts:
            
            if (self.pacman.x,self.pacman.y) == (ghost.x,ghost.y):
                # if pacman is in the same cell as a ghost
                if self.pacman.powerup_duration == 0 and ghost.state == "alive":
                    # if pacman is not powered up and ghost is alive, end game
                    reward -= 100
                    done = True
                else:
                    # if pacman is powered up or ghost is eaten, increase score
                    self.score += 100
                    ghost.state = "eaten"
                    reward += 30
            self.move_agent(ghost,ghost.last_move)
        
        self.move_agent(self.pacman,self.pacman.last_move)
        
        #print(self.pacman.prev_x,self.pacman.prev_y)
        
        self.display_score()
        self.update_window()
        #self.clock.tick(GAME_SPEED)
        
        return reward,done
    
    def play_step(self, state_old, board_old):
        
        assert int(self.pacman.x) == self.pacman.x and int(self.pacman.y) == self.pacman.y
        self.pacman.x, self.pacman.y = int(self.pacman.x), int(self.pacman.y)
        
        reward = 0
        done = False
        # if pacman is at the same position as a cookie
        if (self.pacman.x,self.pacman.y) in self.cookies:
            # remove cookie from set
            self.cookies.remove((self.pacman.x,self.pacman.y))
            self.cookie_board[self.pacman.y][self.pacman.x] = 0
            # if all cookies are eaten end game
            if len(self.cookies) == 0:
                return True
            self.score += 10
            reward += 10
        
        # if pacman is at the same position as a powerup
        if (self.pacman.x,self.pacman.y) in self.powerups:
            # remove powerup from set
            assert (self.pacman.x,self.pacman.y) in self.powerups
            self.powerups.remove((self.pacman.x,self.pacman.y))
            # set timer for powerup
            self.pacman.powerup_duration = POWERUP_DURATION
            # switch direction of ghosts
            for ghost in self.ghosts:
                assert int(ghost.x) == ghost.x and int(ghost.y) == ghost.y
                if ghost.state == "alive":
                    ghost.switch_dir = True
        
        for ghost in self.ghosts:
            if (self.pacman.x,self.pacman.y) == (ghost.x,ghost.y):
                # if pacman is in the same cell as a ghost
                if self.pacman.powerup_duration == 0 and ghost.state == "alive":
                    # if pacman is not powered up and ghost is alive, end game
                    reward -= 100
                    done = True
                else:
                    # if pacman is powered up or ghost is eaten, increase score
                    self.score += 100
                    ghost.state = "eaten"
                    reward += 30
        
        
        # move pacman
        legal_moves = self.get_legal_moves(self.pacman)
        action = self.pacman.get_move(state_old, board_old, legal_moves)
        self.move_agent(self.pacman,action)
        
        for ghost in self.ghosts:
            move = ghost.get_move(self.get_legal_moves(ghost),self.pacman)
            self.move_agent(ghost,move)
        
        # if pacman is powered up   
        if self.pacman.powerup_duration > 0:
            # decrease powerup duration
            self.pacman.powerup_duration -= 1
            
            # if powerup duration is over switch direction of ghosts
            if self.pacman.powerup_duration == 1:
                for ghost in self.ghosts:
                    if ghost.state == "alive":
                        ghost.switch_dir = True
        
        self.update_window()
        
        intermediate_reward,intermediate_done = self.play_intermediate()
        
        #self.clock.tick(GAME_SPEED)

        # if nothing happened decrease reward
        reward -= 1
        
        reward += intermediate_reward
        
        return reward, (done or intermediate_done), self.score, action
            
    
    def setup_board(self):
        for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] == 1:
                        pygame.draw.rect(self.window, (0, 0, 255), (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    elif self.board[row][col] == 2:
                        pygame.draw.rect(self.window, (255, 0, 0), (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    elif self.board[row][col] == 3:
                        pygame.draw.circle(self.window, (255, 0, 255), (col * BLOCK_SIZE + BLOCK_SIZE // 2, row * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 5)
        
        pygame.display.update()
        

if __name__ == "__main__":
    pygame.init()
    game = PacmanGame()
    game.setup_board()
