import numpy as np
import matplotlib.pyplot as plt

def f(theta, omega, m):
    return (np.cos(theta)**4 + 6*np.cos(theta)**2 + 1) * \
           (omega**3 / m) * \
           (1 + (omega/m)*(1 - np.cos(theta)))**(-3) * \
           (1 - np.cos(theta))

theta = np.linspace(0, np.pi, 1000)
ratios = np.logspace(-2, 2, 3)

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharex=True)

for ax, r in zip(axes, ratios):
    y = f(theta, r, 1.0)
    ax.plot(theta, y)
    ax.set_xlabel(r'$\theta$')
    ax.set_title(f"ω/m={r:.2g}")
    ax.grid(True)

axes[0].set_ylabel(r'$f(\theta)$')
fig.suptitle('Regimi ω << m → ω >> m')
plt.tight_layout()
plt.show()