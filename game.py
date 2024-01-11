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

COOCKIES = [
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

COOCKIES_SET = set([(i,j) for j in range(len(COOCKIES)) for i in range(len(COOCKIES[0])) if COOCKIES[j][i] == 0])
#1: wall
#0: coockie
#2: ghost spawn
#3: power up

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20

GAME_SPEED = 10


class PacmanGame:
    def __init__(self, winndows_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT):
        self.board = BOARD
        self.coockies = COOCKIES
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
        self.coockies = COOCKIES
    
    def get_legal_moves(self,agent):
        moves = [1,1,1,1] # up, right, down, left
        if self.board[agent.y][agent.x] == 2:
            return [1,0,0,0]
        
        if 0 < agent.x < len(self.board[0]) - 1:
            if self.board[agent.y][agent.x - 1] == 1:
                moves[3] = 0
            if self.board[agent.y][agent.x + 1] == 1:
                moves[1] = 0
        if 0 < agent.y < len(self.board) - 1:
            if self.board[agent.y - 1][agent.x] == 1:
                moves[0] = 0
            if self.board[agent.y + 1][agent.x] == 1 or self.board[agent.y - 1][agent.x] == 2:
                moves[2] = 0
        
        if isinstance(agent,Ghost):
            last_idx = agent.last_move.index(1)
            map_counter_movement = {0:2,1:3,2:0,3:1}
            moves[map_counter_movement[last_idx]] = 0
        
        return moves
    
    def draw_coockies(self,window):
        for coockie in COOCKIES_SET:
            pygame.draw.circle(window, (255, 255, 0), (coockie[0] * BLOCK_SIZE + BLOCK_SIZE // 2, coockie[1] * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 5)
    
    def draw_pacman(self,window):
        pygame.draw.rect(window, (0, 0, 0), (self.pacman.prev_x * BLOCK_SIZE, self.pacman.prev_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.circle(window, (255, 255, 0), (self.pacman.x * BLOCK_SIZE + BLOCK_SIZE // 2, self.pacman.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
    
    def draw_ghosts(self,window):
        for ghost in self.ghosts:
            pygame.draw.rect(window, (0, 0, 0), (ghost.prev_x * BLOCK_SIZE, ghost.prev_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for ghost, color in zip(self.ghosts,self.ghost_colors):
            pygame.draw.circle(window, color, (ghost.x * BLOCK_SIZE + BLOCK_SIZE // 2, ghost.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        
        
    def update_window(self, window):
        self.draw_ghosts(window)
        self.draw_coockies(window)
        self.draw_pacman(window)
        
        pygame.display.flip()
    
    def display_score(self,window):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (650, self.height // 2)
        window.blit(text, textRect)
    
    def move_agent(self,agent,move):
        agent.prev_x = agent.x
        agent.prev_y = agent.y
        if move == [1,0,0,0]:
            agent.y -= 1
        elif move == [0,1,0,0]:
            agent.x += 1
        elif move == [0,0,1,0]:
            agent.y += 1
        elif move == [0,0,0,1]:
            agent.x -= 1

        if agent.x == -1:
            agent.x = len(self.board[0]) - 1
        if agent.x == len(self.board[0]):
            agent.x = 0
    
    def play_step(self,window):
        """self.pacman.move()
            self.pacman.update()
            
            for ghost in self.ghosts:
                ghost.move(self.board, self.pacman)
                """

        move = self.pacman.get_move(self.get_legal_moves(self.pacman))
        self.move_agent(self.pacman,move)
        
        if (self.pacman.x,self.pacman.y) in COOCKIES_SET:
            COOCKIES_SET.remove((self.pacman.x,self.pacman.y))
            self.score += 10
        
        for ghost in self.ghosts:
            move = ghost.get_move(self.get_legal_moves(ghost),self.pacman)
            self.move_agent(ghost,move)
        
        self.display_score(window)
        self.update_window(window)
        self.clock.tick(GAME_SPEED)

    def setup_board(self):
        # Set up the game window
        window_width = 800
        window_height = 600
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
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.play_step(window)
        pygame.quit()
        

if __name__ == "__main__":
    pygame.init()
    game = PacmanGame()
    game.setup_board()
