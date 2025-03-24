from random import randrange

import numpy as np
import matplotlib.pyplot as plt
import uuid

targets = ["authorities", "humans", "parrots", "cars", "motorcycles", "buildings", "warehouses"]
robots = ["Terminator #" + str(uuid.uuid4())[:5] for i in range(7)]
harvest = np.array([[randrange(i * j) for i in range(10, 80, 10)] for j in range(10, 80, 10)])

fig, ax = plt.subplots()
im = ax.imshow(harvest)

ax.set_xticks(np.arange(len(robots)), labels=robots)
ax.set_yticks(np.arange(len(targets)), labels=targets)
plt.setp(ax.get_xticklabels(), rotation=60, ha="right", rotation_mode="anchor")

for i in range(len(targets)):
    for j in range(len(robots)):
        text = ax.text(j, i, harvest[i, j], ha="center", va="center", color="w")

ax.set_title("Targets destroyed")
fig.tight_layout()
plt.show()
