import funciones as fn
import os 

miLista = ['a','e','i','o','u']
miMatriz = [
    [1,2,3,4],
    [5,6,7,8],
    ['a','e','i','o']
]
# fn.recorridoSinPosicion(miLista)
# fn.recorridoConPosicion(miLista)
# fn.infoLista(miLista)
# fn.recorrerMatrizSinPosv1(miMatriz)
# fn.recorrerMatrizSinPosv2(miMatriz)
# fn.recorrerMatrizConPos(miMatriz)
# fn.recorrerMatrizPos3(miMatriz)
# f,c = fn.buscarPosicionEnMatriz(miMatriz)
"""if f == -1 and c == -1:
    print('Letra no encontrada')
else:
    print(f'Encontrado, en la posicion [{f}][{c}]')"""

"""letra = input('Ingrese letra a buscar:  ').lower()
if fn.buscarSiExiste(letra):
    print(f'Letra {letra} existe')
else:
    print('La letra no existe')
"""
r = 's'
while r == 's':
    txtIn = input('Ingrese un texto: ')
    fn.guardarEnTxt(txtIn)
    r = input('Desea ingresar un nuevo texto? [s/n]:  ').lower()
    if r != 's':
        print('Para ver sus textos revise el archivo')

