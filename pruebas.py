# class NodoArbolNArio:
#     def __init__(self, valor):
#         self.valor = valor
#         self.hijos = []  # Lista de hijos

# from collections import deque  # Importa la cola desde la biblioteca collections

# lista_sin_raiz = []

# def recorrido_por_niveles(arbol):
#     if arbol is None:
#         return

#     cola = deque()
#     cola.append(arbol)  # Agrega el nodo raíz a la cola

#     while cola:
#         nodo_actual = cola.popleft()  # Saca el nodo de la cola

#         # Imprime o procesa el nodo actual
#         lista_sin_raiz.append(nodo_actual.valor)
#         print(nodo_actual.valor, end=' ')

#         # Agrega los hijos del nodo actual a la cola
#         for hijo in nodo_actual.hijos:
#             cola.append(hijo)

# # Crear un árbol n-ario
# raiz = NodoArbolNArio(1)
# raiz.hijos.append(NodoArbolNArio(2))
# raiz.hijos.append(NodoArbolNArio(3))
# raiz.hijos[0].hijos.append(NodoArbolNArio(4))
# raiz.hijos[0].hijos.append(NodoArbolNArio(5))
# raiz.hijos[1].hijos.append(NodoArbolNArio(6))
# raiz.hijos[1].hijos.append(NodoArbolNArio(7))

# # Realizar el recorrido por niveles
# print("Recorrido por Niveles:")
# recorrido_por_niveles(raiz)
# print("lista sin raiz:")
# print(lista_sin_raiz)

# class NodoArbolNArio:
#     def __init__(self, valor):
#         self.valor = valor
#         self.hijos = []

# def recorrer_hacia_arriba(nodo, nivel, lista_nodos, nodo_menor_valor):
#     if nodo is None:
#         return

#     if len(lista_nodos) <= nivel:
#         lista_nodos.append([])

#     lista_nodos[nivel].append(nodo)

#     if nodo.valor < nodo_menor_valor[0]:
#         nodo_menor_valor[0] = nodo.valor

#     for hijo in nodo.hijos:
#         recorrer_hacia_arriba(hijo, nivel + 1, lista_nodos, nodo_menor_valor)

# # Ejemplo de uso
# raiz = NodoArbolNArio(10)
# raiz.hijos.extend([NodoArbolNArio(5), NodoArbolNArio(15)])
# raiz.hijos[0].hijos.extend([NodoArbolNArio(3), NodoArbolNArio(7)])
# raiz.hijos[1].hijos.extend([NodoArbolNArio(12), NodoArbolNArio(18)])

# nodo_menor_valor = [float('inf')]
# lista_nodos = []
# recorrer_hacia_arriba(raiz, 0, lista_nodos, nodo_menor_valor)

# print("Nodo con el valor más bajo:", nodo_menor_valor[0])

# class NodoArbolNArio:
#     def __init__(self, valor):
#         self.valor = valor
#         self.hijos = []

# def recorrer_hacia_arriba_con_nodo(nodo, nivel, lista_nodos, nodo_menor_valor):
#     if nodo is None:
#         return

#     if len(lista_nodos) <= nivel:
#         lista_nodos.append([])

#     lista_nodos[nivel].append(nodo)

#     if nodo.valor < nodo_menor_valor[0].valor:
#         nodo_menor_valor[0] = nodo

#     for hijo in nodo.hijos:
#         recorrer_hacia_arriba_con_nodo(hijo, nivel + 1, lista_nodos, nodo_menor_valor)

# # Ejemplo de uso
# raiz = NodoArbolNArio(10)
# raiz.hijos.extend([NodoArbolNArio(5), NodoArbolNArio(15)])
# raiz.hijos[0].hijos.extend([NodoArbolNArio(3), NodoArbolNArio(7)])
# raiz.hijos[1].hijos.extend([NodoArbolNArio(12), NodoArbolNArio(18)])

# nodo_menor_valor = [NodoArbolNArio(float('inf'))]
# lista_nodos = []
# recorrer_hacia_arriba_con_nodo(raiz, 0, lista_nodos, nodo_menor_valor)

# print("Nodo con el valor más bajo:", nodo_menor_valor[0].valor)

# lista = [1,2,3]
# print(lista.count(4))
# verificar si el objeto existe en la lista = objeto in lista_objetos

class NodoArbolNArio:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def organizar_valores_desde_nodo(nodo):
    # Realiza un recorrido DFS para recoger todos los valores en una lista
    def recorrido_dfs(nodo, valores):
        if nodo is None:
            return
        valores.append(nodo.valor)
        for hijo in nodo.hijos:
            recorrido_dfs(hijo, valores)

    valores = []
    recorrido_dfs(nodo, valores)
    valores.sort()  # Organiza la lista de valores de menor a mayor
    return valores

# Ejemplo de uso
raiz = NodoArbolNArio(10)
raiz.hijos.extend([NodoArbolNArio(5), NodoArbolNArio(15)])
raiz.hijos[0].hijos.extend([NodoArbolNArio(3), NodoArbolNArio(7)])
raiz.hijos[1].hijos.extend([NodoArbolNArio(12), NodoArbolNArio(18)])

nodo_actual = raiz.hijos[1].hijos[0]  # Supongamos que estamos en el nodo raíz
valores_organizados = organizar_valores_desde_nodo(nodo_actual)

# print("Valores organizados de menor a mayor:", valores_organizados)

lista_A = [2, 4, 6]
lista_B = [1, 2, 3, 4, 5]

# Crear una nueva lista que excluye los valores de A
nueva_lista = [valor for valor in lista_B if valor not in lista_A]

# Imprimir la nueva lista
print(nueva_lista)



