#! /usr/bin/python3
# Powerball simulator
# 5 white balls chosen from 1 to 69.
# 1 red ball chosen from 1 to 26.

from random import randint

# white and red balls list creation
white_balls, red_balls = [], []
for i in range(1, 70):
    white_balls.append(i)
for i in range(1, 27):
    red_balls.append(i)

print(white_balls)
print(red_balls)


