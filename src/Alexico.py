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
            print("Fichero de entrada:\n\n" + testFile + "\n\n")
    else:
        print("File not found")

#--------------------------------------------------------------------------------------------------
# Lista de tokens para el Analizador Lexico.
tokens = (
    'ID',               # Identificador
    'NUMBER',           # Numero
    'STRING',           # Cadena
    'OPARIT',           # Operador aritmetico suma: +
    'OPRELA',           # Operador relacional mayor que: >
    'OPLOGI',           # Operador logico and: &&
    'OPASIG',           # Operador asignacion: =
    'PARENT',           # Parentesis: ( o )
    'BRACKET',          # Llave: { o }
    'QMARK',            # Commilas dobles: "
    'APOSTROPH',        # Comillas simples: '
    'SEMICOLON',        # Punto y coma: ;
    'COLON',            # Dos puntos: : (para case)
    'COMMA',            # Coma: ,
    'EOL',              # Fin de linea
    'EOF'               # Fin de fichero
)

# Lista de palabras reservadas
palReservadas = (
    'INT',
    'CHARS',
    'BOOL',
    'IF',
    'ELSE',
    'RETURN',
    'FUNCTION',
    'VAR',
    'WRITE',
    'PROMPT',
    'SWITCH',
    'CASE',
    'BREAK',
    'DEFAULT'
)

# Importante, no borrar ya que el PLY necesita tener tokens+palreservadas juntos
tokens = tokens + palReservadas

# Expresiones regulares para algunos tokens simples
t_OPRELA    = r'>'
t_OPLOGI    = r'&&'
t_OPASIG    = r'='
t_PARENT    = r'(\()|(\))'
t_BRACKET   = r'(\{)|(\})'
t_QMARK     = r'\"'
t_APOSTROPH = r'\''
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','
# Cadenas
t_STRING    = r'\'([^\'\n])*\'|\"([^"\n])*\"'

# Expresiones regulares para tokens complejos

# Define tegla para identificadores
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper() in palReservadas:
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

# Define regla para operaciones aritmeticas (+ y --)
def t_OPARIT(t):
    r'(\+)|(--[a-zA-Z][a-zA-Z0-9_;]*)'
    if t.value != "+":
        t.value = "--"
    return t

# Define regla para numeros de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define regla para comentarios de /* */ y de //
def t_comments(t):
    r'(\/\*((\*)*[^\*\/]*)*\*\/)|(\/\/[^\n]*)'
    pass

# Cadena con los caracteres a ignorar (espacios y tabs)
t_ignore  = ' \t'

# Regla de manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Define regla para espacios en blanco !!! INNECESARIA, ya los ignoramos en t_ignore
# def t_nonspace(t):
#     r'\s+'
#     pass

#Mirar operdaor de igualdad en pyth
    #def t_ENDFILE(t) :
    #   if t == "eof"
    #      print("Fin fichero" % t.value[0])
    # return t_ID(t)
#t.lexer.skip(0)


#--------------------------------------------------------------------------------------------------


# Construirimos el Analizador
lexer = lex.lex()

leerFichero()

lexer.input(testFile)

#--------------------------------------------------------------------------------------------------

print("Lista de Tokens generados: \n")
while True:
    tok = lexer.token()
    if not tok:
        break      # No hay mas entrada
    print('<'+str(tok.type)+','+str(tok.value)+'>\n')