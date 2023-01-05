import numpy as np
import matplotlib.pyplot as plt

def zeta(s, n_terms):
  return sum(1/n**s for n in range(1, n_terms+1))

# Read input from the user
s_start = float(input("Enter the start value for s: "))
s_end = float(input("Enter the end value for s: "))
n_terms = int(input("Enter the number of terms in the summation: "))

s = np.linspace(s_start, s_end, 100)
y = [zeta(si, n_terms) for si in s]

plt.plot(s, y)
plt.xlabel('s')
plt.ylabel('ζ(s)')
plt.title('Riemann Zeta Function')
plt.show()
