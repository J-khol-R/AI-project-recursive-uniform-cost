import copy

class TreeNode:
    def __init__(self, cost, position, padre):
        self.cost = cost
        self.hijos = []
        self.position = position
        self.nodoPadre = padre
        self.raiz = False
        self.cambiado = False
        self.posicion_anterior_de_mi_padre = None
        self.completo = False
        self.matriz = matriz
        
    #comparamos la posicion de un nodo para saber si ya llegamos a la meta
    def is_goal(self, meta):
        if self.position[0] == meta[0] and self.position[1] == meta[1]:
            return True
        return False
    
    #verificamos si al expandir tengo hijos, si no tengo hijos ya estoy completo
    def i_have_childrens(self):
        if not self.hijos:
            # self.completo = True
            return False
        return True
    
    #obtienen los nodos y coordenadas de donde pasó
    def get_recorrido(self):
        if self is None:
            return nodos_recorridos, coordenadas
        nodos_recorridos = [self]
        coordenadas = [self.position]
        while not self.raiz:
            nodos_recorridos.append(self.nodoPadre)
            coordenadas.append(self.nodoPadre.position)
            self = self.nodoPadre
        coordenadas.reverse()
        return nodos_recorridos, coordenadas
    
    #pregunta si mi hijo es el menor para ver si seguir por ahi o cambiar de nodo
    def mi_hijo_es_el_mejor(self, nodo):
        for hijo in self.hijos:
            if nodo.position == hijo.position:
                return True
            break
        return False
    
    def indice_en_padre(self):
        if self.nodoPadre is not None:
            for i, hijo in enumerate(self.nodoPadre.hijos):
                if hijo is self:
                    return i
        return None
    
#construir es uns funcion recursiva que va creando el arbol y retorna las coordenadas de la matriz con menor costo
def construir(matriz, nodo, meta):
    if nodo == None:
        return "nodo vacio"
    
    if not coordenada_en_matriz(matriz, meta[0], meta[1]):
        return "la meta no existe dentro de la matriz"
    
    if matriz[meta[0]][meta[1]] == 0:
        return "nunca llegaras a la meta porque no puedes atravezar la pared"
    
    if nodo.is_goal(meta):
        _, coordenadas = nodo.get_recorrido() #si llegamos a la meta retorno las coordenadas para recorrer la matriz
        return nodo.cost, coordenadas
    
    #si no es meta expando el nodo
    # copia_matriz = copy.copy(matriz)
    # nodo.matriz = copia_matriz
    _, coordenadas = nodo.get_recorrido()
    nodo.matriz = poner_en_cero_matriz(matriz, coordenadas)
    nodo.hijos = expandir(nodo.matriz, nodo)
    
    nodos_ordenados = organizar_nodos_desde_nodo(raiz)
    mi_recorrido, _ = nodo.get_recorrido()
    nodo_siguiente = get_best_node(mi_recorrido, nodos_ordenados)
    
    if not nodo.i_have_childrens(): #si no tengo hijos es porque ya no hay recorrido entonces cambio de nodo
        nodo.completo = True
        if not nodo_siguiente:
            return "es imposible llegar a la meta"
        return construir(matriz, nodo_siguiente[0], meta)
    
    if nodo.mi_hijo_es_el_mejor(nodo_siguiente[0]):
        # revisar esta parte para mandar directamente el hijo
        nodo.completo = True
        if nodo_siguiente[0].cambiado:
            revertir(nodo_siguiente[0])
        return construir(matriz, nodo_siguiente[0], meta)
    
    acomodar_arbol(nodo) #cambia la posicion del padre por su mejor hijo
    
    if nodo_siguiente[0].cambiado:
        revertir(nodo_siguiente[0])
        
    return construir(matriz, nodo_siguiente[0], meta)

def poner_en_cero_matriz(matriz, coordenadas_a_cero):
    # Crear una copia de la matriz original
    nueva_matriz = [fila[:] for fila in matriz]

    for fila, columna in coordenadas_a_cero:
        if 0 <= fila < len(nueva_matriz) and 0 <= columna < len(nueva_matriz[0]):
            nueva_matriz[fila][columna] = 0

    return nueva_matriz


    
