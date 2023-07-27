#!/bin/env python3
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

import cardcraft

# Parallel environments
env = cardcraft.cardcraft()

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)

