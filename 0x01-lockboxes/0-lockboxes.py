#!/usr/bin/python3
"""A script to determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    if not boxes or not boxes[0]:
        return False  # No boxes or the first box is empty

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # The first box is initially unlocked
    keys_stack = [0]  # Stack to keep track of keys to explore

    while keys_stack:
        current_box = keys_stack.pop()

        # Check the keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_stack.append(key)

    return all(unlocked_boxes)
