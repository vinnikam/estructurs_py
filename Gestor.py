from Persona import Persona

class Gestor:
    listaPersonas = []
    listaPersonasOrden = []
    
    def insertar(self, persona):
        self.listaPersonas.append(persona)

    def imprimir(self):
        for obj in self.listaPersonas:
            print( obj.nombre, obj.identificacion, sep =' ' )

    def imprimirOrdenado(self):
        for obj in self.listaPersonasOrden:
            print( obj.nombre, obj.identificacion, sep =' ' )

    def bubbleSort(self):
        self.listaPersonasOrden = self.listaPersonas
        n = len(self.listaPersonasOrden)
    
        for i in range(n):
    
            for j in range(0, n-i-1):
    
                if self.listaPersonasOrden[j].identificacion > self.listaPersonasOrden[j+1].identificacion:
                    self.listaPersonasOrden[j], self.listaPersonasOrden[j+1] = self.listaPersonasOrden[j+1], self.listaPersonasOrden[j]            
