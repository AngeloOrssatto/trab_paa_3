import sys, time
import pandas as pd
sys.setrecursionlimit(10**9)

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def insert(root, key) :
        node = Node(key)
        if (root == None) :
            root = node
            return
        prev = None
        temp = root
        while (temp != None):
            if (temp.val > key):
                prev = temp
                temp = temp.left
            elif(temp.val < key):
                prev = temp
                temp = temp.right
        if (prev.val > key):
            prev.left = node
        else :
            prev.right = node


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def search(root,key):

    while root is not None:
        if root.val == key:
            return root
        elif root.val < key:
            root = root.right
        else:
            root = root.left
    return root
     

sizes = [
    #50, 100, 200, 300, 500
    50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000, 12500, 15000,
    20000, 25000, 30000, 40000, 50000, 75000, 100000, 125000, 150000, 175000, 20000, 250000
]

iterative_results = pd.DataFrame(columns=['Size', 'Biuld Time', 'Search Time', 'Hit', 'Miss'])

for i in range (0, len(sizes)):
    f = open('C7/Construir' + str(sizes[i]) + '.txt', 'r')
    line = f.readlines()
    elements = line[0].split()
    print(sizes[i])
    # BUILD
    # inicializa a arvore
    root = Node(int(elements[0]))
    begin_biuld = time.perf_counter_ns()
    # insere restante dos elementos
    for j in range (1, len(elements)):
        
        r = insert(root, int(elements[j]))
        # print('vai inserir')

    end_biuld = time.perf_counter_ns()
    print('Biulded in', end_biuld-begin_biuld, 'ns')

    # SEARCH
    hits = 0
    miss = 0
    f = open('C7/Consultar' + str(sizes[i]) + '.txt', 'r')
    line = f.readlines()
    elements = line[0].split()

    begin_search = time.perf_counter_ns()
    for el in elements:
        res = search(root, int(el))
        if res:
            hits = hits + 1
        else:
            miss = miss + 1
    end_search = time.perf_counter_ns()
    print('Searched')

    iterative_results.loc[i] = [sizes[i], end_biuld-begin_biuld, end_search-begin_search, hits, miss]

iterative_results.to_csv('iterative_results.csv')
print('Finish')
