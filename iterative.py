from itertools import count
import sys
from node import Node
sys.setrecursionlimit(10**9)


def iterative_insert(root, key):
    count = 0
    node = Node(key)
    if (root == None):
        count += 1
        root = node
        return count
    prev = None
    temp = root
    while (temp != None):
        if (temp.val > key):
            count += 1
            prev = temp
            temp = temp.left
        elif(temp.val < key):
            count += 1
            prev = temp
            temp = temp.right
    if (prev.val > key):
        count += 1
        prev.left = node
    else:
        prev.right = node
    
    return count
    

def iterative_search(root,key):
    count = 0
    while root is not None:
        if root.val == key:
            count += 1
            return root, count
        elif root.val < key:
            count += 1
            root = root.right
        else:
            root = root.left
    return root, count