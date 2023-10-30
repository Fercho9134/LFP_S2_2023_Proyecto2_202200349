from tokens import Tokens
from error import Error
import copy
import tkinter as tk



def analizador_lexico(entrada):
    tokens = []
    errores = []  # Lista para almacenar errores
    i = 0  # Índice para recorrer la cadena de entrada
    fila = 1
    columna = 1

    while i < len(entrada):
        char = entrada[i]

        # Reconocer espacios en blanco
        if char == ' ':
            columna += 1
            i += 1
            continue

        if char == '\t':
            columna += 1
            i += 1
            continue

        # Reconocer saltos de línea
        if char == '\n':
            fila += 1
            columna = 1
            i += 1
            continue

        # Reconocer cadenas (strings)
        if char == '"':
            token = Tokens("comillas", char, fila, columna)
            tokens.append(token)
            i += 1
            inicio = i
            while i < len(entrada) and entrada[i] != '"':
                i += 1

            if i >= len(entrada):
                errores.append(Error("No se cerraron comillas", fila, columna, entrada[inicio - 1]))
                columna += i - inicio + 1
            else:
                cadena = entrada[inicio:i].lower()
                token = Tokens("cadena", cadena, fila, columna + i - inicio)
                tokens.append(token)
                token = Tokens("comillas", "\"", fila, columna + i - inicio + 1)
                tokens.append(token)
                columna += i - inicio + 2
            i += 1
            continue

        # Reconocer números
        if char.isdigit() or (char == '-' and i + 1 < len(entrada) and entrada[i + 1].isdigit()):
            inicio = i
            i += 1
            while i < len(entrada) and (entrada[i].isdigit() or entrada[i] == '.'):
                i += 1
            token = Tokens("numero", entrada[inicio:i], fila, columna + i - inicio)
            tokens.append(token)
            columna += i - inicio
            continue

        if char == '{':
            token = Tokens("llave_abierta", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == '}':
            token = Tokens("llave_cerrada", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == '[':
            token = Tokens("corchete_abierto", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ']':
            token = Tokens("corchete_cerrado", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ':':
            token = Tokens("dos_puntos", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ',':
            token = Tokens("coma", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == '=':
            token = Tokens("igual", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ";":
            token = Tokens("punto_coma", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == "#":
            token = Tokens("numeral", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == "'":
            token = Tokens("comilla_simple", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if es_letra(char):
            inicio = i
            i += 1
            while i < len(entrada) and es_letra(entrada[i]):
                if entrada[i] == " ":
                    break
                
                i += 1
            palabra = entrada[inicio:i].lower()
            if palabra == "claves":
                token = Tokens("claves", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "registros":
                token = Tokens("registros", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "imprimir":
                token = Tokens("imprimir", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "imprimirln":
                token = Tokens("imprimirln", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "conteo":
                token = Tokens("conteo", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "promedio":
                token = Tokens("promedio", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "contarsi":
                token = Tokens("contarsi", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "datos":
                token = Tokens("datos", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "sumar":
                token = Tokens("sumar", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "max":
                token = Tokens("max", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "min": 
                token = Tokens("min", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            elif palabra == "exportarreporte":
                token = Tokens("exportarreporte", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                continue

            else:
            # se agrega como palabra generica
                token = Tokens("palabra_generica", palabra, fila, columna + i - inicio)
                tokens.append(token)
                columna += i - inicio
                print("'"+palabra+"' no es una palabra reservada")
                continue

            

        if char == "(":
            token = Tokens("parentesis_abierto", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ")":
            token = Tokens("parentesis_cerrado", char, fila, columna)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        

        # Registrar errores de tokens no reconocidos
        errores.append(Error("Error lexico", fila, columna, char))
        i += 1
        columna += 1

    return tokens, errores

def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z' or caracter == ' '

def es_letra_con_guion_bajo(caracter):
    return es_letra(caracter) or caracter == '_'


def analizar_claves(tokens, errores, dot=None, parent=None):
    i = 0
    contador_claves = 0
    matriz = []
    fila = []
    while i < len(tokens):
        if tokens[i].tipo == "claves":
            nodo_claves = f'Clave_{contador_claves}'
            dot.node(nodo_claves, f'Clave: {tokens[i].valor}')
            dot.edge("parent", nodo_claves)
            tokens.pop(i)
            if tokens[i].tipo == "igual":
                nodo_igual = f'Igual_{contador_claves}'
                dot.node(nodo_igual, 'Igual')
                dot.edge(nodo_claves, nodo_igual)
                tokens.pop(i)
                if tokens[i].tipo == "corchete_abierto":
                    nodo_corchete_abierto = f'CorcheteAbierto_{contador_claves}'
                    dot.node(nodo_corchete_abierto, 'Corchete Abierto')
                    dot.edge(nodo_igual, nodo_corchete_abierto)
                    tokens.pop(i)
                    while i<len(tokens) and tokens[i].tipo != "corchete_cerrado":
                        if tokens[i].tipo == "comillas":
                            nodo_comillas = f'ComillasI_{contador_claves}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_corchete_abierto, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "cadena":
                                nodo_cadena = f'Cadena_{contador_claves}'
                                dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                                dot.edge(nodo_corchete_abierto, nodo_cadena)
                                fila.append(tokens[i].valor)
                                contador_claves+=1
                                tokens.pop(i)
                                if tokens[i].tipo == "comillas":
                                    nodo_comillas = f'ComillasF_{contador_claves}'
                                    dot.node(nodo_comillas, 'Comillas')
                                    dot.edge(nodo_cadena, nodo_comillas)
                                    tokens.pop(i)
                                    if tokens[i].tipo == "coma" or tokens[i].tipo == "corchete_cerrado":
                                        if tokens[i].tipo == "coma":
                                            nodo_coma = f'Coma_{contador_claves}'
                                            dot.node(nodo_coma, 'Coma')
                                            dot.edge(nodo_comillas, nodo_coma)
                                            tokens.pop(i)
                                            continue
                                        elif tokens[i].tipo == "corchete_cerrado":
                                            nodo_corchete_cerrado = f'CorcheteCerrado_{contador_claves}'
                                            dot.node(nodo_corchete_cerrado, 'Corchete Cerrado')
                                            dot.edge(nodo_comillas, nodo_corchete_cerrado)
                                            tokens.pop(i)
                                            matriz.append(fila)
                                            return matriz, contador_claves
                                        
                                    else:
                                        print("Error sintactico: Se esperaba una coma o un corchete cerrado")
                                        error = Error("Error sintactico: Se esperaba una coma o un corchete cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return None, None
                                else:
                                    print("Error sintactico: Se esperaba una comilla")
                                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return None, None
                            else:
                                print("Error sintactico: Se esperaba una cadena")
                                error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                return None, None
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            return None, None
                        
                    if tokens[i].tipo == "corchete_cerrado":
                        return matriz, contador_claves
                    else:
                        print("Error sintactico: Se esperaba un corchete cerrado")
                        error = Error("Error sintactico: Se esperaba un corchete cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return None, None
                else:
                    print("Error sintactico: Se esperaba un corchete abierto")
                    error = Error("Error sintactico: Se esperaba un corchete abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return None, None
                
            else:
                print("Error sintactico: Se esperaba un signo igual")
                error = Error("Error sintactico: Se esperaba un signo igual", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return None, None
            
        else: 
            i+=1


#Funcion para eliminar los comentarios y palabra_generica de la lista de tokens
#Un comentario es cualquier cosa que este entre un numeral y un salto de linea
#Una palabra generica es cualquier palabra que no sea una palabra reservada y no sea un comentario
#Un comentario multilinea es cualquier cosa que este entre tres comillas simples al inicio y al final, todo lo que este dentro de las comillas simples se elimina
#Si hay palabras genericas y no son comentarios, se debe de mostrar un error 
#Hay que verificar que un comentario multilinea tenga su cierre, si no lo tiene, se debe de mostrar un error
def eliminar_comentarios(tokens, errores):
    i = 0
    
    while i < len(tokens):
        if tokens[i].tipo == "numeral":
            linea = tokens[i].fila
            tokens.pop(i)
            while i < len(tokens) and tokens[i].fila == linea:
                tokens.pop(i)
                if len(tokens) == 0:
                    return True

        elif tokens[i].tipo == "comilla_simple" and tokens[i+1].tipo == "comilla_simple" and tokens[i+2].tipo == "comilla_simple":
            fila_inicio = tokens[i].fila
            columna_inicio = tokens[i].columna
            token_inesperado = tokens[i].valor
            tokens.pop(i)
            tokens.pop(i)
            tokens.pop(i)
            contador_comillas_simple = 0
            while i<len(tokens) and contador_comillas_simple < 3:
                if tokens[i].tipo == "comilla_simple":
                    contador_comillas_simple+=1
                    tokens.pop(i)
                    continue
                else:
                    tokens.pop(i)
                    continue

            if contador_comillas_simple != 3:
                print("Error sintactico: Se esperaban tres comillas simples")
                error = Error("Error sintactico: No se cerró el comentario multilinea", fila_inicio, columna_inicio, token_inesperado)
                errores.append(error)
                return False
        
        elif tokens[i].tipo == "palabra_generica":
            print("Error lexico: Palabra no reconocida")
            error = Error("Error Lexico: Palabra no reconocida", tokens[i].fila, tokens[i].columna, tokens[i].valor)
            errores.append(error)
            tokens.pop(i)
        
        else:
            i+=1
    
    return True




    
def analizar_registros(tokens, errores, matriz, contador_claves, dot=None, parent=None):
    i = 0
    fila_registros = []
    contador_registros = 0
    while i < len(tokens):
        if tokens[i].tipo == "registros":
            nodo_registros = f'RegistrosR_{contador_registros}'
            dot.node(nodo_registros, f'Registros')
            dot.edge("parent", nodo_registros)
            tokens.pop(i)
            if tokens[i].tipo == "igual":
                nodo_igual = f'IgualR_{contador_registros}'
                dot.node(nodo_igual, 'Igual')
                dot.edge(nodo_registros, nodo_igual)
                tokens.pop(i)
                if tokens[i].tipo == "corchete_abierto":
                    nodo_corchete_abierto = f'CorcheteAbiertoR_{contador_registros}'
                    dot.node(nodo_corchete_abierto, 'Corchete Abierto')
                    dot.edge(nodo_igual, nodo_corchete_abierto)
                    tokens.pop(i)
                    while i<len(tokens) and tokens[i].tipo != "corchete_cerrado":
                        if tokens[i].tipo == "llave_abierta":
                            nodo_llave_abierta = f'LlaveAbiertaR_{contador_registros}'
                            dot.node(nodo_llave_abierta, 'Llave Abierta')
                            dot.edge(nodo_corchete_abierto, nodo_llave_abierta)
                            tokens.pop(i)
                            fila_registros.clear()
                            contador_registros+=1
                            for j in range(contador_claves):
                                #Estamos en el primer registro, hay dos opciones para cada registro/fila que sean cadenas entre comillas o numeros, la cantidad de elementos debe ser igual a la cantidad de claves
                                if tokens[i].tipo == "comillas":
                                    nodo_comillas = f'ComillasIR_{contador_registros}{j}'
                                    dot.node(nodo_comillas, 'Comillas')
                                    dot.edge(nodo_llave_abierta, nodo_comillas)
                                    tokens.pop(i)
                                    if tokens[i].tipo == "cadena":
                                        nodo_cadena = f'CadenaR_{contador_registros}{j}'
                                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                                        dot.edge(nodo_llave_abierta, nodo_cadena)
                                        fila_registros.append(tokens[i].valor)
                                        tokens.pop(i)

                                        if tokens[i].tipo == "comillas":
                                            nodo_comillas = f'ComillasFR_{contador_registros}{j}'
                                            dot.node(nodo_comillas, 'Comillas')
                                            dot.edge(nodo_cadena, nodo_comillas)
                                            tokens.pop(i)

                                            #Si aun no se ha llegado a la ultima clave, se espera una coma, si no se espera una llave cerrada
                                            if j < contador_claves-1:
                                                if tokens[i].tipo == "coma":
                                                    nodo_coma = f'ComaR_{contador_registros}{j}'
                                                    dot.node(nodo_coma, 'Coma')
                                                    dot.edge(nodo_comillas, nodo_coma)
                                                    tokens.pop(i)
                                                    continue
                                                else:
                                                    print("Error sintactico: Se esperaba una coma")
                                                    error = Error("Error sintactico: Se esperaba una coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                                    errores.append(error)
                                                    return False
                                            else:
                                                if tokens[i].tipo == "llave_cerrada":
                                                    tokens.pop(i)
                                                    matriz.append(copy.deepcopy(fila_registros))

                                                    break
                                                else:
                                                    print("Error sintactico: Se esperaba una llave cerrada")
                                                    error = Error("Error sintactico: Se esperaba una llave cerrada", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                                    errores.append(error)
                                                    return False
                                        else:
                                            print("Error sintactico: Se esperaba una comilla")
                                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                            errores.append(error)
                                            return False
                                    else:
                                        print("Error sintactico: Se esperaba una cadena")
                                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return False
                                    
                                        
                                elif tokens[i].tipo == "numero":
                                    fila_registros.append(tokens[i].valor)
                                    nodo_numero = f'NumeroR_{contador_registros}{j}'
                                    dot.node(nodo_numero, f'Numero: {tokens[i].valor}')
                                    dot.edge(nodo_llave_abierta, nodo_numero)
                                    tokens.pop(i)
                                    if j < contador_claves-1:
                                        if tokens[i].tipo == "coma":
                                            nodo_coma = f'ComaR_{contador_registros}{j}'
                                            dot.node(nodo_coma, 'Coma')
                                            dot.edge(nodo_numero, nodo_coma)
                                            tokens.pop(i)
                                            continue
                                        else:
                                            print("Error sintactico: Se esperaba una coma")
                                            error = Error("Error sintactico: Se esperaba una coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                            errores.append(error)
                                            return False
                                    else:
                                        if tokens[i].tipo == "llave_cerrada":
                                            nodo_llave_cerrada = f'LlaveCerradaR_{contador_registros}{j}'
                                            dot.node(nodo_llave_cerrada, 'Llave Cerrada')
                                            dot.edge(nodo_numero, nodo_llave_cerrada)
                                            tokens.pop(i)
                                            matriz.append(copy.deepcopy(fila_registros))
                                            break
                                        else:
                                            print("Error sintactico: Se esperaba una llave cerrada")
                                            error = Error("Error sintactico: Se esperaba una llave cerrada", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                            errores.append(error)
                                            return False
                                else:
                                    print("Error sintactico: Se esperaba una cadena o un numero")
                                    error = Error("Error sintactico: Se esperaba una cadena o un numero", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                        else:
                            print("Error sintactico: Se esperaba una llave abierta")
                            error = Error("Error sintactico: Se esperaba una llave abierta", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    
                    if tokens[i].tipo == "corchete_cerrado":
                        tokens.pop(i)
                        return True
                        
                else:
                    print("Error sintactico: Se esperaba un corchete abierto")
                    error = Error("Error sintactico: Se esperaba un corchete abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else: 
                print("Error sintactico: Se esperaba un signo igual")
                error = Error("Error sintactico: Se esperaba un signo igual", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
                            
        else: 
            i+=1

def analizar_cuerpo(tokens, errores, consola, matriz, dot = None, parent = None):
    #Se analizaran los tokens restantes para ver si son instrucciones validas, si no lo son, se mostrara un error, si hay simbolos inesperados, sin estar dentro de una instruccion, se almacenaran en la lista de errores, pero el analisis continuara eliminando los tokens inesperados
    i = 0
    error_encontrado_saltado = False
    instruccion_seguida = 0
    while i<len(tokens):

        #Instruccion para imprimir en la consola
        if tokens[i].tipo == "imprimir" and i<len(tokens):
            nodo_imprimir = f'ImprimirIM_{instruccion_seguida}'
            dot.node(nodo_imprimir, 'Imprimir')
            dot.edge("parent", nodo_imprimir)
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_cerrado = f'ParentesisAbiertoIM_{instruccion_seguida}'
                dot.node(nodo_parentesis_cerrado, 'Parentesis Abierto')
                dot.edge(nodo_imprimir, nodo_parentesis_cerrado)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIIM_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_cerrado, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaIM_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_cerrado, nodo_cadena)
                        cadena_a_imprimir = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFIM_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoIM_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)
                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    nodo_punto_coma = f'PuntoComaIM_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    tokens.pop(i)
                                    #Se imprime en la consola
                                    consola.insert(tk.END,str(cadena_a_imprimir))
                                    instruccion_seguida+=1
                                    continue
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
        
        #Instruccion para imprimir en la consola con salto de linea
        elif tokens[i].tipo == "imprimirln" and i<len(tokens):
            consola.insert(tk.END, "\n")
            nodo_imprimirln = f'ImprimirlnILN_{instruccion_seguida}'
            dot.node(nodo_imprimirln, 'Imprimirln')
            dot.edge("parent", nodo_imprimirln)
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoILN_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_imprimirln, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIILN_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaILN_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        cadena_a_imprimir = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFILN_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoILN_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)
                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    nodo_punto_coma = f'PuntoComaILN_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    tokens.pop(i)
                                    #Se imprime en la consola
                                    consola.insert(tk.END,">>>" + str(cadena_a_imprimir) + "\n")
                                    instruccion_seguida+=1
                                    continue
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens)
                errores.append(error)
                return False

        #Instruccion para contar la cantidad de registros
        elif tokens[i].tipo == "conteo" and i<len(tokens):
            nodo_conteo = f'ConteoC_{instruccion_seguida}'
            dot.node(nodo_conteo, 'Conteo')
            dot.edge("parent", nodo_conteo)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoC_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_conteo, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                    nodo_parentesis_cerrado = f'ParentesisCerradoC_{instruccion_seguida}'
                    dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                    dot.edge(nodo_parentesis_abierto, nodo_parentesis_cerrado)
                    tokens.pop(i)
                    if tokens[i].tipo == "punto_coma" and i<len(tokens):
                        nodo_punto_coma = f'PuntoComaC_{instruccion_seguida}'
                        dot.node(nodo_punto_coma, 'Punto y Coma')
                        dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                        instruccion_seguida+=1
                        tokens.pop(i)
                        consola.insert(tk.END, ">>> Cantidad de registros: " + str(len(matriz) - 1) + "\n")
                        continue
                    else:
                        print("Error sintactico: Se esperaba un punto y coma")
                        error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba un parentesis cerrado")
                    error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
        
        #Instruccion para obtener el promedio de una columna especifica dado el nombre especifico de la clave (columna)
        #Hay que verificar que el nombre de la clave exista, si no existe, se debe de mostrar un error
        #Hay que verificar que el valor de cada elemento de la columna sea un numero, si no lo es, se debe de mostrar un error
        elif tokens[i].tipo == "promedio" and i<len(tokens):
            nodo_promedio = f'PromedioP_{instruccion_seguida}'
            dot.node(nodo_promedio, 'Promedio')
            dot.edge("parent", nodo_promedio)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoP_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_promedio, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIP_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaP_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        nombre_clave = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFP_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoP_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)
                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    tokens.pop(i)

                                    nodo_punto_coma = f'PuntoComaP_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    instruccion_seguida+=1

                                    #Instruccion correcta, se procede a obtener el promedio

                                    indice_clave = -1

                                    for j in range(len(matriz[0])):
                                        if matriz[0][j] == nombre_clave:
                                            indice_clave = j
                                            break
                                    
                                    if indice_clave != -1:
                                        suma = 0
                                        contador = 0
                                        for j in range(1, len(matriz)):
                                            if str(matriz[j][indice_clave]).replace(".", "", 1).isdigit():
                                                suma += float(matriz[j][indice_clave])
                                                contador += 1
                                            else:
                                                print("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero")
                                                error = Error("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero", tokens[i].fila, tokens[i].columna, nombre_clave)
                                                errores.append(error)
                                                return False
                                        
                                        promedio = suma / contador
                                        consola.insert(tk.END, ">>> Promedio de la clave '" + nombre_clave + "': " + str(promedio) + "\n")
                                        continue
                                    else:
                                        print("Error semantico: La clave '" + nombre_clave + "' no existe")
                                        error = Error("Error semantico: La clave '" + nombre_clave + "' no existe", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return False
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
        
        #contarsi(“Stock”, 1): Imprime por consola la cantidad de registros en la que el campo dado sea igual al valor dado. El valor debe ser un número entero o decimal.
        #Hay que verificar que el nombre de la clave exista, si no existe, se debe de mostrar un error
        #Hay que verificar que el valor de cada elemento de la columna sea un numero, si no lo es, se debe de mostrar un error
        #El valor debe ser un numero entero o decimal, solo numeros, NO cadenas
        elif tokens[i].tipo == "contarsi" and i<len(tokens):
            nodo_contarsi = f'ContarsiCS_{instruccion_seguida}'
            dot.node(nodo_contarsi, 'Contarsi')
            dot.edge("parent", nodo_contarsi)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoCS_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_contarsi, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasICS_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaCS_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        nombre_clave = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFCS_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "coma" and i<len(tokens):
                                nodo_coma = f'ComaCS_{instruccion_seguida}'
                                dot.node(nodo_coma, 'Coma')
                                dot.edge(nodo_comillas, nodo_coma)
                                tokens.pop(i)
                                if tokens[i].tipo == "numero" and i<len(tokens):
                                    nodo_numero = f'NumeroCS_{instruccion_seguida}'
                                    dot.node(nodo_numero, f'Numero: {tokens[i].valor}')
                                    dot.edge(nodo_coma, nodo_numero)
                                    valor = tokens[i].valor
                                    tokens.pop(i)
                                    if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                        nodo_parentesis_cerrado = f'ParentesisCerradoCS_{instruccion_seguida}'
                                        dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                        dot.edge(nodo_numero, nodo_parentesis_cerrado)
                                        tokens.pop(i)
                                        if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                            nodo_punto_coma = f'PuntoComaCS_{instruccion_seguida}'
                                            dot.node(nodo_punto_coma, 'Punto y Coma')
                                            dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                            instruccion_seguida+=1
                                            tokens.pop(i)

                                            #Instruccion correcta, se procede a obtener el conteo

                                            indice_clave = -1

                                            for j in range(len(matriz[0])):
                                                if matriz[0][j] == nombre_clave:
                                                    indice_clave = j
                                                    break
                                            
                                            if indice_clave != -1:
                                                contador = 0
                                                for j in range(1, len(matriz)):
                                                    if str(matriz[j][indice_clave]).replace(".", "", 1).isdigit():
                                                        if float(matriz[j][indice_clave]) == float(valor):
                                                            contador += 1
                                                    else:
                                                        print("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero")
                                                        error = Error("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                                        errores.append(error)
                                                        return False
                                                
                                                consola.insert(tk.END, ">>> Cantidad de registros en los que la clave '" + nombre_clave + "' es igual a " + str(valor) + ": " + str(contador) + "\n")
                                                continue
                                            else:
                                                print("Error semantico: La clave '" + nombre_clave + "' no existe")
                                                error = Error("Error semantico: La clave '" + nombre_clave + "' no existe", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                                errores.append(error)
                                                return False
                                        else:
                                            print("Error sintactico: Se esperaba un punto y coma")
                                            error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                            errores.append(error)
                                            return False
                                    else:
                                        print("Error sintactico: Se esperaba un parentesis cerrado")
                                        error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return False
                                else:
                                    print("Error sintactico: Se esperaba un numero")
                                    error = Error("Error sintactico: Se esperaba un numero", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba una coma")
                                error = Error("Error sintactico: Se esperaba una coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
        
        #datos(); Imprime por consola los registros leídos. En forma de tabla.
        elif tokens[i].tipo == "datos" and i<len(tokens):
            nodo_datos = f'DatosD_{instruccion_seguida}'
            dot.node(nodo_datos, 'Datos')
            dot.edge("parent", nodo_datos)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoD_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_datos, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                    nodo_parentesis_cerrado = f'ParentesisCerradoD_{instruccion_seguida}'
                    dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                    dot.edge(nodo_parentesis_abierto, nodo_parentesis_cerrado)
                    tokens.pop(i)
                    if tokens[i].tipo == "punto_coma" and i<len(tokens):
                        nodo_punto_coma = f'PuntoComaD_{instruccion_seguida}'
                        dot.node(nodo_punto_coma, 'Punto y Coma')
                        dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                        instruccion_seguida+=1
                        tokens.pop(i)

                        #Instruccion correcta, se procede a imprimir los registros

                        for j in range(len(matriz)):
                            for k in range(len(matriz[j])):
                                consola.insert(tk.END, "{:<18}".format(str(matriz[j][k])))
                            consola.insert(tk.END, "\n")
                        continue
                    else:
                        print("Error sintactico: Se esperaba un punto y coma")
                        error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba un parentesis cerrado")
                    error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
        
        #sumar(“campo”); Imprime en consola la suma todos los valores del campo dado, el campo debe ser numérico.
        #Hay que verificar que el nombre de la clave exista, si no existe, se debe de mostrar un error
        #Hay que verificar que el valor de cada elemento de la columna sea un numero, si no lo es, se debe de mostrar un error
        elif tokens[i].tipo == "sumar" and i<len(tokens):
            nodo_sumar = f'SumarS_{instruccion_seguida}'
            dot.node(nodo_sumar, 'Sumar')
            dot.edge("parent", nodo_sumar)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoS_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_sumar, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIS_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaS_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        nombre_clave = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFS_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoS_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)
                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    nodo_punto_coma = f'PuntoComaS_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    instruccion_seguida+=1
                                    tokens.pop(i)

                                    #Instruccion correcta, se procede a obtener la suma

                                    indice_clave = -1

                                    for j in range(len(matriz[0])):
                                        if matriz[0][j] == nombre_clave:
                                            indice_clave = j
                                            break
                                    
                                    if indice_clave != -1:
                                        suma = 0
                                        for j in range(1, len(matriz)):
                                            if str(matriz[j][indice_clave]).replace(".", "", 1).isdigit():
                                                suma += float(matriz[j][indice_clave])
                                            else:
                                                print("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero")
                                                error = Error("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero", tokens[i].fila, tokens[i].columna, nombre_clave)
                                                errores.append(error)
                                                return False
                                        
                                        consola.insert(tk.END, ">>> Suma de la clave '" + nombre_clave + "': " + str(suma) + "\n")
                                        continue
                                    else:
                                        print("Error semantico: La clave '" + nombre_clave + "' no existe")
                                        error = Error("Error semantico: La clave '" + nombre_clave + "' no existe", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return False
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
            
        #max(“campo”); Encuentra el valor máximo del campo dado
        #Hay que verificar que el nombre de la clave exista, si no existe, se debe de mostrar un error
        #Hay que verificar que el valor de cada elemento de la columna sea un numero, si no lo es, se debe de mostrar un error
        # El valor debe ser un numero entero o decimal, solo numeros, NO cadenas
        # Si hay mas de un valor maximo, se debe de mostrar el primero que se encuentre
        elif tokens[i].tipo == "max" and i<len(tokens):
            nodo_max = f'MaxM_{instruccion_seguida}'
            dot.node(nodo_max, 'Max')
            dot.edge("parent", nodo_max)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoM_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_max, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIM_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaM_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        nombre_clave = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFM_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoM_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)
                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    nodo_punto_coma = f'PuntoComaM_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    instruccion_seguida+=1
                                    tokens.pop(i)

                                    #Instruccion correcta, se procede a obtener el maximo

                                    indice_clave = -1

                                    for j in range(len(matriz[0])):
                                        if matriz[0][j] == nombre_clave:
                                            indice_clave = j
                                            break
                                    
                                    if indice_clave != -1:
                                        maximo = None
                                        for j in range(1, len(matriz)):
                                            if str(matriz[j][indice_clave]).replace(".", "", 1).isdigit():
                                                if maximo == None:
                                                    maximo = float(matriz[j][indice_clave])
                                                else:
                                                    if float(matriz[j][indice_clave]) > maximo:
                                                        maximo = float(matriz[j][indice_clave])
                                            else:
                                                print("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero")
                                                error = Error("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                                errores.append(error)
                                                return False
                                        
                                        consola.insert(tk.END, ">>> Maximo de la clave '" + nombre_clave + "': " + str(maximo) + "\n")
                                        continue
                                    else:
                                        print("Error semantico: La clave '" + nombre_clave + "' no existe")
                                        error = Error("Error semantico: La clave '" + nombre_clave + "' no existe", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return False
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False

        #min(“campo”); Encuentra el valor mínimo del campo dado
        # Hay que verificar que el nombre de la clave exista, si no existe, se debe de mostrar un error
        # Hay que verificar que el valor de cada elemento de la columna sea un numero, si no lo es, se debe de mostrar un error
        # El valor debe ser un numero entero o decimal, solo numeros, NO cadenas
        # Si hay mas de un valor minimo, se debe de mostrar el primero que se encuentre
        elif tokens[i].tipo == "min" and i<len(tokens):
            nodo_min = f'MinM_{instruccion_seguida}'
            dot.node(nodo_min, 'Min')
            dot.edge("parent", nodo_min)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoMi_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_min, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIMi_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaMi_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        nombre_clave = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFMi_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoMi_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)

                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    nodo_punto_coma = f'PuntoComaMi_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    instruccion_seguida+=1
                                    tokens.pop(i)

                                    #Instruccion correcta, se procede a obtener el minimo

                                    indice_clave = -1

                                    for j in range(len(matriz[0])):
                                        if matriz[0][j] == nombre_clave:
                                            indice_clave = j
                                            break
                                    
                                    if indice_clave != -1:
                                        minimo = None
                                        for j in range(1, len(matriz)):
                                            if str(matriz[j][indice_clave]).replace(".", "", 1).isdigit():
                                                if minimo == None:
                                                    minimo = float(matriz[j][indice_clave])
                                                else:
                                                    if float(matriz[j][indice_clave]) < minimo:
                                                        minimo = float(matriz[j][indice_clave])
                                            else:
                                                print("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero")
                                                error = Error("Error semantico: El valor de la clave '" + nombre_clave + "' no es un numero", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                                errores.append(error)
                                                return False
                                        
                                        consola.insert(tk.END, ">>> Minimo de la clave '" + nombre_clave + "': " + str(minimo) + "\n")
                                        continue
                                    else:
                                        print("Error semantico: La clave '" + nombre_clave + "' no existe")
                                        error = Error("Error semantico: La clave '" + nombre_clave + "' no existe", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                        errores.append(error)
                                        return False
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
                 
        #exportarReporte(“titulo”): Genera un archivo html con una tabla en donde se encuentren las claves y los registros leídos y con el título como parámetro.
        elif tokens[i].tipo == "exportarreporte" and i<len(tokens):
            nodo_exportar_reporte = f'ExportarReporteER_{instruccion_seguida}'
            dot.node(nodo_exportar_reporte, 'Exportar Reporte')
            dot.edge("parent", nodo_exportar_reporte)
            consola.insert(tk.END, "\n")
            tokens.pop(i)
            if tokens[i].tipo == "parentesis_abierto" and i<len(tokens):
                nodo_parentesis_abierto = f'ParentesisAbiertoER_{instruccion_seguida}'
                dot.node(nodo_parentesis_abierto, 'Parentesis Abierto')
                dot.edge(nodo_exportar_reporte, nodo_parentesis_abierto)
                tokens.pop(i)
                if tokens[i].tipo == "comillas" and i<len(tokens):
                    nodo_comillas = f'ComillasIER_{instruccion_seguida}'
                    dot.node(nodo_comillas, 'Comillas')
                    dot.edge(nodo_parentesis_abierto, nodo_comillas)
                    tokens.pop(i)
                    if tokens[i].tipo == "cadena" and i<len(tokens):
                        nodo_cadena = f'CadenaER_{instruccion_seguida}'
                        dot.node(nodo_cadena, f'Cadena: {tokens[i].valor}')
                        dot.edge(nodo_parentesis_abierto, nodo_cadena)
                        titulo = tokens[i].valor
                        tokens.pop(i)
                        if tokens[i].tipo == "comillas" and i<len(tokens):
                            nodo_comillas = f'ComillasFER_{instruccion_seguida}'
                            dot.node(nodo_comillas, 'Comillas')
                            dot.edge(nodo_cadena, nodo_comillas)
                            tokens.pop(i)
                            if tokens[i].tipo == "parentesis_cerrado" and i<len(tokens):
                                nodo_parentesis_cerrado = f'ParentesisCerradoER_{instruccion_seguida}'
                                dot.node(nodo_parentesis_cerrado, 'Parentesis Cerrado')
                                dot.edge(nodo_comillas, nodo_parentesis_cerrado)

                                tokens.pop(i)
                                if tokens[i].tipo == "punto_coma" and i<len(tokens):
                                    nodo_punto_coma = f'PuntoComaER_{instruccion_seguida}'
                                    dot.node(nodo_punto_coma, 'Punto y Coma')
                                    dot.edge(nodo_parentesis_cerrado, nodo_punto_coma)
                                    instruccion_seguida+=1
                                    tokens.pop(i)

                                    #Instruccion correcta, se procede a generar el reporte

                                    archivo = open("reporte.html", "w")
                                    archivo.write("<!DOCTYPE html>\n")
                                    archivo.write("<html>\n")
                                    archivo.write("<head>\n")
                                    archivo.write("<title>" + titulo + "</title>\n")
                                    archivo.write("<link rel=\"stylesheet\" href=\"style.css\">\n")
                                    archivo.write("</head>\n")
                                    archivo.write("<body>\n")
                                    archivo.write("<table border=\"1\">\n")
                                    archivo.write("<tr><th colspan=\"" + str(len(matriz[0])) + "\">" + titulo + "</th><tr>\n")
                                    for j in range(len(matriz)):
                                        archivo.write("<tr>\n")
                                        for k in range(len(matriz[j])):
                                            archivo.write("<td>" + str(matriz[j][k]) + "</td>\n")
                                        archivo.write("</tr>\n")
                                    archivo.write("</table>\n")
                                    archivo.write("</body>\n")
                                    archivo.write("</html>\n")
                                    archivo.close()

                                    consola.insert(tk.END, ">>> Reporte generado con exito\n")
                                    continue
                                else:
                                    print("Error sintactico: Se esperaba un punto y coma")
                                    error = Error("Error sintactico: Se esperaba un punto y coma", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                    errores.append(error)
                                    return False
                            else:
                                print("Error sintactico: Se esperaba un parentesis cerrado")
                                error = Error("Error sintactico: Se esperaba un parentesis cerrado", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                                errores.append(error)
                                return False
                        else:
                            print("Error sintactico: Se esperaba una comilla")
                            error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                            errores.append(error)
                            return False
                    else:
                        print("Error sintactico: Se esperaba una cadena")
                        error = Error("Error sintactico: Se esperaba una cadena", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                        errores.append(error)
                        return False
                else:
                    print("Error sintactico: Se esperaba una comilla")
                    error = Error("Error sintactico: Se esperaba una comilla", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                    errores.append(error)
                    return False
            else:
                print("Error sintactico: Se esperaba un parentesis abierto")
                error = Error("Error sintactico: Se esperaba un parentesis abierto", tokens[i].fila, tokens[i].columna, tokens[i].valor)
                errores.append(error)
                return False
        
        #Cualquier otro token que no sea una instruccion valida para el lenguaje se debe de mostrar un error sintactico, se eliminara el token y se seguira con el analisis
        else:
            print("Error sintactico: Token no valido")
            error = Error("Error sintactico: Token no valido", tokens[i].fila, tokens[i].columna, tokens[i].valor)
            errores.append(error)
            tokens.pop(i)
            error_encontrado_saltado = True
    
    if error_encontrado_saltado:
        return False
    else:
        return True



                                    
