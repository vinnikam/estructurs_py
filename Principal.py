from Persona import Persona
from Gestor import Gestor

def main():
    print(" Iniciando programa")
    persona1 = Persona(12, "Jascin")
    print (persona1.identificacion)

    elgestor = Gestor()
    elgestor.insertar(Persona(20, "Josef"))
    elgestor.insertar(Persona(14, "Luisa"))
    elgestor.insertar(Persona(9, "Manuel"))
    elgestor.insertar(Persona(5, "Julian"))
    elgestor.insertar(Persona(31, "Camilo"))
    print ("Normal ------")
    elgestor.imprimir()
    elgestor.bubbleSort()
    print ("Ordenado ------")
    elgestor.imprimirOrdenado()


if __name__ == "__main__":
    main()