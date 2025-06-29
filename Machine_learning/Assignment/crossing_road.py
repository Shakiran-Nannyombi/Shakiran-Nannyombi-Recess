"""
train a Reinforcement Learning agent 
to navigate to cross the road with action 
right, left, right
"""

import numpy as np
import random

# Actions
LOOK_LEFT = 0
LOOK_RIGHT = 1
CROSS = 2
actions = ["look left", "look right", "cross"]

# States: 0 = start, 1 = looked left, 2 = looked right, 3 = looked left again, 4 = crossed
state_size = 5
action_size = 3

# Intializing Q-table
Q = np.zeros((state_size, action_size))

# seyting learning parameters
learning_rate = 0.1
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 1000

# function to determine crossing if road ios clear
def is_road_clear():
    # 30% chance the road is clear after look sequence
    return random.random() < 0.3

# Training loop
for episode in range(episodes):
    state = 0
    done = False
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, action_size - 1)
        else:
            action = np.argmax(Q[state])

        # State transitions
        if state == 0 and action == LOOK_LEFT:
            next_state = 1
            reward = -1
            done = False
        elif state == 1 and action == LOOK_RIGHT:
            next_state = 2
            reward = -1
            done = False
        elif state == 2 and action == LOOK_LEFT:
            next_state = 3
            reward = -1
            done = False
        elif state == 3 and action == CROSS:
            if is_road_clear():
                next_state = 4
                reward = 10
                done = True
            else:
                next_state = 0  # Start over
                reward = -5
                done = False
        else:
            next_state = 0  # Wrong action, restart
            reward = -5
            done = False

        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

# Test the trained agent
state = 0
steps = 0
print("\nAgent's actions to cross the road:")
while state != 4:
    action = np.argmax(Q[state])
    print(f"Step {steps+1}: {actions[action]}")
    if state == 0 and action == LOOK_LEFT:
        state = 1
    elif state == 1 and action == LOOK_RIGHT:
        state = 2
    elif state == 2 and action == LOOK_LEFT:
        state = 3
    elif state == 3 and action == CROSS:
        if is_road_clear():
            state = 4
            print("Agent crossed the road safely!")
        else:
            print("Road not clear, repeating sequence.")
            state = 0
    else:
        print("Wrong action, restarting sequence.")
        state = 0
    steps += 1
    
# output
    """
Agent's actions to cross the road:
Step 1: look left
Step 2: look right
Step 3: look left
Step 4: cross
Agent crossed the road safely!
    """