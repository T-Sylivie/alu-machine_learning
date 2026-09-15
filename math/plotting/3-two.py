#!/usr/bin/env python3
"""
Exponential decay comparison of C-14 and Ra-226
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 20000, 1000)
t1 = np.log(2)

# Half-lives
t2 = 5730   # C-14
t3 = 1600   # Ra-226

y1 = np.exp(-(t / t2) * t1)
y2 = np.exp(-(t / t3) * t1)

plt.plot(t, y1, 'r--', label="C-14")
plt.plot(t, y2, 'g-', label="Ra-226")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.title("Exponential Decay of Radioactive Elements")
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.legend(loc="upper right")
plt.show()
