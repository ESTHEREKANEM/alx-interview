#!/usr/bin/python3
"This Script will unlock all the boxes"

def canUnlockAll(boxes):
    numBoxes = len(boxes)
    unlocked = [False] * numBoxes
    unlocked[0] = True

    keys = boxes[0]
    while keys:
        key = keys.pop()
        if key >= numBoxes:
            continue
        unlocked[key] = True
        keys.extend(boxes[key])

    return all(unlocked)
