#!/usr/bin/python3
def canUnlockAll(boxes):
    '''Checks if keys in boxes can open all boxes'''
    
    keys = [0]
    visited = set()

    while keys:
        current_key = keys.pop()
        print(current_key)
        if current_key not in visited:
            visited.add(current_key)
            keys.extend(boxes[current_key])

    return len(visited) == len(boxes)
