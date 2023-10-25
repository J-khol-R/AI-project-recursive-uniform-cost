class TreeNode:
    def __init__(self, value):
        self.value = value
        self.hijos = []
        self.posicion = []
        self.nodoPadre = None
        self.nodosComparar = []
        self.raiz = True             
        
        
def construir(matriz, nodo, im, jm):
    i = nodo.posicion[0]
    j = nodo.posicion[1]
    
    if i != im and j != jm:  #preguntar si es meta
        # nodo = TreeNode(matriz[i][j])
        # nodo.posicion = [i, j]
        nodo.hijos = expandir(matriz, nodo)
        
        if len(nodo.hijos) > 0: #pregunta si tuvo hijos
            nodo.nodosComparar.extend(nodo.hijos)
            costos = []
            for nodoComparar in nodo.nodosComparar:
                costos.append(nodoComparar.value)
        
            menor = min(costos)
            lugar_menor = costos.index(menor)
            nodoSiguiente = nodo.nodosComparar.index(lugar_menor) 
        
            # nuevo_i = nodo.hijos[nodoSiguiente].posicion[0]
            # nuevo_j = nodo.hijos[nodoSiguiente].posicion[1]

            construir(matriz, nuevo_i, nuevo_j, im, jm)
        else: #pregunta si tengo hermanos
            print("hasta aqui llegue hpta ya queme mucha cabeza en esta mondá mañana sigo, al que le guste bien al que no tambien")
    else:
        print("meta: ", i, j, "codto:", )
        return nodo
    
    
    
    
       
#variables globales
matriz = [
    [1, 1, 3, 1, 1, 1, 1, 1],
    [1, -2, 0, 0, -2, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, -2, 1, 3, 1, 1, 1, 1],
]
 
#expenade el nodo i,j de una matriz y devuelve sus hijos, si es un cero no lo añade
# ya que seria una pared (el recorrido se hace como las manecillas del reloj)
def expandir(matriz, padre):
    children = []
    i = padre.posicion[0]
    j = padre.posicion[1]
    if i-1 >= 0:
        if matriz[i-1][j] != 0:
            nodo = TreeNode(matriz[i-1][j] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i-1,j]
            nodo.nodoPadre = padre
            nodo.raiz = False
            children.append(nodo)
    if j+1 < len(matriz[0]):
        if matriz[i][j+1] != 0:
            nodo = TreeNode(matriz[i][j+1] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i,j+1]
            nodo.nodoPadre = padre
            nodo.raiz = False
            children.append(nodo)
    if i+1 < len(matriz):
        if matriz[i+1][j] != 0:
            nodo = TreeNode(matriz[i+1][j] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i+1,j]
            nodo.nodoPadre = padre
            nodo.raiz = False
            children.append(nodo)
    if j-1 >= 0:
        if matriz[i][j-1] != 0:
            nodo = TreeNode(matriz[i][j-1] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i,j-1]
            nodo.nodoPadre = padre
            nodo.raiz = False
            children.append(nodo)
    matriz[i][j] = 0
    return children
    

