import ply.lex as lex
import os
def leerFichero():
    input("Introduce algo \n")
    fname = 'C:\\Users\\Jonathan\\PycharmProjects\\PDL\\resources\\prueba.js'
    if os.path.isfile(fname):
        with open(fname,'r') as f:
            for line in f:
                print(line)
        with open(fname,'a') as f:
            f.write("\nAñadir linea")
    else:
        print("File not found")


leerFichero()
