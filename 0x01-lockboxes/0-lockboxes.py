#!/usr/bin/python3
'''Lockboxes problem'''


def canUnlockAll(boxes):
    '''Checks if keys in boxes can open all boxes'''
    keys = [0]
    visited = set()

    while keys:
        current_key = keys.pop()
        if current_key not in visited:
            visited.add(current_key)
            keys.extend(boxes[current_key])

    return len(visited) == len(boxes)
