class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
        self.vecinos = []

    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)

    def dfs(self, r): #checar si nodo r está en el conjunto de los vertices para iniciar
        if r in self.vertices:
            self.vertices[r].visitado = True

            for nodo in self.vertices[r].vecinos: #recorrer cada vecino del vertice r
                if self.vertices[nodo].visitado == False: #revisar si vertice nodo no ha sido visitado
                    self.vertices[nodo].padre = r
                    print("(" + str(nodo) + ", " + str (r) + ")") #escribir el nodo y r 
                    self.dfs(nodo)

def main():
    g = Grafica()

    l = [1,2,3,4,5,6]
    for v in l:
        g.agregaVertice(v)

    l = [1,2,1,5,2,3,2,5,3,4,4,5,4,6]
    for i in range(0, len(l) -1, 2):
        g.agregarArista(l[i], l[i+1]) #crear aristas

        print("(1, NULL)") #revisar que no tiene padre
        g.dfs(1)

main()

    



        