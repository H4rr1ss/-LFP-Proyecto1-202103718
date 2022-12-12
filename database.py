from afd import *
import tkinter.messagebox as MB

class Database():
    def __init__(self):
        self.lista_AFD = []

#-------------------------------------------------MODULO AFD-------------------------------------------------|
# (CREAR AFD)
    def __validaciones_alfabeto(self, lista_alfabeto, lista_estados):
        ''' || Verifica que el alfabeto ingresado ningun simbolo se repita 2 veces ||'''
        for h in lista_alfabeto:
            if lista_alfabeto.count(h) > 1:
                return False

            for a in lista_estados:
                if h == a:
                    return False
        return True

    def __validaciones_estadoInicial(self, estados, estadoInicial):
        '''|| Verifica que el estado inicial ingresado exista en la lista de estados ||'''
        for estado in estados:
            if estado == estadoInicial:
                return True
        return False

    def __validaciones_estadosAceptacion(self, estados, estadosAceptacion):
        '''|| Verifica que todos los estados de aceptación ingresados existan en la lista de estados ||'''
        for e_aceptacion in estadosAceptacion:

            confirmacion = False

            for estado in estados:
                if e_aceptacion == estado:
                    confirmacion = True
                    break
            
            if confirmacion is False:
                return False
                
        return True

    def __validaciones_transiciones(self, lista_transiciones):
        for transicion1 in lista_transiciones:
            contador = 0

            for transicion2 in lista_transiciones:

                if transicion1[0:3] == transicion2[0:3]:
                    contador += 1

            if contador == 2:
                return False

        return True

    def crear_ObjAFD(self, nombre, estados, alfabeto, estadosAceptacion, transiciones, estadoInicial):
        estados_ = estados.split(";")
        alfabeto_ = alfabeto.split(";")
        estadosAceptacion_ = estadosAceptacion.split(";")
        transiciones_ = transiciones.split(";")

        # VALIDACIONES----------|
        if not self.__validaciones_alfabeto(alfabeto_, estados_):
            MB.showerror(message="por favor, revise el alfabeto.", title="Error")
            return 0

        if not self.__validaciones_estadoInicial(estados_, estadoInicial):
            MB.showerror(message="por favor, coloque un estado valido.", title="Error")
            return 0
            
        if not self.__validaciones_estadosAceptacion(estados_, estadosAceptacion_):
            MB.showerror(message="por favor, ingrese un estado existente.", title="Error")
            return 0

        if not self.__validaciones_transiciones(transiciones_):
            MB.showerror(message="por favor, verifique sus transiciones.", title="Error")
            return 0
        # -----------------------|

        # CREACION OBJETOS DE AFD'S
        transiciones__ = []
        for t in transiciones_:
            t = t.split(",")
            transiciones__.append(Transicion(t[0], t[1], t[2]))

        automata = Automata(nombre, estados_, alfabeto_, estadoInicial, estadosAceptacion_, transiciones__)
        self.lista_AFD.append(automata)
        
        MB.showinfo(message="Se agrego correctamente!", title="AFD guardado")

# (EVALUAR CADENA)

#------------------------------------------------------------------------------------------------------------|



#-------------------------------------------------MODULO CARGAR ARCHIVO AFD-------------------------------------------------|     

    def leerArchivo(self, texto):
        listaAFDS = []
        listaAux = []
        listaTransiciones = []

        listaString = str(list(map(str.strip, texto)))
        listaConvertida = eval(listaString)
        
        for linea in listaConvertida:
            if linea == '%':
                listaAux.append(listaTransiciones)
                listaAFDS.append(listaAux)
                listaAux = []
                listaTransiciones = []
                continue

            if len(listaAux) > 4:
                # Empiezan las transiciones
                listaTransiciones.append(linea)
                continue

            listaAux.append(linea)

        # VERIFICACIONES --------------------------------------------------------------------------------------------
        i = 1
        for afd in listaAFDS:
            estados_ = afd[1].split(",")
            alfabeto_ = afd[2].split(",")
            estadosAceptacion_ = afd[4].split(",")

            # VALIDACIONES----------|
            if not self.__validaciones_alfabeto(alfabeto_, estados_):
                MB.showerror(message = f"por favor, revise el alfabeto del AFD {i}", title="Error")
                i += 1
                continue

            if not self.__validaciones_estadoInicial(estados_, afd[3]):
                MB.showerror(message = f"por favor, coloque un estado válido en el AFD {i}", title="Error")
                i += 1
                continue

            if not self.__validaciones_estadosAceptacion(estados_, estadosAceptacion_):
                MB.showerror(message = f"por favor, ingrese un estado existente en el AFD {i}", title="Error")
                i += 1
                continue
            
            transicionesAFD = []
            for transicion in range(len(afd[5])):
                t = afd[5][transicion].split(",") # t = contiene lista ['origen', 'simbolo;destino']
                sd = t[1].split(';') # sd = Contiene lista ['simbolo', 'destino']
                transicionesAFD.append(f'{t[0]}, {sd[0]}, {sd[1]}')

            if not self.__validaciones_transiciones(transicionesAFD):
                MB.showerror(message = f"por favor, verifique sus transiciones del AFD {i}", title="Error")
                i += 1
                continue
            # -----------------------|

            transiciones_ = []
            for t in transicionesAFD:
                t = t.split(",")
                transiciones_.append(Transicion(t[0], t[1], t[2]))

            automata = Automata(afd[0], estados_, alfabeto_, afd[3], estadosAceptacion_, transiciones_)
            self.lista_AFD.append(automata)
            i += 1
            
#---------------------------------------------------------------------------------------------------------------------------|
DB = Database()

'''
transiciones_ = []
            l = []
            for transicion in range(len(afd[5])):
                t = afd[5][transicion].split(",") # t = contiene lista ['origen', 'simbolo;destino']
                sd = t[1].split(';') # sd = Contiene lista ['simbolo', 'destino']

                if not self.__validaciones_transiciones(transiciones_):
                    MB.showerror(message = f"por favor, verifique sus transiciones del AFD {i}", title="Error")
                    i += 1
                    continue
                l.append(f'{t[0]}, {sd[0]}, {sd[1]}')
                transiciones_.append(Transicion(t[0], sd[0], sd[1]))

            automata = Automata(afd[0], estados_, alfabeto_, afd[3], estadosAceptacion_, transiciones_)
            self.lista_AFD.append(automata)
            i += 1
'''