def acomodar_arbol(nodo):
    mejor_hijo = min(nodo.hijos, key=lambda hijo: hijo.cost) #0,7
    indice_mejor_hijo = nodo.hijos.index(mejor_hijo) #0
    # if nodo.cambiado:
    #     i = nodo.nodoPadre.hijos.index(nodo)
    # else: i = nodo.nodoPadre.hijos.index(nodo)
    # print(nodo.nodoPadre.hijos)
    i = nodo.indice_en_padre()
    # print(i) 
    nodo.nodoPadre.hijos[i] = nodo.hijos[indice_mejor_hijo]
    nodo.hijos[indice_mejor_hijo].cambiado = True
    nodo.hijos[indice_mejor_hijo].posicion_anterior_de_mi_padre = i
    
def revertir(nodo):
    i = nodo.posicion_anterior_de_mi_padre
    nodo.nodoPadre.nodoPadre.hijos[i] = nodo.nodoPadre
    nodo.nodoPadre.completo = True
    
    
def recorrer_arbol_por_filas(arbol):
    if not arbol:
        return []

    # Usamos una lista como cola para recorrer por niveles
    fila_actual = [arbol]
    nodos = []

    while fila_actual:
        fila_siguiente = []

        for nodo in fila_actual:
            nodos.append(nodo)
            fila_siguiente.extend(nodo.hijos)

        fila_actual = fila_siguiente
    
    def orden_personalizado(nodo):
        return (nodo.cost, nodos.index(nodo))
    
    nodos_ordenados = sorted(nodos, key=orden_personalizado)

    return nodos_ordenados    
   
   


def organizar_nodos_desde_nodo(nodo):
    # Realiza un recorrido DFS para recoger todos los nodos en una lista
    def recorrido_dfs(nodo, nodos):
        if nodo is None:
            return
        nodos.append(nodo)
        for hijo in nodo.hijos:
            recorrido_dfs(hijo, nodos)

    nodos = []
    recorrido_dfs(nodo, nodos)
    nodos.sort(key=lambda nodo: nodo.cost)  # Organiza la lista de nodos de menor a mayor
    return nodos   

#retorna una lista con los valores de nodos_creados_ordenados sin los valores de mi_recorrido, ademas elimina los nodos que esten completos
def get_best_node(mi_recorrido, nodos_creados_ordenados):
    nueva_lista = [valor 
                   for valor in nodos_creados_ordenados
                   if valor not in mi_recorrido and not valor.completo]
    return nueva_lista


def coordenada_en_matriz(matriz, fila, columna):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])  # Suponiendo que todas las filas tienen la misma longitud

    if 0 <= fila < num_filas and 0 <= columna < num_columnas:
        return True
    else:
        return False
    
#retorna los hijos de un nodo
def expandir(matriz, padre):
    children = []
    i = padre.position[0]
    j = padre.position[1]
    costo_acumulado = padre.cost
    if i-1 >= 0:
        if matriz[i-1][j] != 0:
            nodo = TreeNode(matriz[i-1][j] + costo_acumulado, #costo acumulado
                            [i-1,j], #posicion en la matriz
                            padre) # nodo padre
            children.append(nodo)
    if j+1 < len(matriz[0]):
        if matriz[i][j+1] != 0:
            nodo = TreeNode(matriz[i][j+1] + costo_acumulado,
                            [i,j+1],
                            padre)
            children.append(nodo)
    if i+1 < len(matriz):
        if matriz[i+1][j] != 0:
            nodo = TreeNode(matriz[i+1][j] + costo_acumulado,
                            [i+1,j],
                            padre)
            children.append(nodo)
    if j-1 >= 0:
        if matriz[i][j-1] != 0:
            nodo = TreeNode(matriz[i][j-1] + costo_acumulado,
                            [i,j-1],
                            padre)
            children.append(nodo)
    matriz[i][j] = 0
    return children


#----------------------------------     PRUEBAS     ---------------------------------
matriz = [
    [1,  1,  3,  1,  1,  1, 1, 1],
    [1, -2,  0,  0, -2,  0, 0, 1],
    [1,  0,  1,  1,  1,  0, 0, 1],
    [1,  0,  1,  0,  0,  0, 1, 1],
    [1, -2,  1,  3,  1,  1, 1, 1],
]

matriz1 = [
        [1, 0,  0, 1,  1, 0, 1, 1],
        [1, 1,  1, 1,  0, 1, 3, 1],
        [0, 0, -2, 0, -2, 3, 1, 1],
        [1, 1,  1, 1, -2, 1, 1, 0],
        [1, 0,  1, 0,  1, 1, 0, 1],
]

raiz = TreeNode(0, [2,7], None)
raiz.raiz = True

dato = construir(matriz1, raiz, [3,0])
print(dato)

# print(8 < 8)

