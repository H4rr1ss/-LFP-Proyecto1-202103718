from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Tk
import tkinter
import tkinter.messagebox as MB
from Database.database import DB

#https://github.com/DiiAns23/LFP_VACACIONES_2022/tree/master/Proyecto1

class Menu():
    def __init__(self):
        self.General_ventana()
        self.ventana.title("Menú Principal")
        self.centrar(self.ventana, 600, 365)
        self.ventana.geometry("600x350")
        self.Ventana_frame()

    def General_ventana(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)

    def centrar(self, ventana, ancho, alto):
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        x = (ancho_pantalla//2) - (ancho//2)
        y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{x}+{y}")
    
    def ir_pantalla_menu(self):
        self.ventana.destroy()
        Menu()        
    
    def __ir_pantalla_AFD(self):
        self.ventana.destroy()
        AFD()

    def __ir_pantalla_GR(self):
        self.ventana.destroy()
        GR()

    def __ir_pantalla_CargarArchivoss(self):
        self.ventana.destroy()
        CargarArchivos()

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "580", height = "330", relief = "ridge", bd = 12)

        # LABELS-----
        Label(self.frame, text = "Lenguajes Formales y de Programación Sección N", bg = "#F9E1BE", font = ("Comic Sans MS", 16)).place(x = 25, y = 20)

        Label(self.frame, text = "Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12)).place(x = 80, y = 100)

        Label(self.frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12)).place(x = 80, y = 140)

        # BUTTON-----
        Button(self.frame, text = "Módulo AFD", command = self.__ir_pantalla_AFD, width = 18, height = 2, font = ("Arial", 11), bg = "#D5A273").place(x = 335, y = 80)

        Button(self.frame, text = "Módulo GR", command = self.__ir_pantalla_GR, width = 18, height = 2, font = ("Arial", 11), bg = "#D5A273").place(x = 335, y = 155)

        Button(self.frame, text = "Cargar Archivos", command = self.__ir_pantalla_CargarArchivoss, width = 18, height = 2, font = ("Arial", 11), bg = "#D5A273").place(x = 335, y = 230)

        Button(self.frame, text = "Salir", command = self.ventana.quit, width = 10, height = 2, font = ("Arial", 11), bg = "#E7C09C").place(x = 115, y = 215)
        
        self.frame.mainloop()  





