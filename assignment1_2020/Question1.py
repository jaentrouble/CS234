#Gridworld

import numpy as np

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

TERMINATE = -1

Rs = -1
Rg = 5
Rr = -5
gamma = 1

reward = np.full((12,4), Rs)
reward[4] = [Rr,Rr,Rr,Rr,]
reward[11] = [Rg,Rg,Rg,Rg,]

Value = np.zeros(12)

Next_state = [
    [0,0,0,1],
    [1,0,1,2],
    [2,1,2,3],
    [3,2,7,3],
    [-1,-1,-1,-1],
    [5,4,9,6],
    [6,5,10,7],
    [3,6,11,7],
    [4,8,12,9],
    [5,8,9,10],
    [6,9,10,11],
    [-1,-1,-1,-1],
    [8,12,12,13],
    [13,12,13,14],
    [14,13,14,15],
    [15,14,15,15],
]

Pi_g = [RIGHT,RIGHT,RIGHT,DOWN,]