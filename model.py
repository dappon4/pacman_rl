import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
import numpy as np
from copy import deepcopy

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size = 4):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, 19)
        self.map_convert_linear1 = nn.Linear(28,50)
        self.map_convert_linear2 = nn.Linear(50,1)
        
        self.output_linear1 = nn.Linear(50,hidden_size)
        self.output = nn.Linear(hidden_size,output_size)
        
    def forward(self, state, board):
        state = torch.tensor(state, dtype = torch.float)
        board = torch.tensor(board, dtype = torch.float)
        
        board = F.relu(self.map_convert_linear1(board))
        board = F.relu(self.map_convert_linear2(board))
        board = board.squeeze(-1) # shape = [(31)]
        
        state = F.relu(self.linear1(state))
        state = F.relu(self.linear2(state)) # shape = [(19)]
        
        x = torch.cat([state,board],-1)
        x = F.relu(self.output_linear1(x))
        x = self.output(x)
        
        return x

    def save(self, file_name='model.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr = self.lr)
        self.criterion = nn.MSELoss()
    
    def train_step(self, state_old, board_old, action, reward, state_new, board_new, done):
        
        pred = self.model(state_old,board_old)
        target = pred.clone()
        for i in range(len(state_old)):
            Q_new = reward[i]
            if done[i] == False:
                next_Q = self.model(state_new[i],board_new[i])
                for j in range(4):
                    if state_new[i][j] == True:
                        next_Q[j] = -np.inf
                Q_new = reward[i] + self.gamma * torch.max(next_Q)
            
            action_cpy = np.array(action[i],dtype=np.float32)
            for j in range(4):
                if state_old[i][j] == True:
                    action_cpy[j] = -np.inf
            target[i][np.argmax(action_cpy)] = Q_new
        
        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()