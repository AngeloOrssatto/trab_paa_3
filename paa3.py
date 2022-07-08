from itertools import count
from node import Node
from iterative import iterative_insert, iterative_search
from recursive import recursive_insert, recursive_search
import time, sys
import pandas as pd

sys.setrecursionlimit(10**9)


sizes = [
    50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000, 12500, 15000,
    20000, 25000, 30000, 40000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 250000
]

print(sizes)

results = pd.DataFrame(columns=[
    'Size', 
    'Recursive Biuld Time',
    'Recursive Search Time',
    'Iterative Biuld Time',
    'Iterative Search Time',
    'No Comparation Recursive Biuld',
    'No Comparation Recursive Search',
    'No Comparation Iterative Biuld',
    'No Comparation Iterative Search',
    'Hits',
    'Miss'
])

for i in range (0, len(sizes)):
    f = open('C7/Construir' + str(sizes[i]) + '.txt', 'r')
    line = f.readlines()
    elements = line[0].split()
    print('---------------------------------------------------')
    print('File:', sizes[i])

    # BUILD RECURSIVE
    # inicializa a arvore
    count_recursive_build_comp = 0
    begin_biuld_recursive = time.perf_counter_ns()
    root_r = Node(int(elements[0]))
    # insere restante dos elementos
    for j in range (1, len(elements)):
        r_r, c = recursive_insert(root_r, int(elements[j]))
        count_recursive_build_comp += c
    end_biuld_recursive = time.perf_counter_ns()
    print('RECURSIVE - Biulded in', end_biuld_recursive-begin_biuld_recursive, 'ns |', count_recursive_build_comp, 'comparations')

    # BUILD ITERATIVE
    # inicializa a arvore
    count_iterative_build_comp = 0
    begin_biuld_iterative = time.perf_counter_ns()
    root_i = Node(int(elements[0]))
    # insere restante dos elementos
    for j in range (1, len(elements)):
        c = iterative_insert(root_i, int(elements[j]))
        count_iterative_build_comp += c
    end_biuld_iterative = time.perf_counter_ns()
    print('ITERATIVE - Biulded in', end_biuld_iterative-begin_biuld_iterative, 'ns |', count_iterative_build_comp, 'comparations')

    # SEARCH
    f = open('C7/Consultar' + str(sizes[i]) + '.txt', 'r')
    line = f.readlines()
    elements = line[0].split()
    # SEARCH RECURSIVE
    hits = 0
    miss = 0
    count_recursive_search_comp = 0
    begin_search_recursive = time.perf_counter_ns()
    for el in elements:
        res, c = recursive_search(root_i, int(el))
        count_recursive_search_comp += c
        if res:
            hits = hits + 1
        else:
            miss = miss + 1
    end_search_recursive = time.perf_counter_ns()
    print('RECURSIVE - Searched in', end_search_recursive-begin_search_recursive, 'ns |', count_recursive_search_comp, 'comparations |', hits, 'hits and', miss, 'miss')

    # SEARCH ITERATIVE
    hits = 0
    miss = 0
    count_iterative_search_comp = 0
    begin_search_iterative = time.perf_counter_ns()
    for el in elements:
        res, c = iterative_search(root_i, int(el))
        count_iterative_search_comp += c
        if res:
            hits = hits + 1
        else:
            miss = miss + 1
    end_search_iterative = time.perf_counter_ns()
    print('ITERATIVE - Searched in', end_search_iterative-begin_search_iterative, 'ns |', count_iterative_search_comp, 'comparations |', hits, 'hits and', miss, 'miss')

    results.loc[i] = [
        sizes[i], 
        end_biuld_recursive-begin_biuld_recursive,
        end_search_recursive-begin_search_recursive,
        end_biuld_iterative-begin_biuld_iterative,
        end_search_iterative-begin_search_iterative,
        count_recursive_build_comp,
        count_recursive_search_comp,
        count_iterative_build_comp,
        count_iterative_search_comp,
        hits,
        miss
    ]

results.to_csv('results.csv')
print('Finish')