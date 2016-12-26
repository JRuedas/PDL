import ply.lex as lex
import os
testFileAux = []
testFile = ""
def leerFichero():
    input("Introduce algo \n")
    fname = 'C:\\Users\\alfre\\PycharmProjects\\PDL\\resources\\prueba.js'
    if os.path.isfile(fname):
        with open(fname,'r') as f:
            for line in f:
                testFileAux.append(line)
            global testFile
            testFile = ''.join(testFileAux)
            print(testFile)
        #with open(fname,'a') as f:
        #    f.write("\nAñadir linea")
    else:
        print("File not found")
#--------------------------------------------------------------------------------------------------
# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
    'ID',
    'ASIGNAR',
    'ENDFILE',
    'MAYOR'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ASIGNAR = r'='
# Comprobar si \ o / en t_MAYOR = r'>'
#Definir token espacio entre linea (mirar doc)
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define token ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper() :
        t.value = (t.value)
        return t

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
        break      # No more input
    print(tok)