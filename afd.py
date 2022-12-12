class Automata:
    def __init__(self, nombre, estados, alfabeto, estadoInicial, estadosAceptacion, transiciones):
        self.nombre = nombre 
        self.estados = estados
        self.alfabeto = alfabeto
        self.estadoInicial = estadoInicial
        self.estadosAceptacion = estadosAceptacion
        self.transiciones = transiciones

    def getNombre(self):
        return self.nombre

class Transicion:
    def __init__(self, origen, simboloEntrada, destino):
        self.origen = origen
        self.simboloEntrada = simboloEntrada
        self.destino = destino
        