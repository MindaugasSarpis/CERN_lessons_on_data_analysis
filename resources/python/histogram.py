import matplotlib.pyplot as plt
import numpy as np

# plt.xkcd()

# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(19680801)
N_points = 100000
n_bins = 20
# Generate two normal distributions
dist1 = rng.standard_normal(N_points)

fig, ax = plt.subplots()
fig.set_size_inches(3, 4)

ax.set_xlabel('Value', fontsize = 20, loc='right')
ax.set_ylabel('Frequency', fontsize = 20, labelpad = 20, loc='top')

[ax.spines[i].set_linewidth(2) for i in ['top', 'right', 'left', 'bottom']] 
ax.tick_params(axis='both', labelsize=20, size=10, width=2, top = True, right = True, direction = 'inout')
ax.set_xticks([-5, -2.5, 0, 2.5, 5])
ax.set_yticks(np.linspace(0,20000,11))
ax.set_ylim(0, 20000)

ax.spines['bottom'].set_visible(True)

# We can set the number of bins with the *bins* keyword argument.
n, bins, patches = ax.hist(dist1, bins=n_bins)
max_height = np.max(n)

# print(max_height)
plt.savefig('Important_Histo.pdf')