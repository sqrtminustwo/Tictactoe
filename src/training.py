#States: 
# 1. Won (3 in a row)
# 2. Made a pseudorandom move
# 3. Stopped oponent from winning (placed in between 3 in row)
# 4. Lost (oponent 3 in row)
#Actions:
#   1. Make a move
#Reward:
#   ...
#   
# Q-table:
#   


import gym # type: ignore
from gym import spaces # type: ignore
import numpy as np # type: ignore

class MyCustomEnv(gym.Env):
    """
    Custom Environment that follows gym interface.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MyCustomEnv, self).__init__()
        # Define action and observation space
        # Example: Discrete action space of size 9 (3x3 tictactoe field)
        self.action_space = spaces.Discrete(9)
        # Example: Observation space is a 2D coordinate in a 3x3 grid
        self.observation_space = spaces.Box(low=0, high=2, shape=(2,), dtype=np.int32)

        # Initialize state
        self.state = [0] * 9
        self.agent_num = 1
        self.not_agent_num = 2

    def reset(self):
        """
        Reset the environment to an initial state and return the initial observation.
        """
        self.state = np.array([1, 1])
        return self.state

    def won(self, num):
        # left upper to right bottom corner
        if self.state[0] == num and self.state[0] == self.state[4] == self.state[8]:
            return True
        # right upper to left bottom corner
        if self.state[2] == num and self.state[2] == self.state[4] == self.state[6]:
            return True
        #vertical lines check
        vert = 0
        while vert <= len(self.state)-3:
            if self.state[vert] == num and self.state[vert] == self.state[vert+1] == self.state[vert+2]:
                return True
            vert += 3
        #horizontal lines check
        for i in range(0, 3):
            if self.state[i] == num and self.state[i] == self.state[i+3] == self.state[i+6]:
                return True
        return False
    
    def blocked_win(self, move):
        self.state[move[0]][move[1]] = self.not_agent_num
        toreturn = self.won(self.not_agent_num)
        self.state[move[0]][move[1]] = self.agent_num
        return toreturn
            

    def step(self, action):
        """
        Execute one time step within the environment.
        """
        # Define action
        moves = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        move = moves[action]
        old_state = self.state[move[0]][move[1]]
        self.state[move[0]][move[1]] = self.agent_num

        # Check if goal is reached
        done = self.won(self.agent_num)
        reward = 0
        if done:
            reward += 2
        elif old_state != 0 or self.won(self.not_agent_num):
            reward -= 1
        elif self.blocked_win(move):
            reward += 1

        info = {}
        return self.state, reward, done, info