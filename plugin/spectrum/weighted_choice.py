from __future__ import division
from random import random
from bisect import bisect

def Choice(available, counts, exclude=set()):
    return _weighted_choice(_weighted(available, counts, exclude))

def _weighted_choice(items_with_probs):
    """
    `items_with_probs`: a dictionary with items and their probs
    """
    items = items_with_probs.keys()
    probs = items_with_probs.values()

    accumulator = []
    prob_accumulator = 0
    for p in probs:
        prob_accumulator += p
        accumulator.append(prob_accumulator)

    while True:
        r = random()
        yield items[bisect(accumulator, r)]

def _weighted(available, counts, exclude=set()):
    """
    `available`: the set of available items
    `counts`: a dictionary of item names and counts
    `exclude`: a set of items to be excluded

    >>> _weighted(set(['a','b','c']), {'a':2, 'b':1})
    {'a': 0.5, 'c': 0.16666666666666666, 'b': 0.33333333333333331}
    >>> _weighted(set(['a','b','c','d']), {'a':2, 'b':1}, set(['d']))
    {'a': 0.5, 'c': 0.16666666666666666, 'b': 0.33333333333333331}
    """
    available -= exclude
    # items not in counts have implicit count=1
    total_counts = sum(counts.values()) + len(available)
    return dict(zip(available, (((counts.get(item, 0)+1) / total_counts) for item in available)))
