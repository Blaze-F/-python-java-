import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

from sympy import symbols, integrate, sin

# Define the symbols for symbolic computation
r, r_s, psi = symbols('r r_s psi')

# Define the expression for critical angle psi_c
psi_c = np.pi / 2  # At this point, psi_c is π/2

# Schwarzschild metric components
E = symbols('E')
L = symbols('L')

# Function for the equation governing particle's trajectory
eq = (1 / r**2) * (L**2 / r**2) - (1 - r_s / r) * (E**2 - 1)

# Define the limits of r for integration
r_lower_limit = 1.01  # To avoid singularity at r_s
r_upper_limit = 6 * r_s

# Calculate psi_c for different r values
psi_c_values = []
r_values = np.linspace(r_lower_limit, r_upper_limit, 100)

for r_val in r_values:
    eq_sub = eq.subs({r: r_val})
    sol = np.sqrt(float(solve(eq_sub, L**2)[0].evalf())))
    psi_c_values.append(np.arccos(sol / r_val))

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(r_values, psi_c_values)
plt.xlabel('r')
plt.ylabel('Critical Angle (psi_c)')
plt.title('Critical Angle vs r in Schwarzschild Spacetime')
plt.grid(True)
plt.show()
