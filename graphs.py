import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12.8, 9.6

def graph_all():
    data = pd.read_excel('results.xlsx', index_col='Size')

    print(data)

    plt.title('Tempo de construção da árvore', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(data['Recursive Biuld Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(data['Iterative Biuld Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('biuld_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Tempo de busca na árvore', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(data['Recursive Search Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(data['Iterative Search Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('search_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na construção da árvore', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(data['No Comparation Recursive Biuld'], color='Blue', marker='o', label='Recursivo')
    plt.plot(data['No Comparation Iterative Biuld'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('comp_build.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na busca na árvore', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(data['No Comparation Recursive Search'], color='Blue', marker='o', label='Recursivo')
    plt.plot(data['No Comparation Iterative Search'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('comp_search.png', dpi=300, bbox_inches='tight')

    plt.cla()


def graph_50to10k(): 
    df = pd.read_excel('results.xlsx')
    df = df[:13]
    print(df)

    plt.title('Tempo de construção da árvore - 50 à 10.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(df['Recursive Biuld Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['Iterative Biuld Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('50_to_10k_biuld_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Tempo de busca na árvore - 50 à 10.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(df['Recursive Search Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['Iterative Search Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('50_to_10k_search_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na construção da árvore - 50 à 10.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(df['No Comparation Recursive Biuld'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['No Comparation Iterative Biuld'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('50_to_10k_comp_build.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na busca na árvore - 50 à 10.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(df['No Comparation Recursive Search'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['No Comparation Iterative Search'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('50_to_10k_comp_search.png', dpi=300, bbox_inches='tight')

    plt.cla()

def graph_10kto100k(): 
    df = pd.read_excel('results.xlsx')
    df = df[14:22]
    print(df)

    plt.title('Tempo de construção da árvore - 10.000 à 100.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(df['Recursive Biuld Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['Iterative Biuld Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('10k_to_100k_biuld_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Tempo de busca na árvore - 10.000 à 100.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(df['Recursive Search Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['Iterative Search Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('10k_to_100k_search_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na construção da árvore - 10.000 à 100.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(df['No Comparation Recursive Biuld'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['No Comparation Iterative Biuld'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('10k_to_100k_comp_build.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na busca na árvore - 10.000 à 100.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(df['No Comparation Recursive Search'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['No Comparation Iterative Search'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('10k_to_100k_comp_search.png', dpi=300, bbox_inches='tight')

    plt.cla()

def graph_100kto250k(): 
    df = pd.read_excel('results.xlsx')
    df = df[14:22]
    print(df)

    plt.title('Tempo de construção da árvore - 100.000 à 250.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(df['Recursive Biuld Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['Iterative Biuld Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('100k_to_250k_biuld_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Tempo de busca na árvore - 100.000 à 250.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Tempo (ns)', fontsize=14)
    plt.plot(df['Recursive Search Time'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['Iterative Search Time'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('100k_to_250k_search_time.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na construção da árvore - 100.000 à 250.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(df['No Comparation Recursive Biuld'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['No Comparation Iterative Biuld'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('100k_to_250k_comp_build.png', dpi=300, bbox_inches='tight')

    plt.cla()

    plt.title('Número de comparações na busca na árvore - 100.000 à 250.000 elementos', fontsize=14)
    plt.xlabel('Tamanho do conjunto', fontsize=14)
    plt.ylabel('Comparações', fontsize=14)
    plt.plot(df['No Comparation Recursive Search'], color='Blue', marker='o', label='Recursivo')
    plt.plot(df['No Comparation Iterative Search'], color='Red', marker='^', label='Iterativo')
    plt.legend()
    plt.savefig('100k_to_250k_comp_search.png', dpi=300, bbox_inches='tight')

    plt.cla()

graph_all()
graph_50to10k()
graph_10kto100k()
graph_100kto250k()
print(rcParams['figure.figsize'])