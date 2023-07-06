#!/usr/bin/python3
"This Script will unlock all the boxes"


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    keys = boxes[0]
    for key in keys:
        if key < num_boxes:
            unlocked[key] = True

    for i in range(1, num_boxes):
        if not unlocked[i]:
            return False

    return True
