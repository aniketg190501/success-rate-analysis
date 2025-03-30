import matplotlib.pyplot as plt
import numpy as np

# Docking methods and their success rates from your output
methods = ['ZDOCK', 'HDOCK', 'HADDOCK', 'ClusPRO', 'GRAMM']
thresholds = [-4.0, -4.5, -5.0, -5.5, -6.0, -6.5]

# Success rates from your output
success_rates = {
    'ZDOCK': [100, 100, 100, 50, 0, 0],
    'HDOCK': [100, 100, 100, 40, 20, 0],
    'HADDOCK': [100, 100, 60, 10, 0, 0],
    'ClusPRO': [100, 100, 100, 30, 0, 0],
    'GRAMM': [100, 90, 30, 0, 0, 0]
}

# Plotting the success rates
plt.figure(figsize=(8, 6))

for method in methods:
    plt.plot(thresholds, success_rates[method], marker='o', label=method, linestyle='-', linewidth=2)

# Adding plot details
plt.xlabel("Binding Affinity (kcal/mol)")
plt.ylabel("Success Rate (%)")
plt.xticks(thresholds)
plt.ylim(0, 110)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Docking Methods")
plt.show()