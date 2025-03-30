import numpy as np

# Docking methods and their binding affinities
methods = ['ZDOCK', 'HDOCK', 'HADDOCK', 'ClusPRO', 'GRAMM']
binding_affinities = {
    'ZDOCK': [-5.6, -5.5, -5.5, -5.5, -5.5, -5.4, -5.4, -5.3, -5.3, -5.3],
    'HDOCK': [-6.0, -6.0, -5.7, -5.6, -5.2, -5.2, -5.2, -5.2, -5.2, -5.1],
    'HADDOCK': [-5.5, -5.3, -5.2, -5.2, -5.1, -5.0, -4.7, -4.6, -4.6, -4.6],
    'ClusPRO': [-5.5, -5.5, -5.5, -5.4, -5.4, -5.4, -5.3, -5.3, -5.3, -5.2],
    'GRAMM': [-5.0, -5.0, -5.0, -4.8, -4.7, -4.6, -4.5, -4.5, -4.5, -4.4]
}

# Define success thresholds
thresholds = [-4.0, -4.5, -5.0, -5.5, -6.0, -6.5]

print("Success Rates for Top Poses:")
for method in methods:
    affinities = binding_affinities[method]
    print(f"
Method: {method}")
    for threshold in thresholds:
        # Calculate the success rate
        success_count = np.sum(np.array(affinities) <= threshold)
        success_rate = (success_count / len(affinities)) * 100
        print(f"Threshold {threshold} kcal/mol: {success_rate:.2f}%")