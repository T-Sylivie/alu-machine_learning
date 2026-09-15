#!/usr/bin/env python3
"""
Line graph of cubic function
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

plt.plot(x, y, 'r-')
plt.xlim(0, 10)
plt.xlabel("x")
plt.ylabel("y = x^3")
plt.title("Cubic Line Graph")
plt.show()
