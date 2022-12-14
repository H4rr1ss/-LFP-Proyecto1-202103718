import os
import webbrowser

from fpdf import FPDF
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
        transiciones__ = {}
        for t in transiciones_:
            t = t.split(",")

            if t[0] in transiciones__:
                entrada = (f'{t[1]}', f'{t[2]}')
                transiciones_[f'{t[0]}'].append(entrada)
                continue

            transiciones__[f'{t[0]}'] = [(f'{t[1]}', f'{t[2]}')]

        automata = Automata(nombre, estados_, alfabeto_, estadoInicial, estadosAceptacion_, transiciones__)
        self.lista_AFD.append(automata)
        
        MB.showinfo(message="Se agrego correctamente!", title="AFD guardado")

# (EVALUAR CADENA)
    def scanner(self, nombreAFD, cadena):
        for afd in self.lista_AFD:
            if afd.getNombre() != nombreAFD:
                continue

            estado = afd.getE_inicial()

            for caracter in cadena:
                
                encontrado = False
                for alfabeto, sig in afd.getTransiciones()[estado]:
                    if caracter != alfabeto:
                        continue
                    estado = sig
                    encontrado = True
                    break

                if not encontrado:
                    print('caracter invalido, no se puede hacer una transicion')
                    break
            
            if estado not in afd.getE_aceptacion():
                print('cadena invalida, no termina en el estado de aceptacion')
            else:
                print('cadena valida')

        print(f'\nNombre del AFD: {nombreAFD}, Cadena a evaluar: {cadena}')

# (GENERAR REPORTE)
    def graphviz(self, nombre_afd):
        for afd in self.lista_AFD:

            if nombre_afd != afd.getNombre():
                continue

            # -----------------------------------------------GRAFICACIÓN-----------------------------------------------
            i = 1
            graphviz = 'digraph Patron{ \n\n    rankdir = LR\n    layout = dot\n    node[shape = circle, width = 1, height = 1]; \n    subgraph Cluster_A{ \n    label = "' + 'Nombre: '+ afd.getNombre() + '"   \n    fontcolor ="black" \n    fontsize = 30 \n    bgcolor ="#F1DFB2" \n'
            
            for estado in afd.getEstados():
                if estado == afd.getE_inicial():
                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled shape = cds]; \n'
                    i += 1
                    continue

                if estado in afd.getE_aceptacion():
                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#D0F3E6" style = filled shape = doublecircle]; \n'
                    i += 1
                    continue

                graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled]; \n'
                i += 1

            # .....................CONEXION DE NODOS.......................|
            for E_origen in afd.getTransiciones():
                listEstado = afd.getTransiciones().get(E_origen)
                
                for elemento in listEstado:
                    simbolo = elemento[0]
                    E_destino = elemento[1]
                    graphviz += f'    node{E_origen}->node{E_destino}[label = {simbolo}]\n'

            graphviz += '\n    } \n\n}'

            document = 'grafica' + '.txt'

            with open(document, 'w') as grafica:
                grafica.write(graphviz)

            jpg = 'afd.jpg'
            os.system("dot.exe -Tjpg " + document + " -o " + jpg)

            # .....................GENERACION DE CADENA MINIMA VALIDA.......................|
            keys = afd.getTransiciones().keys()
            sorted_keys = sorted(keys)

            newDiccionario = {}
            for key in sorted_keys:
                newDiccionario[key] = afd.getTransiciones()[key]

            cadena = ''
            for m in newDiccionario:
                listaEstado = afd.getTransiciones().get(m)
                for e in listaEstado:
                    cadena += e[0]

            # .....................GENERACION DEL PDF(REPORTE).......................|
            pdf = FPDF(orientation = "L", unit = "mm", format = "A4")
    
            pdf.add_page()
            pdf.image("afd.jpg", x = 15, y = 100)
            pdf.image("logo.png", x = 240, y = 11, w = 22, h = 22)

            pdf.set_font('Arial', '', 16)
            pdf.text(x=80, y=10, txt=f'Estados: {afd.getEstados()}')
            pdf.text(x=80, y=20, txt=f'Alfabeto: {afd.getAlfabeto()}')
            pdf.text(x=80, y=30, txt=f'Estados de aceptacion: {afd.getE_aceptacion()}')
            pdf.text(x=80, y=50, txt=f'Estado inicial: {afd.getE_inicial()}')
            pdf.text(x=80, y=60, txt=f'Cadena válida: {cadena}')
            pdf.text(x=170, y=10, txt='Transiciones:')

            posY = 20
            for EstadoOrigen in afd.getTransiciones():
                listEstadoo = afd.getTransiciones().get(EstadoOrigen)
                
                for element in listEstadoo:
                    pdf.text(x=173, y=posY, txt=f'{EstadoOrigen},{element[0]};{element[1]}')
                    posY += 10

            pdf.output(f"Reporte_{afd.getNombre()}" + ".pdf")
            break
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
                transicionesAFD.append(f'{t[0]},{sd[0]},{sd[1]}')

            if not self.__validaciones_transiciones(transicionesAFD):
                MB.showerror(message = f"por favor, verifique sus transiciones del AFD {i}", title="Error")
                i += 1
                continue
            # -----------------------|

            transiciones_ = {}
            for t in transicionesAFD:
                t = t.split(",")

                if t[0] in transiciones_:
                    entrada = (f'{t[1]}', f'{t[2]}')
                    transiciones_[f'{t[0]}'].append(entrada)
                    continue

                transiciones_[f'{t[0]}'] = [(f'{t[1]}', f'{t[2]}')]
            
            automata = Automata(afd[0], estados_, alfabeto_, afd[3], estadosAceptacion_, transiciones_)
            self.lista_AFD.append(automata)
            i += 1

        MB.showinfo(message="Se agrego correctamente!", title="AFD guardado")

#---------------------------------------------------------------------------------------------------------------------------|
DB = Database()