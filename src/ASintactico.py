# coding=utf-8
import ply.yacc as yacc
import pyTable.SymTable as SymTable
from sys import stdin
import os
import GestorTS as gTS
import Alexico as AL
import ASemantico as ASem
#tokens = Alexico.tokens

# Lista de tokens para el Analizador Lexico.
tokens = (
    'ID',               # Identificador
    'NUMBER',           # Numero
    'STRING',           # Cadena
    'OPARIT',           # Operador aritmetico suma: +
    'OPRELA',           # Operador relacional mayor que: >
    'OPLOGI',           # Operador logico and: &&
    'OPASIG',           # Operador asignacion: =
    'LPARENT',          # Parentesis: (
    'RPARENT',          # Parentesis: )
    'LBRACKET',         # Llave: {
    'RBRACKET',         # Llave: }
#   'QMARK',            # Commilas dobles: "
#   'APOSTROPH',        # Comillas simples: '
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
    'DEFAULT',
    'TRUE',
    'FALSE'
)

gTS.creaTS()
tID = gTS.getTSActual()
gTS.insertaLexemaEnTSActual("a")
gTS.imprimeTSActual()

aLex = AL.Alexico(tokens,palReservadas)

# Importante, no borrar ya que el PLY necesita tener tokens+palreservadas juntos
tokens = tokens + palReservadas

precedencia = [  # Cuanto más bajo, más prioridad tiene.
    ('left', 'OPASIG'),  # =
    ('left', 'OPARIT'),  # +
    ('left', 'OPRELA'),  # >
    ('left', 'OPLOGI'),  # &&
]



def p_programa(p):
    ''' programa : elementos zeta programa
                | funcion zeta programa '''
                #| EOF '''
    p[0] = Program(p[1], p[3])



def p_zeta(p):
    ''' zeta : EOL zeta
             | EOL '''
    pass #Podríamos añadir el túmero de línea en la que nos encontramos. (Opcional?)

def p_lambda(p):
    ' lambda : '
    pass

def p_funcion(p):
    ' funcion : function tiposvacio ID PARENT atributos PARENT zeta BRACKET conjunto BRACKET '
    if p[4]=='LPARENT' and p[6]=='RPARENT' and p[8]=='LBRACKET' and p[10]=='RBRACKET':
        p[0] = Funcion(p[1], p[2], p[3], p[5], p[9])

def p_conjunto(p):
    ''' conjunto : elementos zeta conjunto
                 | lambda '''
    if len(p) == 3:
        p[0] = Conjunto(p[1],p[3])
    else:
        pass

def p_elementos(p):
    ''' elementos : var tipos ID
                  | sentncias '''

def p_sentencias_princip(p):
    ' sentencias : if PARENT condicion PARENT BRACKET sentencias BRACKET opcional '

def p_sentencias_ids(p):
    ''' sentencias : ID OPASIG condicion
                   | ID PARENT par PARETN '''

def p_sentencias_wrpr(p):
    ''' sentencias : write PARENT condicion PARENT
                   | prompt PARENT ID PARENT
                   | prompt PARENT STRING PARENT '''

def p_sentencias_return(p):
    ' sentencias : return retorno '

def p_sentencias_switch(p):
    ' sentencias: sentenciaSwitch '

def p_opcional(p):
    ''' opcional : else BRACKET sentencias BRACKET
                 | lambda '''

def p_condicion(p):
    ''' condicion : condicion OPLOGI relacional
                  | relacional '''

def p_relacional(p):
    ''' relacional : relacional OPRELA aritm
                   | aritm '''

def p_aritm(p):
    ''' aritm : aritm OPARIT valores
              | valores '''

def p_valores(p):
    ''' valores : ID
                | NUMBER
                | true | false
                | STRING
                | PARENT condicion PARENT
                | ID PARENT par PARENT'''

def p_par(p):
    ''' par : condicion extra
            | lambda '''

def p_extra(p):
    ''' extra : COMMA condicion extra
              | lambda '''

def p_retorno(p):
    ''' retorno : condicion
                | lambda '''

def p_sentenciaSwitch(p):
    ' sentenciaSwitch : switch PARENT condicion PARENT BRACKET zeta cases default COLON  sentencias zeta BRACKET '

def p_cases(p):
    ' cases : case PARENT NUMBER PARENT COLON sentencias zeta breaks '

def p_breaks(p):
    ''' breaks : break zeta
               | break zeta cases
               | cases
               | lambda '''

def p_tiposvacio(p):
    ''' tiposvacio : tipos
                   | lambda '''

def p_tipos(p):
    ''' tipos : int
              | chars
              | bool '''

def p_atributos(p):
    ''' tipos : ID extraAttr
              | lambda '''

def p_extraAttr(p):
    ''' extraAttr : COMMA tipo ID extraAttr
                  | lambda '''

def p_error(p):
    print("Error sintáctico en el token tipo", p.type)
    if not p:
        print("Error sintáctico en el final del fichero")
        return

    #Vamos a activar el modo pánico con Parent. y con Llaves
    while True:
        tok = parser.token()
        if not tok or tok.type=='RPARENT' or tok.type=='RBRACKET':
            break
    parser.restart()

