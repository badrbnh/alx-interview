#!/usr/bin/python3
"""
Lockboxes problem
"""


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    box_set = set(boxes[0])
    for n in boxes[0]:
        if n < len(boxes):
            box_set.update(boxes[n])

    for i in range(1, len(boxes)):
        if i in box_set:
            box_set.update(boxes[i])
        else:
            return False

    return True
