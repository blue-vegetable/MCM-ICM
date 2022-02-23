import numpy as np
import random
from ypstruct import structure


def run(problem, params):

    # Problem Information
    costfunc = problem.costfunc
    nvar = problem.nvar
    source = problem.source
    destion = problem.destion

    # Parameters
    maxit = params.maxit
    npop = params.npop
    beta = params.beta
    pc = params.pc
    nc = int(np.round(pc*npop/2)*2)
    gamma = params.gamma
    mu = params.mu
    sigma = params.sigma

    # Empty Individual Template
    empty_individual = structure()
    empty_individual.position = None
    empty_individual.cost = None

    # Best Solution Ever Found
    bestsol = empty_individual.deepcopy()
    bestsol.cost = np.inf

    # Initialize Population
    pop = empty_individual.repeat(npop)
    for i in range(npop):
        q = np.random.permutation(np.arange(1, nvar-1))
        q = np.insert(q, 0, 0)
        q = np.append(q, nvar-1)
        pop[i].position = np.array(q)  # 生成随机序列

        pop[i].cost = costfunc(pop[i].position)
        if pop[i].cost < bestsol.cost:
            bestsol = pop[i].deepcopy()

    # Best Cost of Iterations
    bestcost = np.empty(maxit)

    # Main Loop
    for it in range(maxit):

        costs = np.array([x.cost for x in pop])
        avg_cost = np.mean(costs)
        if avg_cost != 0:
            costs = costs/avg_cost
        probs = np.exp(-beta*costs)

        popc = []
        for _ in range(nc//2):

            # Select Parents
            #q = np.random.permutation(npop)
            #p1 = pop[q[0]]
            #p2 = pop[q[1]]

            # Perform Roulette Wheel Selection
            p1 = pop[roulette_wheel_selection(probs)]
            p2 = pop[roulette_wheel_selection(probs)]

            # Perform Crossover
            c1, c2 = crossover(p1, p2, nvar)

            # Perform Mutation
            c1 = mutate(c1, mu, nvar, sigma)
            c2 = mutate(c2, mu, nvar, sigma)

            # Apply Bounds
            #apply_bound(c1, varmin, varmax)
            #apply_bound(c2, varmin, varmax)

            # Evaluate First Offspring
            c1.cost = costfunc(c1.position)
            if c1.cost < bestsol.cost:
                bestsol = c1.deepcopy()

            # Evaluate Second Offspring
            c2.cost = costfunc(c2.position)
            if c2.cost < bestsol.cost:
                bestsol = c2.deepcopy()

            # Add Offsprings to popc
            popc.append(c1)
            popc.append(c2)

        # Merge, Sort and Select
        pop += popc
        pop = sorted(pop, key=lambda x: x.cost)
        pop = pop[0:npop]

        # Store Best Cost
        bestcost[it] = bestsol.cost

        # Show Iteration Information
        print("Iteration {}: Best Cost = {}".format(it, bestcost[it]))

    # Output
    out = structure()
    out.pop = pop
    out.bestsol = bestsol
    out.bestcost = bestcost
    return out


def crossover(p1, p2, nvar, gamma=0.1):
    # c1 = p1.deepcopy()
    # c2 = p1.deepcopy()
    # alpha = np.random.uniform(-gamma, 1+gamma, *c1.position.shape)
    # c1.position = alpha*p1.position + (1-alpha)*p2.position
    # c2.position = alpha*p2.position + (1-alpha)*p1.position
    # return c1, c2
    c1 = p1.deepcopy()
    c2 = p2.deepcopy()
    index1 = random.randint(1, nvar - 1)
    index2 = random.randint(index1, nvar - 1)  # 用于交叉的区域
    # 怎么交叉? 更换顺序? 就不考虑python的时间复杂度啥的
    cross_position = c1.position[index1:index2]
    temp_position1 = np.array([])
    for i in range(len(c1.position)):
        if i == index1:
            temp_position1 = np.append(temp_position1, cross_position)
        if c1.position[i] not in cross_position:
            temp_position1 = np.append(temp_position1, c1.position[i])

    cross_position = c2.position[index1:index2]
    temp_position2 = np.array([])
    for i in range(len(c2.position)):
        if i == index1:
            temp_position2 = np.append(temp_position2, cross_position)
        if c2.position[i] not in cross_position:
            temp_position2 = np.append(temp_position2, c2.position[i])

    c1.position = temp_position1
    c2.position = temp_position2
    return c1, c2


def mutate(x, mu, nvar, sigma):
    # y = x.deepcopy()
    # flag = np.random.rand(*x.position.shape) <= mu
    # ind = np.argwhere(flag)
    # y.position[ind] += sigma*np.random.randn(*ind.shape)
    # return y
    y = x.deepcopy()
    index1 = np.random.randint(1, nvar-1)
    index2 = np.random.randint(1, nvar-1)
    y.position[index1], y.position[index2] = x.position[index2], x.position[index1]
    return y


def apply_bound(x, varmin, varmax):
    x.position = np.maximum(x.position, varmin)
    x.position = np.minimum(x.position, varmax)


def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
