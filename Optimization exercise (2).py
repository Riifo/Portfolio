# Exercise 3: Warehouse location

'''
You have a small business and need a warehouse for your products.
You have customers in 5 places and you know how many times you delivered your products to each customer last year: Vähärauma (90 deliveries), Vihelä (105), Friitala (120), Harjunpää (60) and Pinomäki (130).
Where should you place your warehouse in order to minimize the distance you need to travel based on the information from last year?

'''
# on GOOGLE Maps, km by car

# location, km by car
# Vähärauma to Vihelä, 13.3km
# Vähärauma to Friitala 12.8km
# Vähärauma to Harjunpää 12.2km
# Vähärauma to Pinomäki 6.9km

# Vihelä to Friitala 5.3km
# Vihelä to Harjunpää 4.9km
# Vihelä to Pinomäki 7.9km

# Friitala to Harjunpää 9.4km
# Friitala to Pinomäki 7.6km

# Harjunpää to Pinomäki 12.8km


# with ChatGPT

from pulp import *

# Define the delivery locations and their distances
locations = ["Vähärauma", "Vihelä", "Friitala", "Harjunpää", "Pinomäki"]
distances = {
    ("Vähärauma", "Vihelä"): 13.3,
    ("Vihelä", "Vähärauma"): 13.3,
    ("Vähärauma", "Friitala"): 12.8,
    ("Friitala", "Vähärauma"): 12.8,
    ("Vähärauma", "Harjunpää"): 12.2,
    ("Harjunpää", "Vähärauma"): 12.2,
    ("Vähärauma", "Pinomäki"): 6.9,
    ("Pinomäki", "Vähärauma"): 6.9,
    ("Vihelä", "Friitala"): 5.3,
    ("Friitala", "Vihelä"): 5.3,
    ("Vihelä", "Harjunpää"): 4.9,
    ("Harjunpää", "Vihelä"): 4.9,
    ("Vihelä", "Pinomäki"): 7.9,
    ("Pinomäki", "Vihelä"): 7.9,
    ("Friitala", "Harjunpää"): 9.4,
    ("Harjunpää", "Friitala"): 9.4,
    ("Friitala", "Pinomäki"): 7.6,
    ("Pinomäki", "Friitala"): 7.6,
    ("Harjunpää", "Pinomäki"): 12.8,
    ("Pinomäki", "Harjunpää"): 12.8
}

# Define the number of deliveries for each location
deliveries = {
    "Vähärauma": 90,
    "Vihelä": 105,
    "Friitala": 120,
    "Harjunpää": 60,
    "Pinomäki": 130
}

# Define the problem
prob = LpProblem("WarehouseLocation", LpMinimize)

# Define the decision variables
x = LpVariable.dicts("x", locations, lowBound=0, cat='Binary')

# Define the objective function
prob += lpSum(distances[i, j] * x[i] * deliveries[j] for i, j in distances.keys())

# Define the constraints
prob += lpSum(x[i] for i in locations) == 1, "SelectOneLocation"
for i in locations:
    prob += lpSum(x[i] for i in locations) >= 0.2, "MinDeliveries_{}".format(i)

# Solve the problem
prob.solve()

# Print the result
print("Optimal solution:")
for i in locations:
    if x[i].varValue == 1:
        print("Warehouse location: {}".format(i))


#! Optimal solution:
# Warehouse location: Pinomäki