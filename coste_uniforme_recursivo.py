class TreeNode:
    def __init__(self, cost, position, padre):
        self.cost = cost
        self.hijos = []
        self.position = position
        self.nodoPadre = padre
        self.raiz = False
        self.completo = False
        
    #comparamos la posicion de un nodo para saber si ya llegamos a la meta
    def is_goal(self, meta):
        if self.position[0] == meta[0] and self.position[1] == meta[1]:
            return True
        return False
    
    #verificamos si al expandir tengo hijos, si no tengo hijos ya estoy completo
    def i_have_childrens(self):
        if not self.hijos:
            self.completo = True
            return False
        return True
    
    def get_recorrido(self):
        if self is None:
            return
        nodos_recorridos = [self]
        coordenadas = [self.position]
        while not self.raiz:
            nodos_recorridos.append(self.nodoPadre)
            coordenadas.append(self.nodoPadre.position)
            self = self.nodoPadre
        return nodos_recorridos, coordenadas
    
    def mi_hijo_es_el_mejor(self, nodo):
        for hijo in self.hijos:
            if nodo == hijo:
                return True
            break
        return False
    
#variables globales
nodos_creados = []
costo_nodos_menor_a_mayor = []
raiz = TreeNode(0, [2,7], None)
    
def construir(matriz, nodo, meta):
    if nodo is None:
        return
    
    if nodo.is_goal(meta):
        _, coordenadas = nodo.get_recorrido() #si llegamos a la meta retorno las coordenadas para recorrer la matriz
        return coordenadas
    if nodo.raiz:
        nodos_creados.append(nodo) #para que se agregue una vez
        
    #si no es meta expando el nodo
    nodo.hijos = expandir(matriz, nodo)
    if not nodo.i_have_childrens(): #si no tengo hijos es porque ya no hay recorrido entonces cambio de nodo
        nodos_ordenados = organizar_nodos_desde_nodo(raiz)
        mi_recorrido, _ = nodo.get_recorrido()
        nodo_siguiente = get_best_node(mi_recorrido, nodos_ordenados)
        construir(matriz, nodo_siguiente[0], meta)
    
    for hijo in nodo.hijos:
        nodos_creados.append(hijo)
        
    nodos_ordenados = organizar_nodos_desde_nodo(raiz)
    mi_recorrido, _ = nodo.get_recorrido()
    nodo_siguiente = get_best_node(mi_recorrido, nodos_ordenados)
    
    if nodo.mi_hijo_es_el_mejor(nodo_siguiente[0]):
        construir(matriz, nodo_siguiente[0], meta)
    
    acomodar_arbol() #por definir
    construir(matriz, nodo_siguiente[0], meta)
    
        
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
    nodos.sort(key=lambda nodo: nodo.valor)  # Organiza la lista de nodos de menor a mayor
    return nodos   

#retorna una lista con los valores de nodos_creados_ordenados sin los valores de mi_recorrido
def get_best_node(mi_recorrido, nodos_creados_ordenados):
    nueva_lista = [valor 
                   for valor in nodos_creados_ordenados
                   if valor not in mi_recorrido]
    return nueva_lista
    
#retorna los hijos de un nodo
def expandir(matriz, padre):
    children = []
    i = padre.posicion[0]
    j = padre.posicion[1]
    costo_acumulado = matriz[i][j]
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

