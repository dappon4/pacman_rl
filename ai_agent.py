from ghosts import Ghost, Blinky, Pinky, Inky, Clyde
from pacman import Pacman
from game_ai import PacmanGame
from model import QTrainer, Linear_QNet
from collections import deque
import random
import pygame
import torch
import numpy as np
import time
import matplotlib.pyplot as plt

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class PacmanAI(Pacman):
    def __init__(self) -> None:
        super().__init__()
        self.memory = deque(maxlen = MAX_MEMORY)
        self.model = Linear_QNet(19, 100)
        self.trainer = QTrainer(self.model, LR, 0.9)
        self.epsilon = 0.3
        
    def get_state(self,game):
        """
        wall up,
        wall right,
        wall down,
        wall left,
        normalized pacman x,
        normalized pacman y,
        normalized blinky x,
        normalized blinky y,
        normalized pinky x,
        normalized pinky y,
        normalized inky x,
        normalized inky y,
        normalized clyde x,
        normalized clyde y,
        pacman is powerd up,
        blinky is eaten,
        pinky is eaten,
        inky is eaten,
        clyde is eaten,
        cookie map
        """
        if int(game.pacman.x) != game.pacman.x or int(game.pacman.y) != game.pacman.y:
            #print(game.pacman.x,game.pacman.y,"not int")
            wall_state = (
                game.pacman.last_move[0] == 0,
                game.pacman.last_move[1] == 0,
                game.pacman.last_move[2] == 0,
                game.pacman.last_move[3] == 0)
        else:
            #print(game.pacman.x,game.pacman.y,"int")
            x,y = int(game.pacman.x), int(game.pacman.y)
            try:
                wall_state = (
                    game.board[y - 1][x] == 1,
                    False if x == 27 else game.board[y][x + 1] == 1,
                    game.board[y + 1][x] == 1,
                    False if x == -1 else game.board[y][x - 1] == 1)
            except IndexError:
                print("index error in get state")
                print(x,y)
                exit()
        
        return [
            *wall_state,
            
            2 * game.pacman.x / game.board_width - 1,
            2 * game.pacman.y / game.board_height - 1,
            2 * game.blinky.x / game.board_width - 1,
            2 * game.blinky.y / game.board_height - 1,
            2 * game.pinky.x / game.board_width - 1,
            2 * game.pinky.y / game.board_height - 1,
            2 * game.inky.x / game.board_width - 1,
            2 * game.inky.y / game.board_height - 1,
            2 * game.clyde.x / game.board_width - 1,
            2 * game.clyde.y / game.board_height - 1,
            
            game.pacman.powerup_duration > 0,
            game.blinky.state == "eaten",
            game.pinky.state == "eaten",
            game.inky.state == "eaten",
            game.clyde.state == "eaten",
        ], game.cookie_board
    
    def get_move(self, state, board, legal_moves):
        if random.random() > self.epsilon:
            moves = self.model(state,board)
            
            # filter with legal moves
            for i in range(4):
                if legal_moves[i] == 0:
                    moves[i] = -np.inf
            idx = torch.argmax(moves).item()
            
            move = [0,0,0,0]
            move[idx] = 1
        
        else:
            idx = random.choice([i for i, val in enumerate(legal_moves) if val == 1])
            move = [0,0,0,0]
            move[idx] = 1
        
        return move
    
    def remember(self, state_old, board_old, action, reward, state_new, board_new, done):
        self.memory.append((state_old, board_old, action, reward, state_new, board_new, done))
    
    def train_short_memory(self, state_old, board_old, action, reward, state_new, board_new, done):
        self.trainer.train_step([state_old], [board_old], [action], [reward], [state_new], [board_new], [done])
    
    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        
        states, old_boards, actions, rewards, next_states, next_boards, dones = zip(*mini_sample)
        
        self.trainer.train_step(states, old_boards, actions, rewards, next_states, next_boards, dones)
            
def train():
    agent = PacmanAI()
    game = PacmanGame(pacman=agent)
    game.setup_board() 
    
    iterations = 0
    score_history = []
    while True:
        
        pygame.event.pump()
        
        state_old, board_old = agent.get_state(game)
        
        reward, done, score, action = game.play_step(state_old, board_old)

        state_new, board_new = agent.get_state(game)

        agent.train_short_memory(state_old, board_old, action, reward, state_new, board_new, done)

        agent.remember(state_old, board_old, action, reward, state_new, board_new, done)

        if done:
            #print("reset")
            print(f"iteration {iterations+1}: {score}, total mean score: {np.mean(score_history[-10:])}")
            score_history.append(score)
            iterations += 1
            game.reset()
            #print("train_long_memory")
            agent.train_long_memory()
        
        
if __name__ == "__main__":
    pygame.init()
    train()