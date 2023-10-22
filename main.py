class TreeNode:
    def __init__(self, value):
        self.value = value
        self.hijos = []
        self.posicion = []
        self.nodoPadre = None
        self.raiz = False        


def construir(matriz, i, j, im, jm):
    if i != im and j != jm:
        nodo = TreeNode(matriz[i][j])
        nodo.posicion = [i, j]
        nodo.hijos = expandir(matriz, nodo)
        
        if len(nodo.hijos) > 0:
            costos = []
            for hijo in nodo.hijos:
                costos.append(hijo.value)
        
            menor = min(costos)
            nodoSiguiente = nodo.hijos.index(menor)
        
            nuevo_i = nodo.hijos[nodoSiguiente].posicion[0]
            nuevo_j = nodo.hijos[nodoSiguiente].posicion[1]

            construir(matriz, nuevo_i, nuevo_j, im, jm)
        else:
            print("hasta aqui llegue hpta ya queme mucha cabeza en esta mondá mañana sigo, al que le guste bien al que no tambien")
    else:
        print("meta: ", i, j)
    
    
    
    
       
#variables globales
matriz = [
    [1, 1, 3, 1, 1, 1, 1, 1],
    [1, -2, 0, 0, -2, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, -1],
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
            children.append(nodo)
    if j+1 < len(matriz[0]):
        if matriz[i][j+1] != 0:
            nodo = TreeNode(matriz[i][j+1] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i,j+1]
            nodo.nodoPadre = padre
            children.append(nodo)
    if i+1 < len(matriz):
        if matriz[i+1][j] != 0:
            nodo = TreeNode(matriz[i+1][j] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i+1,j]
            nodo.nodoPadre = padre
            children.append(nodo)
    if j-1 >= 0:
        if matriz[i][j-1] != 0:
            nodo = TreeNode(matriz[i][j-1] + #valor del movimeinto
                            matriz[i][j]) #valor del padre
            nodo.posicion = [i,j-1]
            nodo.nodoPadre = padre
            children.append(nodo)
    matriz[i][j] = 0
    return children
    

