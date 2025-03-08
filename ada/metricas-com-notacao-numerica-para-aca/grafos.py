# Cria a lista  bolinha fruits
bolinha_fruits = ['Morango', 'Abacaxi', 'Cereja']

# Cria lista fruits
fruits = ['Laranja', 'Pera', 'Melão']

# Mostra a contagem de referência bolinha_fruits
print(sys.getrefcount(bolinha_fruits))

# Obtém o id bolinha_fruits
bolinha_fruits_id = id(bolinha_fruits)

# Mostra o id de bolinha_fruits
print(id(bolinha_fruits))

# Mostra a contagen de referência fruits
print(sys.getrefcount(fruits))

# Obtem id fruits para para objeto Python
object_info = ctypes.cast(bolinha_fruits_id, ctypes.py_object).value

# Mostra a informação do objeto
print(object_info)

import graphviz
from graphviz import Graph

# !pip install objgraph

import objgraph

# !pip install xdot

fruit = 'Banana'

bolinha_fruits = ['Morango', 'Abacaxi', 'Cereja', fruit, [fruits], [fruits]]

objgraph.show_refs([bolinha_fruits], filename='other_fruit5.png')