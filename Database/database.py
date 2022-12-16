import os
import webbrowser

from fpdf import FPDF
from Database.afd import *
import tkinter.messagebox as MB

class Database():
    def __init__(self):
        self.lista_AFD = []

#--------------------------------------------------------MODULO AFD--------------------------------------------------------|
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
    def scanner(self, nombreAFD, cadena, confirmacion):
        for afd in self.lista_AFD:
            if afd.getNombre() != nombreAFD:
                continue

            estado = afd.getE_inicial()
            i = 1
            for caracter in cadena:
                
                encontrado = False
                for alfabeto, sig in afd.getTransiciones()[estado]:
                    if caracter != alfabeto:
                        continue
                    
                    estado = sig
                    encontrado = True
                    if confirmacion != '':
                        cantGraficas = self.graphviz(nombreAFD, 'SI', estado, i, alfabeto)
                        i += 1
                    break

                if not encontrado:
                    print('caracter invalido, no se puede hacer una transicion')
                    MB.showerror(message=f"caracter '{caracter}' invalido, no se puede hacer una transicion.", title="Error")
                    break
            
            if estado not in afd.getE_aceptacion():
                print('cadena invalida, no termina en el estado de aceptacion')
                MB.showinfo(message="Cadena invalida, no finalizó en el estado de aceptación.", title="Error")
            else:
                print('cadena valida')
                MB.showinfo(message=f"Cadena: {cadena}, es valida.", title="Proceso exitoso")

        print(f'\nNombre del AFD: {nombreAFD}, Cadena a evaluar: {cadena}')
        if confirmacion != '':
            return cantGraficas

# (GENERAR REPORTE)
    def graphviz(self, nombre_afd, llave, actual, cont, simbolo):
        for afd in self.lista_AFD:

            if nombre_afd != afd.getNombre():
                continue

            # -----------------------------------------------GRAFICACIÓN-----------------------------------------------
            if llave != '':
                graphviz = 'digraph Patron{ \n\n    rankdir = LR\n    layout = dot\n    node[shape = circle, width = 1, height = 1]; \n    subgraph Cluster_A{ \n    label = "' + 'Paso: '+ str(cont) + '  |  Simbolo: '+str(simbolo)+' "   \n    fontcolor ="black" \n    fontsize = 26 \n    bgcolor ="#F1DFB2" \n'
            else:
                graphviz = 'digraph Patron{ \n\n    rankdir = LR\n    layout = dot\n    node[shape = circle, width = 1, height = 1]; \n    subgraph Cluster_A{ \n    label = "' + 'Nombre: '+ afd.getNombre() + '"   \n    fontcolor ="black" \n    fontsize = 30 \n    bgcolor ="#F1DFB2" \n'
            
            for estado in afd.getEstados():
                if estado == afd.getE_inicial():
                    if estado == actual:
                        if llave != '':
                            graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled shape = cds]; \n'
                            continue

                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled shape = cds]; \n'
                    continue

                if estado in afd.getE_aceptacion():
                    if estado == actual:
                        if llave != '':
                            graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled shape = doublecircle]; \n'
                            continue

                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#D0F3E6" style = filled shape = doublecircle]; \n'
                    continue
                
                if estado == actual:
                    if llave != '':
                        graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled]; \n'
                        continue

                graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled]; \n'

            # .....................CONEXION DE NODOS.......................|
            for E_origen in afd.getTransiciones():
                listEstado = afd.getTransiciones().get(E_origen)
                
                for elemento in listEstado:
                    simbolo = elemento[0]
                    E_destino = elemento[1]
                    graphviz += f'    node{E_origen}->node{E_destino}[label = {simbolo}]\n'

            graphviz += '\n    } \n\n}'

            document = './reportes/grafica.txt'

            with open(document, 'w') as grafica:
                grafica.write(graphviz)

            if llave != '':
                jpg = f'./reportes/afd{cont}.jpg'
                os.system("dot.exe -Tjpg " + document + " -o " + jpg)
            else:
                jpg = './reportes/afd.jpg'
                os.system("dot.exe -Tjpg " + document + " -o " + jpg)

            if llave != '':
                return cont

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
            pdf.image("./reportes/afd.jpg", x = 15, y = 100)
            pdf.image("./archivosEntrada/logo.png", x = 270, y = 9, w = 22, h = 22)

            pdf.set_font('Arial', '', 15)
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

            pdf.output(f"./reportes/ReporteAFD__{afd.getNombre()}.pdf")
            MB.showinfo(message="Se genero correctamente.", title="Reporte creado")
            break

    def rutaPDF(self, afds, cadena, nombreAFD):
        pdf = FPDF(orientation = "L", unit = "mm", format = "A4")
    
        for i in range(afds):
            pdf.add_page()
            pdf.image(f"./reportes/afd{str(i+1)}.jpg", x = 8, y = 50)
            pdf.set_font('Arial', '', 21)
            pdf.text(x=80, y=18, txt=f'Cadena que se esta validando: {cadena}')
            pdf.image("./archivosEntrada/logo.png", x = 260, y = 11, w = 22, h = 22)
        pdf.output(f"./reportes/ReporteRutaAFD__{nombreAFD}.pdf")

        ##### ERRORR ##########
        for i in range(afds):
            os.remove(f"./reportes/afd{i+1}.jpg")
