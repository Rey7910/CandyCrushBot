# Notes

## Objectives:

- Create the agent (object oriented structure).
- Think about the possible algorithms.

## Notes on the agent:

- Environment: Discrete, static, deterministic, observable and episodic. The agent takes the best move (this is, the move which assures the greatest
score or creates a special candy) for the current board, without considering 
future possibilities nor past decisions.

## Problem description:

- Utility (in priority order):
    1. Create a special candy.
    2. Max score in one move for the current board.
   
- Perceptions:
    1. Matrix representing the board.
    2. List with the locations (as pairs) of special candies.

- Actions:
    1. Return a tuple with two pairs indicating the best move. 

- Information stored:
    1. It doesn't really store information. The only relevant information is passed as a perception.


