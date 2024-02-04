# Exercise 2: Farmer and SAMK do optimization

'''
# SAMK's advertising problem (grading 4-5)

# SAMK has budgeted up to 8000€ per week for local advertisement. The money is to be allocated among four promotional media: TV spots, newspaper ads, and two types of radio advertisements.
The goal is to reach the largest possible high-potential audience through the various media. The following table presents the number of potential customers reached by making use of advertisement in each of the four media.
It also provides the cost per advertisement placed and the maximum number of ads than can be purchased per week.

# Medium 	Audience reached per ad  Cost per ad  Max ads per week
# TV spot     5000 	                    800         12
# Newspaper 	8500 	                925 	    5
# Radio (30s, prime) 2400 	            290 	    25
# Radio (1min, afternoon) 2800 	        380 	    20

# The company arrangements require that at least five radio spots be placed each week. To ensure a board-scoped promotional campaign, management also insists that no more than 1800€ be spent on radio advertising every week.

# Tips:
# 4 decision variables = different types of ads
# Objective: Maximize the audience - use different ads wisely.
# Constraints: max ads/week, weekly budget, minimum number of radio spots, max budget for radio
# non-negativity constraints = all the decision variables need to be non-negative
'''

# with ChatGPT
# Radio prime is named RadioOne
# Radio afternoon is named RadioTwo

from pulp import *

# Define the problem
prob = LpProblem("MediaOptimization", LpMaximize)

# Define the decision variables
tv = LpVariable("TV", 0, 12, LpInteger)
newspaper = LpVariable("Newspaper", 0, 5, LpInteger)
radio_one = LpVariable("RadioOne", 0, 25, LpInteger)
radio_two = LpVariable("RadioTwo", 0, 20, LpInteger)

# Define the objective function
audience_per_ad = {
    "TV": 5000,
    "Newspaper": 8500,
    "RadioOne": 2400,
    "RadioTwo": 2800
}

cost_per_ad = {
    "TV": 800,
    "Newspaper": 925,
    "RadioOne": 290,
    "RadioTwo": 380
}

prob += (audience_per_ad["TV"] * tv + audience_per_ad["Newspaper"] * newspaper +
         audience_per_ad["RadioOne"] * radio_one + audience_per_ad["RadioTwo"] * radio_two)

# Define the constraints
prob += (cost_per_ad["TV"] * tv + cost_per_ad["Newspaper"] * newspaper +
         cost_per_ad["RadioOne"] * radio_one + cost_per_ad["RadioTwo"] * radio_two) <= 8000, "Budget"
prob += radio_one + radio_two >= 5, "RadioAds"

# Solve the problem
prob.solve()

# Print the result
print("Optimal solution:")
print("TV: {} ads".format(tv.varValue))
print("Newspaper: {} ads".format(newspaper.varValue))
print("RadioOne: {} ads".format(radio_one.varValue))
print("RadioTwo: {} ads".format(radio_two.varValue))
print("Total audience reached: {}".format(value(prob.objective)))


#! Optimal solution:
# TV: 0.0 ads
# Newspaper: 5.0 ads
# RadioOne: 9.0 ads
# RadioTwo: 2.0 ads
# Total audience reached: 69700.0