#!/usr/bin/env python3
"""
Stacked bar chart of fruit per person
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ["Farrah", "Fred", "Felicia"]

# Colors for each fruit
colors = ["red", "yellow", "#ff8000", "#ffe5b4"]
labels = ["apples", "bananas", "oranges", "peaches"]

# Plot stacked bars
plt.bar(people, fruit[0], color=colors[0], width=0.5, label=labels[0])
plt.bar(people, fruit[1], bottom=fruit[0], color=colors[1], width=0.5, label=labels[1])
plt.bar(people, fruit[2], bottom=fruit[0] + fruit[1], color=colors[2], width=0.5, label=labels[2])
plt.bar(people, fruit[3], bottom=fruit[0] + fruit[1] + fruit[2],
        color=colors[3], width=0.5, label=labels[3])

plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))
plt.legend()
plt.show()
