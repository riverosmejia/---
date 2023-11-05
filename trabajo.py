from Enlace import Enlace
from Nodo import Nodo
from grafo import Grafo

def limpiar_pantalla():
    print("\n" * 100)

if __name__ == "__main__":

    sistema=Grafo();

    nodo_1 = Nodo(1)
    sistema.AgregarNodo(nodo_1)
    nodo_2 = Nodo(2)
    sistema.AgregarNodo(nodo_2)
    nodo_3 = Nodo(3)
    sistema.AgregarNodo(nodo_3)
    nodo_4 = Nodo(4)
    sistema.AgregarNodo(nodo_4)
    nodo_5 = Nodo(5)
    sistema.AgregarNodo(nodo_5)
    nodo_6 = Nodo(6)
    sistema.AgregarNodo(nodo_6)
    nodo_7 = Nodo(7)
    sistema.AgregarNodo(nodo_7)

    sistema.agregarArista(nodo_1,nodo_3,3)
    sistema.agregarArista(nodo_1,nodo_4,4)
    sistema.agregarArista(nodo_1,nodo_5,1)
    sistema.agregarArista(nodo_2,nodo_1,2)
    sistema.agregarArista(nodo_2,nodo_3,2)
    sistema.agregarArista(nodo_3,nodo_1,2)
    sistema.agregarArista(nodo_3,nodo_2,4)
    sistema.agregarArista(nodo_3,nodo_5,2)
    sistema.agregarArista(nodo_3,nodo_6,3)
    sistema.agregarArista(nodo_4,nodo_1,1)
    sistema.agregarArista(nodo_4,nodo_3,1)
    sistema.agregarArista(nodo_4,nodo_6,1)
    sistema.agregarArista(nodo_5,nodo_3,1)
    sistema.agregarArista(nodo_5,nodo_7,1)
    sistema.agregarArista(nodo_6,nodo_4,2)
    sistema.agregarArista(nodo_6,nodo_7,2)
    sistema.agregarArista(nodo_7,nodo_6,1)    

    #lista Adyacencia

    listaAdy=sistema.generarListaAdyacencia()

    matriz_adyacencia = sistema.generarMatrizAdyacencia()

    terminar=False

    while terminar is not True:

        print("\n\n<---------------------------------------------->\n\n")
    
        resp = input("1.Lista de adyacencia\n2.Matriz de adyacencia\n3.camino más corto dentre 'a' y 'b'\n4.terminar programa\nR/=")

        if resp =='1':

            for nodo_id,ady in listaAdy.items():

                print(f'nodo:{nodo_id}, {ady}')

            #Fin lista Adyacencia

            input("\npresione ENTER para continuar")

        elif resp=='2':

            for fila in matriz_adyacencia:

                print(f'{fila}')

            input("\npresione Enter para continuar")

        elif resp=='3':

            numero1 = int(input("Introduce el id del nodo de salida: "))
            
            numero2 = int(input("Introduce el id del nodo de llegada: "))

            camino_mas_corto = sistema.encontrar_trayectoria(listaAdy,numero1, numero2)

            print(f'\nel camino entre el nodo {numero1} y el nodo {numero2} necesita {len(camino_mas_corto)} enlaces:')

            for nodo_inicio, nodo_fin, peso in camino_mas_corto:
                
                print(f'(nodo {nodo_inicio}, nodo {nodo_fin}, (peso {peso}))')
        
            input("\npresione ENTER para continuar")

        elif resp=='4':

            print("Vuelva Pronto, presiona ENTER para terminar el programa")

            input()

            terminar=True

        else:

            print(f"la respuesta {resp} no se encuentra dentro del rango 1-4")