#---------------------------------------------------------------------------------------------------------------------------|




#---------------------------------------------------------MODULO GR---------------------------------------------------------|
# (CREAR GR)
    def __validaciones_NoTerminales(self, noTerminales):
        for N_terminal in noTerminales:
            if noTerminales.count(N_terminal) > 1:
                return False, N_terminal
        return True, ''

    def __validaciones_terminales(self, noTerminales, terminales):
        for h in terminales:
            if terminales.count(h) > 1:
                return False

            for a in noTerminales:
                if h == a:
                    return False
        return True

    def __validaciones_noTerminalInicial(self, noTerminales, noTerminalInicial):
        for N_terminal in noTerminales:
            if N_terminal == noTerminalInicial:
                return True
        return False

    def __validaciones_terminalYnoTerminal(self, noTerminalInicial, terminal, noTerminal, listaTerminales, listaNoTerminales):
        if (terminal in listaTerminales) and (noTerminal in listaNoTerminales) and (noTerminalInicial in listaNoTerminales):
            return True
        return False

    def crear_ObjGR(self, nombre, noTerminales, terminales, noTerminalInicial, producciones):
        noTerminales_ = noTerminales.split(';')
        terminales_ = terminales.split(';')
        producciones_ = producciones.split(';')

        # VALIDACIONES----------|
        val, N_terminal = self.__validaciones_NoTerminales(noTerminales_)
        if not val:
            MB.showerror(message=f"El No Terminal {N_terminal} se repite 2 veces, ingreselo 1 vez.", title="Error")
            return 0

        if not self.__validaciones_terminales(noTerminales_, terminales_):
            MB.showerror(message='Por favor, revise sus terminales.', title="Error")
            return 0

        if not self.__validaciones_noTerminalInicial(noTerminales_, noTerminalInicial):
            MB.showerror(message='El no terminal inicial ingresado no existe.', title="Error")
            return 0
        # ----------------------|

        producciones__ = {}
        estadosAceptacion_ = []
        for p in producciones_:
            p = p.split('>') # ['A', '0B']
            
            # RECONOCEDOR DE ESTADOS DE ACEPTACION
            if p[1] == '$':
                if not self.__validaciones_noTerminalInicial(noTerminales_, p[0]):
                    MB.showerror(message='El "no terminal" de aceptacion no existe', title="Error")
                    return 0
                estadosAceptacion_.append(p[0])
                continue

            # VERIFICACION SI SE AGREGA OTRA TRANSICION A UNA LLAVE EXISTENTE
            if not self.__validaciones_terminalYnoTerminal(p[0], p[1][0], p[1][1], terminales_, noTerminales_):
                MB.showerror(message='Por favor, revise sus terminales y noTerminales\nen cada produccion', title="Error")
                return 0

            if p[0] in producciones__:
                entrada = (f'{p[1][0]}', f'{p[1][1]}')
                producciones__[f'{p[0]}'].append(entrada)
                continue
            
            producciones__[f'{p[0]}'] = [(f'{p[1][0]}', f'{p[1][1]}')]

        automata = Automata(nombre, noTerminales_, terminales_, noTerminalInicial, estadosAceptacion_, producciones__)
        self.lista_AFD.append(automata)
        
        MB.showinfo(message="Se agrego correctamente!", title="GRAMATICA cargada")

# (EVALUAR CADENA)