#................................................................MODULO ADF.....................................................
class AFD(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Módulo AFD")
        super().centrar(self.ventana, 320, 330)
        self.ventana.geometry("320x310")# ANCHO X LARGO
        self.Ventana_frame() 
    
    def __ir_pantalla_CrearAFD(self):
        self.ventana.destroy()
        crearAFD()
        
    def __ir_pantalla_EvaluarCadena(self):
        self.ventana.destroy()
        EvaluarCadena()

    def __ayuda(self):
        self.ventana.destroy()
        ayudaAFD()

    def __GenerarReporte(self):
        try:
            DB.graphviz(nombreAFD, '', '', '', '')
        except:
            MB.showwarning(message="Seleccione un AFD para gráficar", title="ERROR")

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "325", height = "315", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_crearAFD = Button(self.frame, text = "Crear AFD", command = self.__ir_pantalla_CrearAFD, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_crearAFD.place(x = 20, y = 31)

        self.__btn_EvaluarCadena = Button(self.frame, text = "Evaluar Cadena", command = self.__ir_pantalla_EvaluarCadena, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_EvaluarCadena.place(x = 20, y = 102)

        self.__btn_GenerarReporte = Button(self.frame, text = "Generar Reporte", command = self.__GenerarReporte, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_GenerarReporte.place(x = 20, y = 173)

        self.__btn_Regresar = Button(self.frame, text = "Salir", command = super().ir_pantalla_menu, width = 9, height = 8, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Regresar.place(x = 172, y = 24)
        self.__btn_Ayuda = Button(self.frame, text = "Ayuda", command = self.__ayuda, width = 9, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Ayuda.place(x = 172, y = 165)

        self.frame.mainloop()

###################################################################
class crearAFD(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Crear AFD")
        super().centrar(self.ventana, 390, 380)
        self.ventana.geometry("390x360")# ANCHO X LARGO
        self.Ventana_frame()   

    def ir_pantalla_menuAFD(self):
        self.ventana.destroy()
        AFD()      

    def __crearAFD(self):
        DB.crear_ObjAFD(self.__tb_nombre.get(), self.__tb_estados.get().replace(' ', ''), self.__tb_alfabeto.get().replace(' ', ''), self.__tb_estadosAceptacion.get().replace(' ', ''), self.__tb_transiciones.get().replace(' ', ''), self.__tb_estadoInicial.get())

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "380", height = "350", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 3)
        Label(self.frame, text = "Estados:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 55)
        Label(self.frame, text = "Alfabeto:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 109)
        Label(self.frame, text = "Estados de aceptación:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 161)
        Label(self.frame, text = "Transiciones:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 213)
        Label(self.frame, text = "Estado Inicial:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 200, y = 3)

        # JTEXFIELD------
        self.__tb_nombre = Entry(self.frame, font = ("Comic Sans MS", 10), width = 16, justify = "center")
        self.__tb_nombre.place(x = 15, y = 23)
        self.__tb_estados= Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_estados.place(x = 15, y = 75)
        self.__tb_alfabeto = Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_alfabeto.place(x = 15, y = 129)
        self.__tb_estadosAceptacion = Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_estadosAceptacion.place(x = 15, y = 181)
        self.__tb_transiciones = Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_transiciones.place(x = 15, y = 233)
        self.__tb_estadoInicial = Entry(self.frame, font = ("Comic Sans MS", 10), width = 9, justify = "center")
        self.__tb_estadoInicial.place(x = 207, y = 23)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_menuAFD, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 165, y = 266)
        self.__btn_Aceptar = Button(self.frame, text = "Aceptar", command = self.__crearAFD, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Aceptar.place(x = 83, y = 266)

        self.frame.mainloop()

###################################################################
class EvaluarCadena(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Evaluar Cadena")
        super().centrar(self.ventana, 390, 320)
        self.ventana.geometry("390x300")# ANCHO X LARGO
        self.Ventana_frame()   

    def __ir_pantalla_menuAFD(self):
        self.ventana.destroy()
        AFD()      

    def funtionsCombo(self, event):
        var = event.widget.get()
        global nombreAFD
        nombreAFD = var

    def __evaluarCadena(self):
        try:
            cadena = self.__tb_validar.get()
            ruta = self.__tb_ruta.get()

            if cadena == '' and ruta == '':
                MB.showwarning(message="No ha ingresado nada para evaluar.", title="Revise los campos de texto")
                return 

            if cadena != '' and ruta == '':
                DB.scanner(nombreAFD, cadena, '')
                return 
            elif ruta != '' and cadena == '':
                listAcept, cantAFDs = DB.scanner(nombreAFD, ruta, 'si')
                DB.rutaPDF(cantAFDs, ruta, nombreAFD, listAcept)
                return 0
            else:
                MB.showwarning(message="Por favor, rellene un solo campo.", title="Revise los campos de texto")
        except:
            MB.showerror(message="Por favor, elija un AFD.", title="ERROR")

    def __listaAFDS(self):
        try:
            listaAux = []
            for i in DB.lista_AFD:
                listaAux.append(i.getNombre())

            # MENU DE AFD'S
            reports = ttk.Combobox(self.frame, width=18, height=5, values = listaAux, state='readonly')
            reports.place(x = 100, y = 45)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus AFD.", title="Carga de archivos")
            
    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "390", height = "320", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "Solo Validar:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 86)
        Label(self.frame, text = "Ruta:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 190, y = 86)


        # JTEXFIELD------
        self.__tb_validar = Entry(self.frame, font = ("Comic Sans MS", 10), width = 17, justify = "center")
        self.__tb_validar.place(x = 11, y = 110)
        self.__tb_ruta = Entry(self.frame, font = ("Comic Sans MS", 10), width = 17, justify = "center")
        self.__tb_ruta.place(x = 186, y = 110)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menuAFD, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 135, y = 200)
        self.__btn_SoloValidar = Button(self.frame, text = "Evaluar", command = self.__evaluarCadena, width = 8, height = 1, font = ("Arial", 8), bg = "#E7C09C")
        self.__btn_SoloValidar.place(x = 45, y = 140)
        self.__btn_ValidarConRuta = Button(self.frame, text = "Evaluar", command = self.__evaluarCadena, width = 8, height = 1, font = ("Arial", 8), bg = "#E7C09C")
        self.__btn_ValidarConRuta.place(x = 228, y = 140)
        self.__btn_MostrarAFD = Button(self.frame, text = "Mostrar AFD'S", command = self.__listaAFDS, width = 12, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_MostrarAFD.place(x = 117, y = 10)

        self.frame.mainloop()

class ayudaAFD(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Ayuda AFD")
        super().centrar(self.ventana, 540, 420)
        self.ventana.geometry("540x400")# ANCHO X LARGO
        self.Ventana_frame()  

    def __ir_pantalla_menuAFD(self):
        self.ventana.destroy()
        AFD()      

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "540", height = "390", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "¿Qué es un automata finito determinista?", bg = "#F9E1BE", font = ("Comic Sans MS", 12)).place(x = 95, y = 3)
        Label(self.frame, text = "Un AFD tiene un conjunto finito de estados y un conjunto \nfinito de símbolos de entrada. El término “determinista” hace \nreferencia al hecho de que para cada entrada sólo existe uno y \nsólo un estado al que el autómata puede hacer la transición \na partir de su estado actual.", bg = "#F9E1BE", font = ("Comic Sans MS", 11)).place(x = 18, y = 35)

        img = tkinter.PhotoImage(file = './imas/AFD.png', width=267, height=156)
        lbl_img = tkinter.Label(self.frame, image=img)
        lbl_img.place(x = 105, y = 144)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command=self.__ir_pantalla_menuAFD, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 210, y = 311)

        self.frame.mainloop()


#...............................................................MODULO GR...................................................
class GR(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Módulo GR")
        super().centrar(self.ventana, 320, 330)
        self.ventana.geometry("320x310")# ANCHO X LARGO
        self.Ventana_frame() 
    
    def __ir_pantalla_CrearGR(self):
        self.ventana.destroy()
        crearGR()
        
    def __ir_pantalla_EvaluarCadena(self):
        self.ventana.destroy()
        EvaluarCadenaGR()

    def __ir_pantalla_ayudaGR(self):
        self.ventana.destroy()
        ayudaGR()

    def __GenerarReporteGR(self):
        try:
            DB.graphvizGR(nombreAFD, '', '', '', '')
        except:
            MB.showwarning(message="Seleccione una gramatica para gráficar", title="ERROR")
        
    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "325", height = "315", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_crearAFD = Button(self.frame, text = "Crear GR", command = self.__ir_pantalla_CrearGR, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_crearAFD.place(x = 20, y = 31)

        self.__btn_EvaluarCadena = Button(self.frame, text = "Evaluar Cadena", command = self.__ir_pantalla_EvaluarCadena, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_EvaluarCadena.place(x = 20, y = 102)

        self.__btn_GenerarReporte = Button(self.frame, text = "Generar Reporte", command = self.__GenerarReporteGR, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_GenerarReporte.place(x = 20, y = 173)

        self.__btn_Regresar = Button(self.frame, text = "Salir", command = super().ir_pantalla_menu, width = 9, height = 8, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Regresar.place(x = 172, y = 24)

        self.__btn_Ayuda = Button(self.frame, text = "Ayuda", command = self.__ir_pantalla_ayudaGR, width = 9, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Ayuda.place(x = 172, y = 165)

        self.frame.mainloop()

###################################################################
class crearGR(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Crear GR")
        super().centrar(self.ventana, 390, 325)
        self.ventana.geometry("390x305")# ANCHO X LARGO
        self.Ventana_frame()   

    def ir_pantalla_menuGR(self):
        self.ventana.destroy()
        GR()      

    def __crearGR(self):
        DB.crear_ObjGR(self.__tb_nombreGR.get(), self.__tb_noTerminales.get().replace(' ', ''), self.__tb_terminales.get().replace(' ', ''), self.__tb_noTerminalInicial.get(), self.__tb_producciones.get().replace(' ', ''))

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "380", height = "295", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "Nombre:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 3)
        Label(self.frame, text = "No Terminales:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 55)
        Label(self.frame, text = "Terminales:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 109)
        Label(self.frame, text = "Producciones:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 161)
        Label(self.frame, text = "No terminal inicial:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 193, y = 3)

        # JTEXFIELD------
        self.__tb_nombreGR = Entry(self.frame, font = ("Comic Sans MS", 10), width = 16, justify = "center")
        self.__tb_nombreGR.place(x = 15, y = 23)
        self.__tb_noTerminales= Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_noTerminales.place(x = 15, y = 75)
        self.__tb_terminales = Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_terminales.place(x = 15, y = 129)
        self.__tb_producciones = Entry(self.frame, font = ("Comic Sans MS", 10), width = 35, justify = "center")
        self.__tb_producciones.place(x = 15, y = 181)
        self.__tb_noTerminalInicial = Entry(self.frame, font = ("Comic Sans MS", 10), width = 10, justify = "center")
        self.__tb_noTerminalInicial.place(x = 205, y = 23)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command = self.ir_pantalla_menuGR, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 167, y = 215)
        self.__btn_Aceptar = Button(self.frame, text = "Aceptar", command = self.__crearGR, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Aceptar.place(x = 85, y = 215)

        self.frame.mainloop()

###################################################################
class EvaluarCadenaGR(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Evaluar Cadena")
        super().centrar(self.ventana, 390, 320)
        self.ventana.geometry("390x300")# ANCHO X LARGO
        self.Ventana_frame()   

    def __ir_pantalla_menuGR(self):
        self.ventana.destroy()
        GR()      

    def __evaluarCadena(self):
        try:
            cadena = self.__tb_validar.get()
            ruta = self.__tb_ruta.get()

            if cadena == '' and ruta == '':
                MB.showwarning(message="No ha ingresado nada para evaluar.", title="Revise los campos de texto")
                return 

            if cadena != '' and ruta == '':
                DB.scanner(nombreAFD, cadena, '')
                return 0
            elif ruta != '' and cadena == '':
                listAceptacion, cantAFDs = DB.scanner(nombreAFD, ruta, 'si')
                DB.rutaPDF(cantAFDs, ruta, nombreAFD, listAceptacion)
                return 0
            else:
                MB.showwarning(message="Por favor, rellene un solo campo.", title="Revise los campos de texto")
        except:
            MB.showerror(message="Por favor, elija un AFD.", title="ERROR")

    def funtionsCombo(self, event):
        var = event.widget.get()
        global nombreAFD
        nombreAFD = var

    def __listaGRS(self):
        try:
            listaAux = []
            for i in DB.lista_AFD:
                listaAux.append(i.getNombre())

            # MENU DE GRAMATICAS
            reports = ttk.Combobox(self.frame, width=18, height=5, values = listaAux, state='readonly')
            reports.place(x = 100, y = 45)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus gramaticas.", title="Carga de archivos")
            
    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "390", height = "320", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "Solo Validar:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 86)
        Label(self.frame, text = "Ruta:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 190, y = 86)

        # JTEXFIELD------
        self.__tb_validar = Entry(self.frame, font = ("Comic Sans MS", 10), width = 17, justify = "center")
        self.__tb_validar.place(x = 11, y = 110)
        self.__tb_ruta= Entry(self.frame, font = ("Comic Sans MS", 10), width = 17, justify = "center")
        self.__tb_ruta.place(x = 186, y = 110)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menuGR, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 135, y = 200)
        self.__btn_SoloValidar = Button(self.frame, text = "Evaluar", command = self.__evaluarCadena, width = 8, height = 1, font = ("Arial", 8), bg = "#E7C09C")
        self.__btn_SoloValidar.place(x = 45, y = 140)
        self.__btn_ValidarConRuta = Button(self.frame, text = "Evaluar", command = self.__evaluarCadena, width = 8, height = 1, font = ("Arial", 8), bg = "#E7C09C")
        self.__btn_ValidarConRuta.place(x = 228, y = 140)
        self.__btn_MostrarAFD = Button(self.frame, text = "Mostrar GR'S", command = self.__listaGRS, width = 12, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_MostrarAFD.place(x = 117, y = 10)

        self.frame.mainloop()

class ayudaGR(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Ayuda GR")
        super().centrar(self.ventana, 540, 420)
        self.ventana.geometry("540x400")# ANCHO X LARGO
        self.Ventana_frame()  

    def __ir_pantalla_menuGR(self):
        self.ventana.destroy()
        GR()      

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "540", height = "390", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "¿Qué es una grámatica regular?", bg = "#F9E1BE", font = ("Comic Sans MS", 12)).place(x = 133, y = 3)
        Label(self.frame, text = "Generan los lenguajes regulares (aquellos reconocidos por un \nautómata finito). Son las gramáticas más restrictivas. El lado \nderecho de una producción debe contener un símbolo terminal\n y, como máximo, un símbolo no terminal", bg = "#F9E1BE", font = ("Comic Sans MS", 11)).place(x = 22, y = 35)

        img = tkinter.PhotoImage(file = './imas/GR.png', width=267, height=158)
        lbl_img = tkinter.Label(self.frame, image=img)
        lbl_img.place(x = 105, y = 135)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command=self.__ir_pantalla_menuGR, width = 8, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 210, y = 308)

        self.frame.mainloop()

#.........................................................CARGAR ARCHIVOS...............................................
class CargarArchivos(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Cargar Archivos")
        super().centrar(self.ventana, 300, 190)
        self.ventana.geometry("300x170")# ANCHO X LARGO
        self.Ventana_frame() 
    
    def __cargarArchivo(self):
        try:
            Tk().withdraw()
            archivo = filedialog.askopenfilename(title = 'Select content image', filetypes= [('Archivo AFD', '*.afd'), ('Archivo GR', '*.gre')])

            with open(archivo, 'r', encoding='utf-8') as file:

                texto = file.readlines()
                
                if texto == '':
                    MB.showerror('aviso', 'No existe datos en el archivo que ha seleccionado')
                    return 0
                
                numerofila = archivo.find('.gre')
                ext = archivo[numerofila:numerofila+4]

                if ext == '':
                    conf = DB.leerArchivo(texto)
                    if conf != 0:
                        self.ventana.destroy()
                        EvaluarCadena() 

                else:
                    conf = DB.leerArchivoGR(texto)
                    if conf != 0:
                        self.ventana.destroy()
                        print(DB.lista_AFD)
                        EvaluarCadenaGR() 
        except:
            MB.showerror('Error', 'No ha cargado ningun archivo, por favor vuelva a internarlo')

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "305", height = "175", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_cargarAFD = Button(self.frame, text = "Cargar archivo", command = self.__cargarArchivo, width = 15, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_cargarAFD.place(x = 10, y = 25)

        self.__btn_Regresar = Button(self.frame, text = "Salir", command = super().ir_pantalla_menu, width = 8, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Regresar.place(x = 158, y = 25)

        self.frame.mainloop()

Menu()