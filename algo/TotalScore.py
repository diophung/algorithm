"""
Prob: given a series of symbols: blocks and n: the number of symbols.
if symbol is integer, add it to total score
if symbol is "+", add the last 2 scores to the total score
if symbol is "X", multiply the last score by 2 and add it to total score
if symbol is "Z", remove the last score from the total score.
"""


def totalScore(blocks, n):
    so_far = 0
    return so_far


blocks = [5, -2, 4, "Z", "X", 9, "+", "+"]
n = 8

print(totalScore(blocks, n))
