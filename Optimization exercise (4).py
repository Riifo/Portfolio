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
Repeat Exercise 1, use Ant Colony Optimization as a solution method.
'''

# with ChatGPT:

import numpy as np

# Define the TSP distances
distances = np.array([
    [0, 43.4, 35.5, 51.2],
    [43.4, 0, 28.0, 64.7],
    [35.5, 28.0, 0, 47.7],
    [51.2, 64.7, 47.7, 0]
])

# Define the parameters for the ACO algorithm
n_ants = 10
n_iterations = 100
alpha = 1.0
beta = 3.0
rho = 0.1
q0 = 0.9

# Initialize the pheromone matrix
pheromone = np.ones(distances.shape) / len(distances)

# Define the ACO algorithm
def aco_tsp(distances, pheromone, n_ants, n_iterations, alpha, beta, rho, q0):
    best_distance = float('inf')
    best_route = None

    for iteration in range(n_iterations):
        ant_routes = []
        ant_distances = []

        # Construct ant routes
        for ant in range(n_ants):
            current_city = 0
            unvisited_cities = set(range(1, len(distances)))

            ant_route = [current_city]
            ant_distance = 0

            while unvisited_cities:
                if np.random.rand() < q0:
                    next_city = max(unvisited_cities, key=lambda city: pheromone[current_city][city])
                else:
                    probabilities = np.power(pheromone[current_city][list(unvisited_cities)], alpha) * \
                                    np.power(1.0 / distances[current_city][list(unvisited_cities)], beta)
                    probabilities /= np.sum(probabilities)
                    next_city = np.random.choice(list(unvisited_cities), p=probabilities)

                ant_route.append(next_city)
                ant_distance += distances[current_city][next_city]

                current_city = next_city
                unvisited_cities.remove(current_city)

            ant_routes.append(ant_route)
            ant_distances.append(ant_distance)

        # Update pheromone matrix
        pheromone *= (1.0 - rho)
        for ant in range(n_ants):
            for i in range(len(ant_routes[ant]) - 1):
                pheromone[ant_routes[ant][i]][ant_routes[ant][i + 1]] += 1.0 / ant_distances[ant]

        # Update best solution
        min_distance = min(ant_distances)
        if min_distance < best_distance:
            best_distance = min_distance
            best_route = ant_routes[np.argmin(ant_distances)]

    return best_route, best_distance

# Run the ACO algorithm for TSP
best_route, best_distance = aco_tsp(distances, pheromone, n_ants, n_iterations, alpha, beta, rho, q0)

# Print the best route and distance
print("Best route: ", best_route)
print("Best distance: ", best_distance)



#! Solution
# Best route:  [0, 1, 2, 3]
# Best distance:  119.10000000000001