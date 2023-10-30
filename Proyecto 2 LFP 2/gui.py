import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from analizador_lexico_sintactico import *
from tkinter import messagebox
import webbrowser
import graphviz

tokens = []
errores = []
dot = graphviz.Digraph(comment='Arbol de derivacion')

def cargar_archivo():
    try:
        archivo = filedialog.askopenfilename(filetypes=[("Bizdata", "*.bizdata")])
        if archivo:
            with open(archivo, 'r') as archivo:
                contenido = archivo.read()
            area_texto.delete("1.0", tk.END)
            area_texto.insert("1.0", contenido)
    except Exception as e:
        print(e)

def analizar_archivo():
    global tokens, errores, dot
    # Se limpia dot
    dot = graphviz.Digraph(comment='Arbol de derivacion')
    parent = dot.node('parent', 'Arbol de derivacion')
    matriz = None
    tokens, errores = analizador_lexico(area_texto.get("1.0", tk.END))
    consola.configure(state=tk.NORMAL)
    consola.delete("1.0", tk.END)

    if len (errores) == 0:
        errores_registros = True
        #Paso 1, buscar la definicion de claves y registros
        try:
            errores_comentarios = eliminar_comentarios(tokens, errores)

            if errores_comentarios == False:
                consola.insert("1.0", "Errores encontrados: " + str(len(errores)) + "\n")
                for error in errores:
                    consola.insert("1.0", "Tipo del error: " + str(error.tipo) + " || Fila: " + str(error.fila) + " || Columna: " + str(error.columna) + " || Valor: " + str(error.expresion) + "\n")
                    return        
                
            resultado = analizar_claves(tokens, errores, dot = dot, parent = parent)

            if resultado is not None:
                matriz, contador_claves = resultado
                errores_registros = analizar_registros(tokens, errores, matriz, contador_claves, dot = dot, parent = parent)
                    

            if errores_registros == False:
                consola.insert("1.0", "Errores encontrados: " + str(len(errores)) + "\n")
                for error in errores:
                    consola.insert("1.0", "Tipo del error: " + str(error.tipo) + " || Fila: " + str(error.fila) + " || Columna: " + str(error.columna) + " || Valor: " + str(error.expresion) + "\n")
                    return
            
            #Paso 2, buscar la definicion de funciones
            if matriz == None:
                matriz = []

            resultado = analizar_cuerpo(tokens, errores, consola, matriz, dot = dot, parent = parent)

            if resultado == False:
                consola.insert("1.0", "Errores encontrados: " + str(len(errores)) + "\n")
                for error in errores:
                    consola.insert("1.0", "Tipo del error: " + str(error.tipo) + " || Fila: " + str(error.fila) + " || Columna: " + str(error.columna) + " || Valor: " + str(error.expresion) + "\n")
                    return
            
            #Imprimimos errores
            for error in errores:
                print("Tipo del error: " + str(error.tipo) + " || Fila: " + str(error.fila) + " || Columna: " + str(error.columna) + " || Valor: " + str(error.expresion) + "\n")
                

        except Exception as e:
            print(e)
            consola.insert("1.0", "Errores encontrados: " + str(len(errores)) + "\n")
            for error in errores:
                consola.insert("1.0", "Tipo del error: " + str(error.tipo) + " || Fila: " + str(error.fila) + " || Columna: " + str(error.columna) + " || Valor: " + str(error.expresion) + "\n")
                return 
    else:
        # Mostrar errores después
        consola.insert("1.0", "Errores encontrados: " + str(len(errores)) + "\n")
        for error in errores:
            consola.insert("1.0", "Tipo del error: " + str(error.tipo) + " || Fila: " + str(error.fila) + " || Columna: " + str(error.columna) + " || Valor: " + str(error.expresion) + "\n")
        
        consola.configure(state=tk.DISABLED)


    

