import ply.lex as lex
import os
testFile = ""
#TODO Leer desde linea de comandos
def leerFichero():
    input("Introduce algo \n")
    fname = '..\\resources\\prueba.js'
    if os.path.isfile(fname):
        with open(fname, 'r') as f:
            global testFile
            for line in f:
                testFile += str(line)
            print(testFile)
    else:
        print("File not found")
#--------------------------------------------------------------------------------------------------
# Lista de tokens para el Analizador Lexico.
tokens = (
    'ID',               # Identificador
    'NUMBER',           # Numero
    'PLUS',             # Operador aritmetico suma: +
    'GT',               # Operador relacional mayor que: >
    'AND',              # Operador logico and: &&
    'ASSIGN',           # Operador asignacion: =
    'LPAREN',           # Parentesis izquierdo: (
    'RPAREN',           # Parentesis derecho: )
    'LBRACKET',         # Llave izquierdo: {
    'RBRACKET',         # Llave derecha: },
    'QMARK',            # Commilas dobles: "
    'APOSTROPH',        # Comillas simples: '
    'SEMICOLON',        # Punto y coma: ;
    'COLON',            # Dos puntos: : (para case)
    'COMMA',            # Coma: ,
    'EOL',              # Fin de linea
    'EOF'               # Fin de fichero
)

# Diccionario de palabras reservadas
palReservadas = {
    'int':'INT',
    'chars':'CHARS',
    'bool': 'BOOL',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'function': 'FUNCTION',
    'var': 'VAR',
    'write': 'WRITE',
    'prompt': 'PROMPT',
    'switch': 'SWITCH',
    'case': 'CASE',
    'break': 'BREAK',
    'default': 'DEFAULT',
}

tokens = tokens + tuple(palReservadas.values())

# Expresiones regulares para algunos tokens simples
t_PLUS      = r'\+'
t_GT        = r'>'
t_AND       = r'&&'
t_ASSIGN    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_QMARK     = r'\"'
t_APOSTROPH = r'\''
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','



# Comprobar si \ o / en t_MAYOR = r'>'
#Definir token espacio entre linea (mirar doc)


# Expresiones regulares para tokens complejos

# Define tegla para identificadores
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.lower() in palReservadas:
        t.type = (t.value.upper())
        t.value = ""
    else:
        t.value = "Devolver entrada TS"
    return t

# Define regla para numeros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define regla para numeros de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define regla para espacios en blanco
def t_nonspace(t):
    r'\s+'
    pass

# Define regla para comentarios
def t_comments(t):
    r'(\/\*((\*)*[^\*\/]*)*\*\/)|(\/\/[^\n]*)'
    pass

# Cadena con los caracteres a ignorar (espacios y tabs)
t_ignore  = ' \t'

# Regla de manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Mirar operdaor de igualdad en pyth
    #def t_ENDFILE(t) :
    #   if t == "eof"
    #      print("Fin fichero" % t.value[0])
    # return t_ID(t)
#t.lexer.skip(0)


#--------------------------------------------------------------------------------------------------


# Build the lexer
lexer = lex.lex()

leerFichero()

print("Prueba "+testFile)
lexer.input(testFile)

#--------------------------------------------------------------------------------------------------
#A.Sintactico
while True:
    tok = lexer.token()
    if not tok:
        break      # No hay mas entrada
    print('<'+str(tok.type)+','+str(tok.value)+'>\n')