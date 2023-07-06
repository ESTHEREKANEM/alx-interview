#!/usr/bin/python3
"This Script will unlock all the boxes"


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

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

    return False
