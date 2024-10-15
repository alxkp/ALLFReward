# ALLFWorld

Early stage prototype of research codebase to use langauge models for intermediate feedback in textworld environments

Example prompt:

```
USER

Given a representation of the scene in alfworld, return a numerical score representing the reward, based on how close the model is to completing the task. Return only the score, with nothing else.

You are in the middle of a room. Looking quickly around you, you see a drawer 2, a shelf 5, a drawer 1, a shelf 4, a sidetable 1, a drawer 5, a shelf 6, a shelf 1, a shelf 9, a cabinet 2, a sofa 1, a cabinet 1, a shelf 3, a cabinet 3, a drawer 3, a shelf 11, a shelf 2, a shelf 10, a dresser 1, a shelf 12, a garbagecan 1, a armchair 1, a cabinet 4, a shelf 7, a shelf 8, a safe 1, and a drawer 4.

Your task is to: put some vase in safe.

> go to shelf 6 You arrive at loc 4. On the shelf 6, you see a vase 2.

> take vase 2 from shelf 6 You pick up the vase 2 from the shelf 6.

> go to safe 1 You arrive at loc 3. The safe 1 is closed.
---------------------------------------------------------------
ASSISTANT 2068 T/s

3
```

## Direct Control with Language Model Policies

Language models have shown their ability to generate high quality reward functions in Eureka (Ma, et al 2024)

Here, we directly use language models as a mechanism to control classic Reinforcement Learning problems such as an inverted pendulum, and a doubly inverted pendulum.

Our scripts are located at `scripts/cartpole.py` and `scripts/double_pendulum.py`

We give some preliminary results below.


![Cartpole LLM Policy](cartpole_LLM_policy.mov)

![Double Pendulum LLM Policy](double_pendulum_LLM_policy.mov)


We see that the cartpole system, as a significantly more linear system than the double pendulum is able to be controlled directly by the LLM, whereas the much more nonlinear double pendulum is significantly more challenging for an LLM to control zero shot.

We give some example prompts below, and full results are located in `results/`


For the single cartpole:
```
---

    The following are a list of state observations of a cartpole system.  Please control it to stand upright.

    Upright is an angle of 0, and angular velocity of 0; and any x value is acceptable.

    Cart position: -0.00
    Cart velocity: -0.01
    Pole angle: 0.00
    Pole angular velocity: -0.00

    What force should be applied to the cart? Respond with a number between -1 (full left) and 1 (full right).

    Think step by step beforehand, but your final answer must include a single number giving the force.

----
Step 0: Action = 0.50, Reward = 1.00
```

For the double cartpole
```
    The following are state observations of a double inverted pendulum system. Please control it to stand upright.
    Upright is when both poles are vertical (angles close to 0 or π) and angular velocities are 0.

    1. Cart position: 0.25 m
    2. Angle of first pole: -0.20 radians
    3. Angle of second pole: 0.38 radians
    4. Cart velocity: 3.42 m/s
    5. Angular velocity of first pole: -6.34 radians/second
    6. Angular velocity of second pole: 7.34 radians/second
    7. Constraint force on cart: 0.00 N

    What force should be applied to the cart? Respond with a number between -1 (full left) and 1 (full right).

    Think step by step beforehand, but your final answer must include a single number giving the force.

-----
Step 2: Action = 1.00, Reward = 8.91
```



## Credit:

Building off of scripts in ALfworld codebase, credit: 


Currently debuging Alfword training code and integration with Cerebras

```
@inproceedings{ALFWorld20,
  title ={{ALFWorld: Aligning Text and Embodied
           Environments for Interactive Learning}},
  author={Mohit Shridhar and Xingdi Yuan and
          Marc-Alexandre C\^ot\'e and Yonatan Bisk and
          Adam Trischler and Matthew Hausknecht},
  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
  year = {2021},
  url = {https://arxiv.org/abs/2010.03768}
}
```