def generar_reporte_tokens():
    tokens, errores = analizador_lexico(area_texto.get("1.0", tk.END))
    #Generamos un archivo html que contenga una tabla con los tokens encontrados, las columnas serán: No., tipo, lexema, fila, columna
    #Se debe abrir el archivo html en el navegador
    try:
        archivo = open("ReporteTokens.html", "w")
        archivo.write("<!DOCTYPE html>\n")
        archivo.write("<html>\n")
        archivo.write("<head>\n")
        archivo.write("<title>Reporte de Tokens</title>\n")
        archivo.write("<link rel=\"stylesheet\" href=\"style.css\">\n")
        archivo.write("</head>\n")
        archivo.write("<body>\n")
        archivo.write("<h1>Reporte de Tokens</h1>\n")
        archivo.write("<table border=\"1\">\n")
        archivo.write("<tr>\n")
        archivo.write("<th>No.</th>\n")
        archivo.write("<th>Tipo</th>\n")
        archivo.write("<th>Lexema</th>\n")
        archivo.write("<th>Fila</th>\n")
        archivo.write("<th>Columna</th>\n")
        archivo.write("</tr>\n")

        contador = 1
        for token in tokens:
            archivo.write("<tr>\n")
            archivo.write("<td>" + str(contador) + "</td>\n")
            archivo.write("<td>" + str(token.tipo) + "</td>\n")
            archivo.write("<td>" + str(token.valor) + "</td>\n")
            archivo.write("<td>" + str(token.fila) + "</td>\n")
            archivo.write("<td>" + str(token.columna) + "</td>\n")
            archivo.write("</tr>\n")
            contador += 1

        archivo.write("</table>\n")
        archivo.write("</body>\n")
        archivo.write("</html>\n")
        archivo.close()
        webbrowser.open_new_tab("ReporteTokens.html")

    except Exception as e:
        print(e)


def generar_reporte_errores():
    global tokens, errores
    #Generamos un archivo html que contenga una tabla con los errores encontrados, las columnas serán: No., tipo, expresion, fila, columna
    #Se debe abrir el archivo html en el navegador
    try:
        archivo = open("ReporteErrores.html", "w")
        archivo.write("<!DOCTYPE html>\n")
        archivo.write("<html>\n")
        archivo.write("<head>\n")
        archivo.write("<title>Reporte de Errores</title>\n")
        archivo.write("<link rel=\"stylesheet\" href=\"style.css\">\n")
        archivo.write("</head>\n")
        archivo.write("<body>\n")
        archivo.write("<h1>Reporte de Errores</h1>\n")
        archivo.write("<table border=\"1\">\n")
        archivo.write("<tr>\n")
        archivo.write("<th>No.</th>\n")
        archivo.write("<th>Tipo</th>\n")
        archivo.write("<th>Expresión</th>\n")
        archivo.write("<th>Fila</th>\n")
        archivo.write("<th>Columna</th>\n")
        archivo.write("</tr>\n")

        contador = 1
        for error in errores:
            archivo.write("<tr>\n")
            archivo.write("<td>" + str(contador) + "</td>\n")
            archivo.write("<td>" + str(error.tipo) + "</td>\n")
            archivo.write("<td>" + str(error.expresion) + "</td>\n")
            archivo.write("<td>" + str(error.fila) + "</td>\n")
            archivo.write("<td>" + str(error.columna) + "</td>\n")
            archivo.write("</tr>\n")
            contador += 1

        archivo.write("</table>\n")
        archivo.write("</body>\n")
        archivo.write("</html>\n")
        archivo.close()
        webbrowser.open_new_tab("ReporteErrores.html")

    except Exception as e:
        print(e)

def generar_arbol_derivacion():
    global dot
    try:
        dot.render('ArbolDerivacion.gv', view=True, format='png')
    except Exception as e:
        print(e)
    # Implementa la lógica para generar el árbol de derivación

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Código Bizdata")
ventana.geometry("800x600")  # Establece el tamaño de la ventana

# Crear un estilo para los elementos
style = ttk.Style()
style.configure('TButton', font=("Arial", 12), padding=10)
style.configure('TLabel', font=("Arial", 12), padding=10)
style.configure('TText', font=("Courier New", 12))

# Botón para cargar archivo
boton_cargar = ttk.Button(ventana, text="Cargar archivo", command=cargar_archivo)
boton_cargar.grid(row=0, column=0, padx=20, pady=10)

# Botón para analizar archivo
boton_analizar = ttk.Button(ventana, text="Analizar archivo", command=analizar_archivo)
boton_analizar.grid(row=0, column=1, padx=0, pady=10)

# Área de texto para visualizar/modificar el código Bizdata
area_texto = tk.Text(ventana, wrap="word", width=96, height=20)
area_texto.grid(row=1, column=0, columnspan=2, padx=10, pady=0)


# Área de consola
consola = tk.Text(ventana, wrap="word", state=tk.DISABLED, width=96, height=10)
consola.configure(bg="#edede9", fg="#2b2d42")
consola.grid(row=3, column=0, columnspan=2, padx=10, pady=15)

# Menú Reportes
menu_reportes = tk.Menu(ventana)
ventana.config(menu=menu_reportes)

reportes_menu = tk.Menu(menu_reportes)
menu_reportes.add_cascade(label="Reportes", menu=reportes_menu)
reportes_menu.add_command(label="Reporte de Tokens", command=generar_reporte_tokens)
reportes_menu.add_command(label="Reporte de Errores", command=generar_reporte_errores)
reportes_menu.add_command(label="Árbol de Derivación", command=generar_arbol_derivacion)

# Iniciar la aplicación
ventana.mainloop()
