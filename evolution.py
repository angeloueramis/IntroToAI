import random

#example 1
exercises = ["Pushup", "Squat", "Plank", "Jump Rope", "Burpees"]

population_size = 6
generations = 10

#random workout plan
def create_individual():
    return random.sample(exercises, 3)

def fitness(plan):
    score = 0
    if "Pushup" in plan:
        score += 2
    if "Squat" in plan:
        score += 2
    if "Burpees" in plan:
        score += 3
    score += len(plan)
    return score

#crossover
def crossover(parent1, parent2):
    child = list(set(parent1[:2] + parent2[1:]))
    while len(child) < 3:
        child.append(random.choice(exercises))
    return child[:3]

#mutation
def mutate(plan):
    if random.random() < 0.3:
        plan[random.randint(0,2)] = random.choice(exercises)
    return plan

population = [create_individual() for _ in range(population_size)]

for generation in range(generations):

    population = sorted(population, key=fitness, reverse=True)

    next_gen = population[:2]

    while len(next_gen) < population_size:
        parent1 = random.choice(population[:3])
        parent2 = random.choice(population[:3])

        child = crossover(parent1, parent2)
        child = mutate(child)

        next_gen.append(child)

    population = next_gen

best = max(population, key=fitness)

print("Best Workout Plan:", best)
print("Fitness Score:", fitness(best))



#example 2
exercises = ["Running", "Cycling", "Jump Rope", "Situps", "Lunges"]

population_size = 6
generations = 8

def create_plan():
    return random.sample(exercises, 3)

def fitness(plan):
    score = 0
    if "Running" in plan:
        score += 3
    if "Jump Rope" in plan:
        score += 2
    if "Lunges" in plan:
        score += 2
    score += len(plan)
    return score

def crossover(p1, p2):
    child = list(set(p1[:2] + p2[1:]))
    while len(child) < 3:
        child.append(random.choice(exercises))
    return child[:3]

def mutate(plan):
    if random.random() < 0.3:
        plan[random.randint(0,2)] = random.choice(exercises)
    return plan

population = [create_plan() for _ in range(population_size)]

for _ in range(generations):

    population = sorted(population, key=fitness, reverse=True)

    next_gen = population[:2]

    while len(next_gen) < population_size:
        p1 = random.choice(population[:3])
        p2 = random.choice(population[:3])

        child = crossover(p1, p2)
        child = mutate(child)

        next_gen.append(child)

    population = next_gen

best = max(population, key=fitness)

print("\nBest Fitness Routine:", best)
print("Fitness Score:", fitness(best))