# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
#import statistics
import matplotlib.pyplot as plt

def random_walk_1d(number_of_steps):
  position = 0
  for e in range(1,number_of_steps + 1):
    move = random.choice([1,-1])
    position = position + move
  return position 


def trials_for_random_walk_1d(number_of_trials):
  trial_list = []
  for e in range(1,number_of_trials + 1):
    trial_list.append(random_walk_1d(16))
  average = sum(trial_list)/len(trial_list)
  #stdev = statistics.stdev(trial_list)
  print ("This is the average of all trials: {}".format(average))
  print ("This is the standard deviation of all trials: {}".format(stdev))
  return sorted(trial_list)
  

def random_walk_2d(number_of_steps):
  position_x = 0 
  position_y = 0
  for e in range(1,number_of_steps + 1):
    move_x = random.choice([1,-1])
    move_y =  random.choice([1,-1])
    position_x = position_x + move_x
    position_y = position_y + move_y 
  return (position_x**2 + position_y**2)**0.5
    
def trials_for_random_walk_2d(number_of_trials):
  trial_list = []
  for e in range(1,number_of_trials+1):
    trial_list.append(random_walk_2d(100))
  average = sum(trial_list)/len(trial_list)
  #stdev = statistics.stdev(trial_list)
  print ("This is the average of all trials: {}".format(average))
  #print ("This is the standard deviation of all trials: {}".format(stdev))
 
  
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

D = freqeuncy_counter(trials_for_random_walk_1d(10000))

plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())

plt.show()




            
            
                    











