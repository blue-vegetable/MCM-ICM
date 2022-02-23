import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import ga2 as ga

# Sphere Test Function

dis = [[0, 2, 3, 4, 5],
       [3, 0, 5, 6, 7],
       [2, 3, 0, 5, 2],
       [2, 3, 4, 0, 6],
       [4, 13, 4, 5, 0]]   # 各城市的距离(有向图)


def get_distance(x):
    # x是城市序列 np.array
    distance = 0
    for i in range(len(x)-1):
        distance += dis[int(x[i])][int(x[i+1])]
    return distance


# Problem Definition
problem = structure()
problem.costfunc = get_distance
problem.source = 0
problem.destion = len(dis[0])-1
problem.nvar = len(dis[0])

# GA Parameters
params = structure()
params.maxit = 100
params.npop = 2
params.beta = 1
params.pc = 1
params.gamma = 0.1
params.mu = 0.01
params.sigma = 0.1

# Run GA
out = ga.run(problem, params)

# Results
plt.plot(out.bestcost)
print(out.bestsol)
# plt.semilogy(out.bestcost)
plt.xlim(0, params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm (GA)')
plt.grid(True)
plt.show()
