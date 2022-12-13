import gym
import numpy as np

class player:
    def __init__(self):
        self.health=30
        self.deck=[]
        self.field=[]
        self.hand=[]

class cardcraft(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MyGym, self).__init__()
        # initialize any game state variables here
        self.state = np.zeros(3)
        self.player = player()
        self.enemy = player()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(np.array([0,0,0]),np.array([1,1,1]))

    def turn(self,p):
        #draw a card
        if(len(p.hand) > 10):
            p.deck.pop()
        else:
            p.hand.append(p.deck.pop())

        #each 'playset' involves a card and a target

    def step(self, action):
        self.turn(player)
        self.turn(enemy)
        reward = 0
        done = false
        return np.array(self.state), reward, done, {}

    def reset(self):
        # reset the environment to the initial state
        self.state = np.zeros(3)
        return np.array(self.state)

    def render(self, mode='human', close=False):
        # render the environment to the screen
        pass
