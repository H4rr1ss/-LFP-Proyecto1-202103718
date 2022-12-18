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
    
    #------------------------------------
    def getEstados(self):
        return self.estados

    def getAlfabeto(self):
        return self.alfabeto

    def getE_inicial(self):
        return self.estadoInicial

    def getE_aceptacion(self):
        return self.estadosAceptacion

    def getTransiciones(self):
        return self.transiciones