# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 00:56:06 2017

@author: user
"""
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def random_walk_2d(number_of_steps):
  position_x = 0 
  position_y = 0
  for e in range(1,number_of_steps + 1):
    move_x = random.choice([1,-1])
    move_y =  random.choice([1,-1])
    position_x = position_x + move_x
    position_y = position_y + move_y 
  return (position_x, position_y)


    
def trials_for_random_walk_2d(number_of_trials):
  trial_list = []
  for e in range(1,number_of_trials+1):
    trial_list.append(random_walk_2d(100))
  return (trial_list)


def add_one(anumber):
    return anumber + 1

def freqeuncy_counter(alist):
    freqenucy_dict = {}
    for e in alist:
        if e not in freqenucy_dict:
            freqenucy_dict[e] = 1
        else:
            freqenucy_dict[e] = add_one(freqenucy_dict[e])
    return freqenucy_dict



D = freqeuncy_counter(trials_for_random_walk_2d(1000000000))

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

xpos = [] #position of x coordinate
for e in D.keys():
    xpos.append(e[0])

ypos = [] #position of y coordinate
for e in D.keys():
    ypos.append(e[1])

zpos = np.ones(len(xpos))# all z coordinate starts at zeros

dx = np.ones(len(xpos)) # width of the bars
dy = np.ones(len(ypos)) # length of the bars
dz = D.values()  # height of the bars

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz , color = '#00ceaa')
plt.show()
