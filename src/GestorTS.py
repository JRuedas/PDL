import pyTable.SymTable as SymTable

# Gestor de TS
symT = SymTable.SymTable()

# Lista que contendra los identificadores de las TS creadas, son enteros y las mas nuevas estaran al final
listaTS = []

# Metodo que crea una nueva TS, inserta el identificador al final de la lista
def creaTS():
    listaTS.append(symT.newTable())

# Metodo que destruye la TS Actual y borra su identificador de la lista
def destruyeTSActual():
    if symT.existTable(len(listaTS)-1):
         symT.destroyTable(len(listaTS)-1)
         del listaTS[len(listaTS)-1]
    else:
        print("No se puede borrar la tabla actual porque no existe")

# Metodo que obtiene la TS Actual, sera la ultima insertada en la lista (por el final)
def getTSActual():
    return int(listaTS[len(listaTS)-1])

# Metodo que inserta el lexema en la TSActual
# Retorna el ID asignado al lexema en esa tabla o falso si ya existia
def insertaLexemaEnTSActual(lexema):
    return symT.add(listaTS[len(listaTS)-1], lexema)

# Metodo que inserta el tipo del lexema en la TSActual
# Retorna falso si el lexema no existe en esa tabla o true si lo ha hecho correctamente
def insertaTipoEnTSActual(lexema,tipo):
    return symT.addType(listaTS[len(listaTS)-1], lexema, tipo)

# Metodo que obtiene el tipo del lexema en la TSActual
def getTipoLexemaTSActual(lexema):
    return symT.checkType(len(listaTS)-1,lexema)

# Metodo que busca en la TS actual un lexema y devuelve
def buscaEnTSActual():
    pass

def imprimeTSActual():
    symT.writeTableConsole(len(listaTS)-1)

# Imprime las TS en el orden en el que fueron creadas
def imprimeListaTS():
    for ts in listaTS:
        symT.writeTableConsole(ts)