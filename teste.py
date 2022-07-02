# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST
import sys
sys.setrecursionlimit(10**9)

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# A utility function to do inorder tree traversal


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
# 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80


# Print inoder traversal of the BST


sizes = [50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000, 75000, 100000, 125000, 150000, 175000, 20000, 250000]

for i in range (0, len(sizes)):
    f = open('C7/Construir' + str(sizes[i]) + '.txt', 'r')
    line = f.readlines()
    elements = line[0].split()
    print(sizes[i])
    # BUILD
    # inicializa a arvore
    r = Node(int(elements[0]))
    # begin_biuld = time.perf_counter_ns()
    
    # insere restante dos elementos
    for j in range (1, len(elements)):
        
        r = insert(r, int(elements[j]))
        # print('vai inserir')

    # end_biuld = time.perf_counter_ns()
    print('Biulded')

    # SEARCH
    # hits = 0
    # miss = 0
    # f = open('C7/Consultar' + str(sizes[i]) + '.txt', 'r')
    # line = f.readlines()
    # elements = line[0].split()

    # begin_search = time.perf_counter_ns()
    # for el in elements:
    #     # vai buscar 
    #     res = 0
    #     if res:
    #         hits = hits + 1
    #     else:
    #         miss = miss + 1
    # end_search = time.perf_counter_ns()
    # print('Searched')

    # recursive_results.loc[i] = [sizes[i], end_biuld-begin_biuld, end_search-begin_search, hits, miss]

# recursive_results.to_excel('recursive_results.xlsx')
print('Finish')
r.inorder()

