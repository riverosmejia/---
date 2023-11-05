
from Enlace import Enlace

class Grafo:
    
    def __init__(self):

        self.nodosList = {};
        self.aristasList = [];

    def AgregarNodo(self,nodo):

        self.nodosList[nodo.id]=nodo;

    def agregarArista(self, nodoSalida, nodoLlegada, peso):
        
        if nodoLlegada.id in self.nodosList and nodoSalida.id in self.nodosList:
            
            enlace = Enlace(nodoSalida, nodoLlegada, peso);
            
            self.aristasList.append(enlace);

    def generarListaAdyacencia(self):

        lista_adyacencia = {}

        for nodo in self.nodosList.values():

            lista_adyacencia[nodo.id] = []

        for arista in self.aristasList:

            lista_adyacencia[arista.NodoSalida.id].append((arista.NodoLlegada.id, arista.peso))

        return lista_adyacencia

    def generarMatrizAdyacencia(self):
        num_nodos = len(self.nodosList)

        matriz_adyacencia = []
        for _ in range(num_nodos+1):
            fila = [f'0 '] * (num_nodos+1)
            matriz_adyacencia.append(fila)

        for i in range(num_nodos+1):
            matriz_adyacencia[0][i]=f'{i}:'
            matriz_adyacencia[i][0]=f'{i}:'

        for arista in self.aristasList:

            nodo_salida = arista.NodoSalida

            nodo_llegada = arista.NodoLlegada

            matriz_adyacencia[nodo_salida.id][nodo_llegada.id] = f'{arista.peso} '

        return matriz_adyacencia

    def encontrar_trayectoria(self, listaAdy, inicio, destino):
        if inicio not in self.nodosList or destino not in self.nodosList:
            return None

        visitados = set()
        queue = [(inicio, [inicio])]  # Usaremos una cola de tuplas (nodo, camino)

        while queue:
            nodo_actual, camino_actual = queue.pop(0)
            visitados.add(nodo_actual)

            if nodo_actual == destino:
                # Aquí creamos una lista de nodos y enlaces en el camino
                camino_con_enlaces = []
                for i in range(len(camino_actual) - 1):
                    nodo_inicio = camino_actual[i]
                    nodo_fin = camino_actual[i + 1]
                    for arista in self.aristasList:
                        if arista.NodoSalida.id == nodo_inicio and arista.NodoLlegada.id == nodo_fin:
                            camino_con_enlaces.append((nodo_inicio, nodo_fin, arista.peso))
                return camino_con_enlaces

            adyacentes = [ady[0] for ady in listaAdy[nodo_actual] if ady[0] not in visitados]

            for adyacente in adyacentes:
                nuevo_camino = list(camino_actual)
                nuevo_camino.append(adyacente)
                queue.append((adyacente, nuevo_camino))

        return None