import os
import gymnasium as gym
import numpy as np
import re
from time import sleep

from cerebras.cloud.sdk import Cerebras

# Function to convert state to a text prompt (placeholder for LLaMa integration)
def state_to_prompt(observation):
    x, x_dot, theta, theta_dot = observation
    return f"""
    The following are a list of state observations of a cartpole system.  Please control it to stand upright.

    Upright is an angle of 0, and angular velocity of 0; and any x value is acceptable.

    Cart position: {x:.2f}
    Cart velocity: {x_dot:.2f}
    Pole angle: {theta:.2f}
    Pole angular velocity: {theta_dot:.2f}
    
    What force should be applied to the cart? Respond with a number between -1 (full left) and 1 (full right).
    
    Think step by step beforehand, but your final answer must include a single number giving the force.
    """

# Placeholder function for LLaMa model (replace with your actual implementation)
def llama_generate(prompt):
    # This is where you'd call your LLaMa 3.1 model
    # For now, we'll just return a random action
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3.1-8b",
    )


    response = chat_completion.choices[0].message
    # breakpoint()
    number_pattern = r'-?\d*\.?\d+'
    numbers = re.findall(number_pattern, response.content)
    
    valid_numbers = []
    for num in numbers:
        try:
            float_num = float(num)
            if -1 <= float_num <= 1:
                valid_numbers.append(float_num)
        except ValueError:
            continue  # Skip any strings that can't be converted to float
    
    # breakpoint()
    if valid_numbers:
        # Return the last valid number found
        return valid_numbers[-1]
    else:
        print("No valid action found in LLaMa response. Using random action.")
        return np.random.uniform(-1, 1)


# Function to parse LLaMa response into an action
def parse_llama_response(response):
    try:
        action = float(response)
        return np.clip(action, -1, 1)
    except ValueError:
        print("Invalid LLaMa response. Using random action.")
        return np.random.uniform(-1, 1)

# Main simulation loop
def run_inverted_pendulum_simulation(num_episodes=5, max_steps=1000):
    env = gym.make("InvertedPendulum-v5", render_mode="human")

    for episode in range(num_episodes):
        observation, info = env.reset()
        total_reward = 0

        for step in range(max_steps):
            # Convert the observation to a prompt
            prompt = state_to_prompt(observation)
            
            # Get action from LLaMa model (simulated here)
            # Parse the response into an action
            action = llama_generate(prompt)
            
            # Take the action in the environment
            observation, reward, terminated, truncated, info = env.step([action])
            total_reward += reward

            
            print(prompt)
            print("----")
            print(f"Step {step}: Action = {action:.2f}, Reward = {reward:.2f}")
            sleep(0.1)

            if terminated or truncated:
                break

        print(f"Episode {episode + 1} finished after {step + 1} steps. Total reward: {total_reward:.2f}")
        print("---")

    env.close()

# Run the simulation
if __name__ == "__main__":

    client = Cerebras(
        # This is the default and can be omitted
        api_key=os.environ.get("CEREBRAS_API_KEY"),
    )

    run_inverted_pendulum_simulation()
