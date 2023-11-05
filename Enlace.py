class Enlace:

    def __init__(self, NodoSalida,nodoLlegada,Peso):

        self.NodoSalida=NodoSalida;
        self.NodoLlegada=nodoLlegada;
        self.peso=Peso;

    def __str__(self):
        return f'nodo inicial del enlace: {self.NodoSalida} --> nodo final del enlace: {self.NodoLlegada} -->costo del enlace {self.peso}'       
