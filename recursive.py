import sys
from node import Node

sys.setrecursionlimit(10**9)


def recursive_insert(root, key):
    count = 0
    if root is None:
        count += 1
        return Node(key), count
    else:
        if root.val == key:
            count += 1
            return root, count
        elif root.val < key:
            root.right, count = recursive_insert(root.right, key)
            count += 1
        else:
            root.left, count = recursive_insert(root.left, key)
    return root, count

def recursive_search(root,key):
    count = 0
    if root is None or root.val== key:
        count += 1
        return root, count
    if root.val < key:
        count += 1
        return recursive_search(root.right,key)
   
    return recursive_search(root.left,key)
 
