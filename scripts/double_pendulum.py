import os
import gymnasium as gym
import numpy as np
import re
from time import sleep
from cerebras.cloud.sdk import Cerebras

def state_to_prompt(observation):
    cart_pos, sin_pole1, sin_pole2, cos_pole1, cos_pole2, cart_vel, ang_vel1, ang_vel2, constraint_force = observation

    angle1 = np.arctan2(sin_pole1, cos_pole1)
    angle2 = np.arctan2(sin_pole2, cos_pole2)

    return f"""
    The following are state observations of a double inverted pendulum system. Please control it to stand upright.
    Upright is when both poles are vertical (angles close to 0 or π) and angular velocities are 0.

    1. Cart position: {cart_pos:.2f} m
    2. Angle of first pole: {angle1:.2f} radians
    3. Angle of second pole: {angle2:.2f} radians
    4. Cart velocity: {cart_vel:.2f} m/s
    5. Angular velocity of first pole: {ang_vel1:.2f} radians/second
    6. Angular velocity of second pole: {ang_vel2:.2f} radians/second
    7. Constraint force on cart: {constraint_force:.2f} N

    What force should be applied to the cart? Respond with a number between -1 (full left) and 1 (full right).
    
    Think step by step beforehand, but your final answer must include a single number giving the force.
    """

def llama_generate(prompt):
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
    
    number_pattern = r'-?\d*\.?\d+'
    numbers = re.findall(number_pattern, response.content)
    
    valid_numbers = []
    for num in numbers:
        try:
            float_num = float(num)
            if -1 <= float_num <= 1:
                valid_numbers.append(float_num)
        except ValueError:
            continue  
    
    if valid_numbers:
        return valid_numbers[-1]
    else:
        print("No valid action found in LLaMa response. Using random action.")
        return np.random.uniform(-1, 1)

def run_double_pendulum_simulation(num_episodes=5, max_steps=1000):
    env = gym.make("InvertedDoublePendulum-v5", render_mode="human")
    
    for episode in range(num_episodes):
        observation, info = env.reset()
        total_reward = 0
        
        for step in range(max_steps):
            prompt = state_to_prompt(observation)
            
            action = llama_generate(prompt)
            
            observation, reward, terminated, truncated, info = env.step([action])
            total_reward += reward
            

            print(prompt)
            print("-----")
            print(f"Step {step}: Action = {action:.2f}, Reward = {reward:.2f}")
            sleep(0.1)
            
            if terminated or truncated:
                break
        
        print(f"Episode {episode + 1} finished after {step + 1} steps. Total reward: {total_reward:.2f}")
        print("---")
    
    env.close()

if __name__ == "__main__":
    client = Cerebras(
        api_key=os.environ.get("CEREBRAS_API_KEY"),
    )
    run_double_pendulum_simulation()
