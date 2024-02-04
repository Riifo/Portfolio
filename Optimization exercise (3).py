# Exercise 1: Travelling AI student

# Travelling AI student starts from Tampere and returns to Tampere. He visits Toijala, Vesilahti and Sastamala.
# Find the shortest possible path for him to complete the round-trip route. (Travelling salesman problem)
# Return a document that describes how you solved the problem. Use figures and tables and present the code you used.
# In which order should the traveller visit the cities? How long is the route? There are a lot of examples available.

# Routes on GOOGLE Maps, by car

# Tampere to Toijala: (35min) 43.4km
# Toijala to Vesilahti: (30min) 28.0km
# Vesilahti to Sastamala: (50min) 47.7km
# Sastamala to Tampere: (45min) 51.2km

# Toijala to Sastamala: (1h 8min) 64.7km
# Tampere to Vesilahti: (33min) 35.5km

'''
Repeat Exercise 1, use Genetic Algorithm as a solution method.
'''

# with ChatGPT:

import random
import numpy as np
from deap import algorithms, base, creator, tools

# Define the TSP distances
distances = {
    ('Tampere', 'Toijala'): 43.4,
    ('Toijala', 'Vesilahti'): 28.0,
    ('Vesilahti', 'Sastamala'): 47.7,
    ('Sastamala', 'Tampere'): 51.2,
    ('Toijala', 'Sastamala'): 64.7,
    ('Tampere', 'Vesilahti'): 35.5
}

# Create a list of cities
cities = list(set([city for city_pair in distances.keys() for city in city_pair]))

# Define the fitness function
def tsp_fitness(individual):
    distance = 0
    for i in range(len(individual)):
        city1 = cities[individual[i]]
        city2 = cities[individual[(i+1)%len(individual)]]
        if (city1, city2) in distances:
            distance += distances[(city1, city2)]
        else:
            distance += distances[(city2, city1)]  # consider reverse order as well
    return distance,


# Create a Fitness class for the TSP problem
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Register the necessary functions for the Genetic Algorithm
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(len(cities)), len(cities))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", tsp_fitness)

# Define the main function to solve the TSP problem
def tsp_ga():
    pop_size = 100
    n_generations = 500
    cx_prob = 0.8
    mut_prob = 0.2

    # Create the initial population
    pop = toolbox.population(n=pop_size)

    # Run the Genetic Algorithm
    algorithms.eaSimple(pop, toolbox, cx_prob, mut_prob, n_generations, verbose=True)

    # Return the best individual
    best_individual = tools.selBest(pop, 1)[0]
    return best_individual

# Run the TSP Genetic Algorithm
best_route = tsp_ga()
print("Best route: ", [cities[i] for i in best_route])


#! Solution, went through 500 calculation things
# Best route:  ['Tampere', 'Toijala', 'Vesilahti', 'Sastamala']