# (GENERAR REPORTE)
    def graphvizGR(self, nombre_gr, llave, actual, cont, simbolo):
        for afd in self.lista_AFD:

            if nombre_gr != afd.getNombre():
                continue

            graphviz = 'digraph Patron{ \n\n    rankdir = LR\n    layout = dot\n    node[shape = circle, width = 1, height = 1]; \n    subgraph Cluster_A{ \n    label = "' + 'Nombre: '+ afd.getNombre() + '"   \n    fontcolor ="black" \n    fontsize = 30 \n    bgcolor ="#F1DFB2" \n'

            for estado in afd.getEstados():
                if estado == afd.getE_inicial():
                    if estado == actual:
                        if llave != '':
                            graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled shape = cds]; \n'
                            continue

                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled shape = cds]; \n'
                    continue

                if estado in afd.getE_aceptacion():
                    if estado == actual:
                        if llave != '':
                            graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled shape = doublecircle]; \n'
                            continue

                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#D0F3E6" style = filled shape = doublecircle]; \n'
                    continue
                
                if estado == actual:
                    if llave != '':
                        graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled]; \n'
                        continue

                graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled]; \n'

            # .....................CONEXION DE NODOS.......................|
            for E_origen in afd.getTransiciones():
                listEstado = afd.getTransiciones().get(E_origen)
                
                for elemento in listEstado:
                    simbolo = elemento[0]
                    E_destino = elemento[1]
                    graphviz += f'    node{E_origen}->node{E_destino}[label = {simbolo}]\n'

            graphviz += '\n    } \n\n}'

            document = './reportes/graficaGR.txt'

            with open(document, 'w') as grafica:
                grafica.write(graphviz)

            if llave != '':
                jpg = f'./reportes/gr{cont}.jpg'
                os.system(f"dot.exe -Tjpg {document} -o {jpg}")
            else:
                jpg = './reportes/gr.jpg'
                os.system(f"dot.exe -Tjpg {document} -o {jpg}")

            if llave != '':
                return cont

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
            pdf.image("./reportes/gr.jpg", x = 15, y = 100)
            pdf.image("./archivosEntrada/logo.png", x = 270, y = 7, w = 22, h = 22)

            pdf.set_font('Arial', '', 12)
            pdf.text(x=65, y=10, txt=f'No terminales: {afd.getEstados()}')
            pdf.text(x=65, y=30, txt=f'Terminales: {afd.getAlfabeto()}')
            pdf.text(x=65, y=50, txt=f'No terminal inicial: {afd.getE_inicial()}')
            pdf.text(x=65, y=70, txt=f'Cadena minima válida: {cadena}')
            pdf.text(x=170, y=10, txt='Producciones:')

            posY = 20
            for EstadoOrigen in newDiccionario:
                listEstadoo = newDiccionario.get(EstadoOrigen)
                suma = 0
                for element in listEstadoo:

                    if len(listEstadoo) == suma:
                        pdf.text(x=183, y=posY, txt=f' | {element[0]} {element[1]}')
                        posY += 8
                        continue

                    pdf.text(x=173, y=posY, txt=f'{EstadoOrigen} > {element[0]} {element[1]}')
                    suma += 2
                    posY += 8

            pdf.output(f"./reportes/ReporteGR__{afd.getNombre()}.pdf")
            MB.showinfo(message="Se genero correctamente.", title="Reporte creado")
            break
#---------------------------------------------------------------------------------------------------------------------------|




#-------------------------------------------------MODULO CARGAR ARCHIVO AFD-------------------------------------------------|     
# (LEER ARCHIVO AFD)
    def leerArchivo(self, texto):
        listaAFDS = []
        listaAux = []
        listaTransiciones = []

        newText = str(texto).replace(' ', '')

        listaString = str(list(map(str.strip, eval(newText))))
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
        return True

# (LEER ARCHIVO GR)
    def leerArchivoGR(self, texto):
        listaAFDS = []
        listaAux = []
        listaProducciones = []
        estadosAceptacion = []

        # Quitar espacios y saltos de linea
        newText = str(texto).replace(' ', '')
        listaString = str(list(map(str.strip, eval(newText))))
        listaConvertida = eval(listaString)
        
        for linea in listaConvertida:
            if linea == '%':
                listaAux.append(listaProducciones)
                listaAux.append(estadosAceptacion)
                listaAFDS.append(listaAux)
                listaAux = []
                listaProducciones = []
                continue

            if len(listaAux) > 3:
                # Empiezan las producciones
                if linea[2] == '$':
                    estadosAceptacion.append(linea[0])
                    continue

                listaProducciones.append(linea)
                continue

            listaAux.append(linea)
        
        # VERIFICACIONES --------------------------------------------------------------------------------------------
        i = 1
        for afd in listaAFDS:
            noTerminales = afd[1].split(",")
            terminales = afd[2].split(",")

            # VALIDACIONES----------|
            val, N_terminal = self.__validaciones_NoTerminales(noTerminales)
            if not val:
                MB.showerror(message=f"El No Terminal {N_terminal} se repite 2 veces en la gramatica {i}, ingreselo 1 vez.", title="Error")
                i += 1
                continue

            if not self.__validaciones_terminales(noTerminales, terminales):
                MB.showerror(message=f'Por favor, revise sus terminales de la gramatica {i}.', title="Error")
                i += 1
                continue

            if not self.__validaciones_noTerminalInicial(noTerminales, afd[3]):
                MB.showerror(message=f'El no terminal inicial ingresado no existe en la gramatica {i}.', title="Error")
                i += 1
                continue
        
            for p in afd[4]:
                if not self.__validaciones_terminalYnoTerminal(p[0], p[2], p[3], afd[2], afd[1]):
                    MB.showerror(message=f'Por favor, revise sus terminales y noTerminales\nen las producciones de la gramatica {i}', title="Error")
                    i += 1
                    continue
            # ----------------------|
            
            producciones_ = {}
            for t in afd[4]:
                t = t.split(">")

                if t[0] in producciones_: # A>0B
                    entrada = (f'{t[1][0]}', f'{t[1][1]}')
                    producciones_[f'{t[0]}'].append(entrada)
                    continue

                producciones_[f'{t[0]}'] = [(f'{t[1][0]}', f'{t[1][1]}')]

            automata = Automata(afd[0], noTerminales, terminales, afd[3], afd[5], producciones_)
            self.lista_AFD.append(automata)
            i += 1

        MB.showinfo(message="Se agrego correctamente!", title="AFD guardado")
        return True
#---------------------------------------------------------------------------------------------------------------------------|
DB = Database()