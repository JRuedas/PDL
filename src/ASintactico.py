import ply.yacc as yacc
import pyTable.SymTable as SymTable
from sys import stdin
import os
import Alexico
tokens = Alexico.tokens

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

def p_zeta(p):
    ''' zeta : EOL zeta
                | EOL '''
def p_lambda(p):
    ''' lambda : '''

def p_funcion(p):
    ''' funcion : function tiposvacio ID PARENT atributos PARENT zeta BRACKET conjunto BRACKET '''

def p_conjunto(p):
    ''' conjunto : elementos zeta conjunto
                | landa '''

def p_elementos(p):
    ''' elementos : var tipos ID
                | sentncias '''

def p_sentencias(p):
    ''' sentencias : if PARENT condicion PARENT BRACKET sentencias BRACKET opcional
                | ID OPASIG condicion
                | ID PARENT par PARETN
                | write PARENT condicion PARENT
                | prompt PARENT ID PARENT
                | prompt PARENT STRING PARENT
                | return retorno
                | sentenciaSwitch '''

def p_opcional(p):
    ''' opcional : else BRACKET sentencias BRACKET
                | lambda '''

def p_concicion(p):
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
                |ID PARENT par PARENT'''

def p_par(p):
    ''' par : condicion extra
            | lambda '''

def p_extra(p):
    ''' extra : COMMA condicion extra
            | lambda '''

def p_retorno(p):
    ''' retorno : condicion | lambda '''

def p_sentenciaSwitch(p):
    ''' sentenciaSwitch : switch PARENT condicion PARENT BRACKET zeta cases default COLON  sentencias zeta BRACKET '''

def p_cases(p):
    ''' cases : case PARENT NUMBER PARENT COLON sentencias zeta breaks '''

def p_breaks(p):
    ''' breaks : break zeta
            | break zeta cases
            | cases
            | lambda '''

def p_tiposvacio(p):
    ''' tiposvacio : tipos | lambda '''

def p_tipos(p):
    ''' tipos : int | chars | bool '''

def p_atributos(p):
    ''' tipos ID extraAttr | lambda '''

def p_extraAttr(p):
    ''' extraAttr : COMMA tipo ID extraAttr | lambda '''

