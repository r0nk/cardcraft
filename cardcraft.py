import gym
from gym import spaces
import numpy as np
import card
import random

standard_deck = []

for i in range(30):
    standard_deck.append(card.card())

def random_action():
    return (random.randrange(12),random.randrange(10))

class player:
    def __init__(self):
        self.health=30
        self.deck=[]
        self.field={'1':None,'2':None,'3':None,'4':None}
        self.hand=[]

class cardcraft(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(cardcraft, self).__init__()
        # initialize any game state variables here
        self.state = np.zeros(3)
        self.player = player()
        self.enemy = player()
        self.reward=0
        self.done=False
        self.turn=0 # 0 player, 1 enemy
        #each 'playset' involves a card and a target
        #'summoning' -> hand card, board space
        #'attacking' -> field card, target
        # action is basically (card,target) pair
        self.action_space = spaces.MultiDiscrete([12,10])

        # observation space is a bit different:
        # 2X(n/30) player health 
        # 16 cards total
            # 8 in hand
            # 4 on each side of field
        # each card has
        # health (n/20)
        # damage (n/20)
        # cost (n/10)
        # trigger (n)
        # effect (n)
        self.observation_space = spaces.MultiDiscrete([30,30])

    #draw a card
    def draw(self,p):
        if(len(p.hand) > 8):
            p.deck.pop()
        else:
            p.hand.append(p.deck.pop())

    def damage(self,target,amount):
        if target == 0:
            self.player.health-=amount
            if(self.player.health<=0):
                self.done=True
                self.reward=-100
        if target == 25:
            self.enemy.health-=amount
            if(self.enemy.health<=0):
                self.done=True
                self.reward=100

        if target > 8 and target < 13:
            self.player.field[target-8].health-=amount
        if target > 12 and target < 17:
            self.enemy.field[target-12].health-=amount

    def play_from_hand(self,action):
        print(f"play from hand {action=}")

    def play_from_field(self,action):
        print(f"play from field {action=}")

    def step(self, action):
        if(action[0] < 8):
            self.play_from_hand(action)
        else:
            self.play_from_field(action)
        print(f"{action=}")
        return np.array(self.state), self.reward, self.done, {}

    def reset(self):
        # reset the environment to the initial state
        self.state = np.zeros(3)
        return np.array(self.state)

    def render(self, mode='human', close=False):
        print(f"HEALTH P[{self.player.health}] E[{self.enemy.health}]")
        print(f"{self.enemy.field=}")
        print(f"{self.player.field=}")
        print(f"{self.player.hand=}")
        pass

cce = cardcraft()
for i in range(4):
    cce.step(random_action())
    cce.render()
