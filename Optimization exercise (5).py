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

# with ChatGPT:

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the distance matrix
# The distances are provided in kilometers
distances = [
    [0, 43.4, 35.5, 51.2],    # Tampere
    [43.4, 0, 28.0, 64.7],    # Toijala
    [35.5, 28.0, 0, 47.7],    # Vesilahti
    [51.2, 64.7, 47.7, 0]     # Sastamala
]

# Create routing model
manager = pywrapcp.RoutingIndexManager(len(distances), 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Define the cost function (distance callback)
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distances[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Define the search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the TSP
assignment = routing.SolveWithParameters(search_parameters)
if assignment:
    # Extract the solution
    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        node = manager.IndexToNode(index)
        route.append(node)
        index = assignment.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(index))

    # Print the result
    print("Shortest route: ", route)
    total_distance = assignment.ObjectiveValue()
    print("Total distance: {} km".format(total_distance))
else:
    print("No solution found.")
