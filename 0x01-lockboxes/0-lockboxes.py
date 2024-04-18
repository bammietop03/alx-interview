#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ function that can unlock all """
    if not boxes:
        return False

    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]

    while stack:
        box_index = stack.pop()

        for key in boxes[box_index]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
