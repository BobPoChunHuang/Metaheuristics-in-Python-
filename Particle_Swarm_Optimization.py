# particle swarm optimization for Schwefel minimization problem


# need some python libraries
import copy
import math
from random import Random

# to setup a random number generator, we will specify a "seed" value
seed = 12345
myPRNG = Random(seed)

# to get a random number between 0 and 1, write call this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, write call this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, write call this: myPRNG.randint(lwrBnd,upprBnd)


# number of dimensions of problem
n = 200

# number of particles in swarm
swarmSize = 100


# Schwefel function to evaluate a real-valued solution x
# note: the feasible space is an n-dimensional hypercube centered at the origin with side length = 2 * 500

def evaluate(x):
    val = 0
    d = len(x)
    for i in range(d):
        val = val + x[i] * math.sin(math.sqrt(abs(x[i])))

    val = 418.9829 * d - val

    return val


# the swarm will be represented as a list of positions, velocities, values, pbest, and pbest values


def update_velocity(vel, phi1, phi2, pi, index, x):  # update velocity
    r1 = myPRNG.random()
    r2 = myPRNG.random()

    for i in range(len(vel)):
        for k in range(n):
            vel[i][k] = vel[i][k] + phi1 * r1 * (pi[i][k] - x[i][k]) + phi2 * r2 * (pi[index][k] - x[i][k])
    return vel


def update_pos(pos, vel):  # update position
    for i in range(len(vel)):
        for k in range(n):

            pos[i][k] = pos[i][k] + vel[i][k]
            if pos[i][k] > 500:
                pos[i][k] = 500
            if pos[i][k] < -500:
                pos[i][k] = -500
    return pos


pos = [[] for _ in range(swarmSize)]  # position of particles -- will be a list of lists
vel = [[] for _ in range(swarmSize)]  # velocity of particles -- will be a list of lists

curValue = []  # value of current position  -- will be a list of real values
pbest = []  # particles' best historical position -- will be a list of lists
pbestVal = []  # value of pbest position  -- will be a list of real values

# initialize the swarm randomly
for i in range(swarmSize):
    for j in range(n):
        pos[i].append(myPRNG.uniform(-500, 500))  # assign random value between -500 and 500
        vel[i].append(myPRNG.uniform(-1, 1))  # assign random value between -1 and 1

    curValue.append(evaluate(pos[i]))  # evaluate the current position

pBest = pos[:]  # initialize pbest to the starting position
pBestVal = curValue[:]  # initialize pbest to the starting position

for y in range(100):
    for i in range(swarmSize):  # for each particule
        x = evaluate(pos[i])  # compute the value
        if pBestVal[i] > x:  # compute pbest[i]
            pBest[i] = pos[i]
            pBestVal[i] = x
    MIN = 999999999
    index = 0
    for i in range(swarmSize):  # To keep tracking of pg
        if pBestVal[i] < MIN:
            MIN = pBestVal[i]
            index = i

    vel = update_velocity(vel, 0.0038, 0.0038, pBest, index, pos)
    pos = update_pos(pos, vel)
    print(pos)

print("\n")
print(pBest)
print(pBestVal)
print(pBestVal[index])

