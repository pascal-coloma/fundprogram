import os

def recorridoSinPosicion(lista):
    for elem in lista:
        print(elem)

def recorridoConPosicion(lista):
    for pos in range(len(lista)):
        print(f'elemento {lista[pos]} en posicion: {pos}')

def infoLista(lista):
    print('*' * 40)
    print(f"""
Lista: {lista}
Largo de lista: {len(lista)}
Primer elemento: {lista[0]}
Ultimo elemento: {lista[-1]}
""")
    
def recorrerMatrizSinPosv1(matriz):
    for fila in matriz:
        print(fila)

def recorrerMatrizSinPosv2(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=' - ')
        print()

def recorrerMatrizConPos(matriz):
    print('Recorrer con posicion')
    print('*' * 40)
    for fila in range(len(matriz)):
        for colum in range(len(matriz[fila])):
            print(matriz[fila][colum], end=' ')
        print()

def recorrerMatrizPos3(matriz):
    print('Recorrer con posicion 3')
    print('*' * 40)
    for fila in range(len(matriz)): # Recorro la cantidad de filas dado el rango de la matriz (3)
        for colum in range(len(matriz[fila])): # Recorro las columnas tomando la longitud de la fila ubicada en matriz[fila]
            print(f'Elemento en posicion [{fila}][{colum}]: {matriz[fila][colum]}')
        print()

def buscarPosicionEnMatriz(matriz):
    letra = input('Ingrese letra a buscar: ')
    existe = False
    for fila in range(len(matriz)):
        for colum in range(len(matriz[fila])):
            if letra == matriz[fila][colum]:
                existe = True
                break
        if existe:
            break
    if existe:
        return fila, colum
    else:
        return -1, -1
    
def buscarSiExiste(letra): # Se utiliza para buscar elementos unicos
    lista = ['h','o','l','i','t','a']
    if letra in lista:
        return True
    else:
        return False

def guardarEnTxt(texto):
    try:
        if os.path.isfile('miArchivoTXT.txt'): # Si el archivo existe
            permiso = 'a' # Permiso append write 
        else:
            permiso = 'w' # Permiso de escritura
        with open ('miArchivoTXT.txt', permiso) as archivo:
            archivo.write(texto + '\n')
    except Exception as error: # se asigna la excepcion a una variable
        print('Error: ',error)
