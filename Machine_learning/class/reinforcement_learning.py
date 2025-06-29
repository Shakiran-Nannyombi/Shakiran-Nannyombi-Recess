import numpy as np
import random

# Define environment parameters
positions = 5  # Number of positions (0 to 4)
actions = 2    # Number of possible actions (0: move left, 1: move right)

# Initialize Q-table
Q = np.zeros((positions, actions))

# Define learning parameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.4

# Training loop
for episode in range(episodes):
    state = random.randint(0, positions - 1)
    done = False
    while not done:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)
        else:
            action = np.argmax(Q[state])

        # Take action and observe new state and reward
        if action == 0:  # Move left
            next_state = max(0, state - 1)
        else:  # Move right
            next_state = min(positions - 1, state + 1)

        # Reward structure
        if next_state == positions - 1:
            reward = 10
            done = True
        else:
            reward = -1

        # Q-learning update
        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state

print("Learned Q-values:")
print(Q)

# Test the trained agent
state = 0
steps = 0
print("\nAgent's path to the goal:")
while state < positions - 1:
    action = np.argmax(Q[state])
    if action == 0:
        state = max(0, state - 1)
    else:
        state = min(positions - 1, state + 1)
    steps += 1
    print(f"Step {steps}: Moved to position {state}")

print(f"Reached the goal in {steps} steps.")

#Final Q-table
print("\nFinal Q-table:")
print(Q)
 
 # output
"""Learned Q-values:
[[62.17055763 70.18954734]
 [62.17058285 79.09949815]
 [70.18950926 88.99944265]
 [79.09949802 99.99942828]
 [88.99940541 99.9994176 ]]

Agent's path to the goal:
Step 1: Moved to position 1
Step 2: Moved to position 2
Step 3: Moved to position 3
Step 4: Moved to position 4
Reached the goal in 4 steps.

Final Q-table:
[[62.17055763 70.18954734]
 [62.17058285 79.09949815]
 [70.18950926 88.99944265]
 [79.09949802 99.99942828]
 [88.99940541 99.9994176 ]]"""