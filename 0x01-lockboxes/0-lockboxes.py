#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not.

    Returns:
        True if all boxes can be opened, else False.
    '''
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        box_to_open = keys.pop()
        if not unlocked[box_to_open]:
            unlocked[box_to_open] = True
            keys.update(boxes[box_to_open])

    return all(unlocked)
