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
