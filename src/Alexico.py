# coding=utf-8
import ply.lex as lex
import os
import sys
import GestorTS as gTS
#import ASintactico

class Alexico():

    def __init__(self,tokens,palReservadas):
        self.tokens = tokens
        self.palReservadas = palReservadas
        self.initALexico()

    def leerFichero(self):
        testFile=""
        fname = '..\\resources\\prueba.js'
        # fname = sys.argv
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                # global testFile
                for line in f:
                    testFile += str(line)
                print("Fichero de entrada:\n\n" + testFile + "\n\n")
            return testFile
        else:
            print("File not found")

    def initALexico(self):
        tokens = self.tokens + self.palReservadas
        palReservadas = self.palReservadas

        gTS.insertaEnTSActual("b")
        gTS.imprimeTSActual()

        # Expresiones regulares para algunos tokens simples
        t_OPRELA    = r'>'
        t_OPLOGI    = r'&&'
        t_OPASIG    = r'='
        t_LPARENT    = r'\('
        t_RPARENT    = r'\)'
        t_LBRACKET   = r'\{'
        t_RBRACKET   = r'\}'
        #t_QMARK     = r'\"'
        #t_APOSTROPH = r'\''
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
        def t_EOL(t):
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
            rutaFicheroErrores = "..\\generated\\errores.txt"
            print("Error de tipo Lexico: Caracter ilegal {0} en linea {1} \n".format(t.value[0],t.lexer.lineno))
            ferrores = open(rutaFicheroErrores,'a')
            ferrores.write("Error de tipo Lexico: Caracter ilegal {0} en linea {1} \n".format(t.value[0],t.lexer.lineno))
            ferrores.close()
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

        testFile =  self.leerFichero()

        lexer.input(testFile)

        #--------------------------------------------------------------------------------------------------

        rutaFicheroTokens = "..\\generated\\tokens.txt"

        print("Lista de Tokens generados: \n")

        ftok = open(rutaFicheroTokens,'w')
        ftok.write("//Lista de Tokens generados: \n")

        while True:
            tok = lexer.token()
            if not tok:
                # Generamos token EOF
                print('<EOF,->\n')
                ftok.close()
                break      # No hay mas entrada
            print('<'+str(tok.type)+','+str(tok.value)+'>\n')
            ftok.write('<'+str(tok.type)+','+str(tok.value)+'>\n')

