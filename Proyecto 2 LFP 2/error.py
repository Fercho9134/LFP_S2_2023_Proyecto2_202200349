class Error:
    def __init__(self, tipo, fila, columna, expresion):
        self.tipo = tipo  
        self.fila = fila 
        self.columna = columna 
        self.expresion = expresion
