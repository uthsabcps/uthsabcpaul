"""
Helper module to generate value sequences
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"

import random


def sequence(limit: int) -> list[int]:
    return list(range(limit))


def random_sequence(limit: int) -> list[int]:
    seq: list[int] = sequence(limit)

    for i in range(len(seq)):
        j = random.randint(0, limit-1)
        temp = seq[i]
        seq[i] = seq[j]
        seq[j] = temp

    return seq
