from Ficha import *

matriz = []


def llenaMatriz(size):  #Metodo para llenar la matriz utilizada en el juego
    matriz = [[Ficha('\u2B1c',0,x,y) for x in range(size)] for y in range(size)]
    half = size//2
    matriz[half-1][half-1].setColor('\u26AA')
    matriz[half][half].setColor('\u26AA')
    matriz[half-1][half].setColor('\u26AB')
    matriz[half][half-1].setColor('\u26AB')
    ba(matriz, size)
    return matriz

def ba(matriz, size):
    tabla = ""
    numerito = 0
    for x in range(size):
        for y in range(size):
            matriz[x][y].setId(numerito)
            matriz[x][y].setX(x)
            matriz[x][y].setY(y)
            numerito+=1
            tabla += str(matriz[x][y].getColor()) + " "
        tabla += "\n"
    print(tabla)
    return matriz


def verificaRangoVecina(ficha,x,y,size): #VERIFICA QUE LOS VECINOS DE FICHA A PONER TENGAN UNA POSICION VÁLIDA
    if (x == ficha[0] - 1 and y==ficha[1]):  # CASO ARRIBA
        if ficha[0] - 1 < 0:
            return True
        else:
            return False

    elif (x == ficha[0] + 1 and y==ficha[1]):  # CASO ABAJO
        if ficha[0] + 1 > size - 1:
            return True
        else:
            return False

    elif (y == ficha[1] - 1 and x==ficha[0]):  # CASO IZQ
        if ficha[1] - 1 < 0:
            return True
        else:
            return False

    elif (y == ficha[1]+1 and x==ficha[0]):  # CASO DER
        if ficha[1] + 1 > size-1:
            return True
        else:
            return False

    elif (x == ficha[0] - 1 and y == ficha[1] - 1): # CASO ESQUINA IZQ ARRIBA
        if ficha [0]-1 < 0 or ficha[1]-1 < 0:
            return True
        else:
            return False
    elif (x == ficha[0] - 1 and y == ficha[1] + 1): # CASO ESQUINA DER ARRIBA
        if ficha [1]+1 > size-1 or ficha[0]-1 < 0:
            return True
        else:
            return False
    elif (x == ficha[0] + 1 and y == ficha[1] - 1): # CASO ESQUINA DER ABAJO
        if ficha [1]-1 < 0 or ficha[0]+1 >size-1:
            return True
        else:
            return False
    elif (x == ficha[0] + 1 and y == ficha[1] + 1): # CASO ESQUINA IZQ ABAJO
        if ficha [1]+1 > size-1 or ficha[0]+1 > size-1:
            return True
        else:
            return False


def fueraDeRango(jugada, size):

    if jugada[0]+1 > size or jugada[0]<0 or jugada[1]+1>size or jugada[1]>size:  #SI DONDE SE QUIERE PONER LA PIEZA ESTA FUERA DE RANGO
        return True

    else:
        return False

def fueraDeRango2(x,y, size):

    if x+1 > size or x<0 or y+1>size or y>size:  #SI DONDE SE QUIERE PONER LA PIEZA ESTA FUERA DE RANGO
        return True

    else:
        return False


def filtersito(lista,color):  #filter que agarra una fila para la busqueda de una ficha
    newlist = list(filter(lambda elem: elem.getColor()== color, lista))

    return newlist

def cuentaPuntos(size,matriz):  #Cuenta los puntos de las fichas negras y blancas

    lista = []
    negras =0
    blancas =0
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if y < size:
                lista.append(matriz[x][y])
            if y == size-1:
                negras += len(filtersito(lista,'\u26AB'))
                blancas += len(filtersito(lista,'\u26AA'))
                lista.clear()
    puntitos = (negras,blancas)  #retorna una tupla con los puntajes de las negras y blancas respectivamente
    return puntitos


def hayFicha(color, matriz):  #Verifica si hay una ficha en especifico, por ejemplo, sino hay vacias, el juego debe terminar
    lista = []

    for x in range(len(matriz)):
        for y in range(len(matriz)):
            lista.append(matriz[x][y])

    if(len(filtersito(lista,color))==0):  #Utiliza el filtar en cada fila para ir buscando alguno ficha del tipo a buscar
        return False
    else:
        return True


def jugadaValida(ficha,color, size, matriz):  #VERIFICA TODOS LOS VECINOS Y VE SI LA FICHA PUEDE COLOCARSE

    if fueraDeRango(ficha, size)==False: #Esta en el rango de la matriz?
        if matriz[ficha[0]][ficha[1]].getColor() == '\u2B1c': #Esta vacio donde se quiere poner?

            if cruzYEquis(ficha,color,ficha[0]- 1,ficha[1], size, matriz): #CASO ARRIBA VERIFICA
                matriz[ficha[0]][ficha[1]].setColor(color)  #coloca la ficha
                vertical(ficha,color, matriz) #pinta
                imprimeMatriz(size, matriz) #imprime la matriz modificada

            if cruzYEquis(ficha, color, ficha[0] + 1,ficha[1], size, matriz) :  # CASO ABAJO VERIFICA
                matriz[ficha[0]][ficha[1]].setColor(color) #coloca la ficha
                vertical(ficha, color, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada

            if cruzYEquis(ficha, color, ficha[0], ficha[1]-1,size, matriz) : #CASO LADO IZQ
                matriz[ficha[0]][ficha[1]].setColor(color)  #coloca la ficha
                horizontal(ficha,color, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada

            if cruzYEquis(ficha, color, ficha[0], ficha[1]+1, size, matriz): #CASO LADO DER
                matriz[ficha[0]][ficha[1]].setColor(color) #coloca la ficha
                horizontal(ficha, color, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada


            if cruzYEquis(ficha,color,ficha[0] - 1,ficha[1] - 1, size, matriz): # CASO ESQUINA IZQ ARRIBA
                matriz[ficha[0]][ficha[1]].setColor(color)#coloca la ficha
                diagonalIzqAbaj(ficha, color, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada

            if cruzYEquis(ficha,color,ficha[0] - 1,ficha[1] + 1, size, matriz): #CASO ESQUINA DER ARRIBA
                matriz[ficha[0]][ficha[1]].setColor(color)#coloca la ficha
                diagonalDerHaciaArr(ficha, color,size, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada

            if cruzYEquis(ficha,color,ficha[0] + 1,ficha[1] - 1,size, matriz): #CASO ESQUINA DER ABAJO
                matriz[ficha[0]][ficha[1]].setColor(color)#coloca la ficha
                diagonalDerHaciaAb(ficha, color, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada

            if cruzYEquis(ficha,color,ficha[0] + 1,ficha[1] + 1, size, matriz): #CASO ESQUINA IZQ ABAJO
                matriz[ficha[0]][ficha[1]].setColor(color)#coloca la ficha
                diagonalIzqArri(ficha, color, matriz)#pinta
                imprimeMatriz(size, matriz)#imprime la matriz modificada

            return matriz

        else:
            print("Ya hay una ficha en esa posición")
            return matriz
    else:
        print("Esa posición esta fuera del tablero")
        return matriz

def cruzYEquis(ficha,color,x,y, size, matriz):  #ESTE METODO EVALUA TODAS LAS POSIBILIDADES, TANTO EN CRUZ COMO EN EQUIS
    loop = True
    auxx = x
    auxy = y

    if verificaRangoVecina(ficha,x,y, size) == False:

        if matriz[x][y].getColor() != '\u2B1c':

            while(loop):
                #SE DESCARTA LA JUGADA SI ES VACIA, FUERA DE RANGO, O DEL MISMO COLOR LA SIGUIENTE POS (SOLO PARA LA PIEZA VECINA)

                if fueraDeRango2(auxx,auxy, size) == False:

                    if matriz[x][y].getColor() == '\u2B1c'  or matriz[x][y].getColor() == color:
                        return False


                    #SI AVANZO Y NO ENCONTRO DE SUS MISMO COLOR O VACIAS PERO SI UNA DE DIFERENTE COLOR ES PONTECIAL
                    elif matriz[auxx][auxy].getColor() == color:
                       return True


                    #SI EN EL RECORRIDO ENCUENTRA UNA VACIA, SE CAE LA JUGADA
                    elif matriz[auxx][auxy].getColor() == '\u2B1c':
                        return False

                    #AUMENTE SEGUN EL CASO QUE HAYA ENTRADO
                    if(x == ficha[0]-1 and y == ficha[1]): #CASO ARRIBA
                        auxx=auxx-1
                    elif(x == ficha[0]+1 and y == ficha[1]): #CASO ABAJO
                        auxx=auxx+1
                    elif(y == ficha[1]-1 and x == ficha[0]):#CASO IZQ
                        auxy=auxy-1
                    elif (y == ficha[1] + 1 and x == ficha[0]): #CASO DER
                        auxy = auxy + 1
                    elif (x == ficha[0] - 1 and y == ficha[1] - 1): #CASO ESQ ARRIBA IZQ
                         auxy = auxy - 1
                         auxx = auxx - 1
                    elif (x == ficha[0] - 1 and y == ficha[1] + 1): #CASO ESQ ARRIBA DER
                         auxy = auxy + 1
                         auxx = auxx - 1
                    elif (x == ficha[0] + 1 and y == ficha[1] - 1): #CASO ESQ ABAJO DER
                         auxy = auxy - 1
                         auxx = auxx + 1
                    elif (x == ficha[0] + 1 and y == ficha[1] + 1): #CASO ESQ ABAJO IZQ
                         auxy = auxy + 1
                         auxx = auxx + 1
                else:
                    return False
def diagonalIzqArri(fichaI, color, matriz):  #Metodo que saca una lista para que el map cambie las fichas de color
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz)):

            if x == fichaI[0] and y == fichaI[1]:
                k = x; j = y
                while(j<len(matriz)):
                    lista.append(matriz[k][j])
                    k+=1 ; j+=1

    mapitaEquis(lista, color, matriz)

def diagonalIzqAbaj(fichaI, color, matriz): #Metodo que saca una lista para que el map cambie las fichas de color
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz)):

            if x == fichaI[0] and y == fichaI[1]:
                k = x; j = y
                while(j>=0):
                    lista.append(matriz[k][j])
                    k-=1 ; j-=1

    mapitaEquis(lista, color, matriz)


def diagonalDerHaciaArr(fichaI, color, size, matriz): #Metodo que saca una lista para que el map cambie las fichas de color
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz)):

            if x == fichaI[0] and y == fichaI[1]:
                k = x; j = y
                while(k>=0 and j<size):
                    lista.append(matriz[k][j])
                    k-=1 ; j+=1

    mapitaEquis(lista, color, matriz)

def diagonalDerHaciaAb(fichaI, color, matriz): #Metodo que saca una lista para que el map cambie las fichas de color
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if x == fichaI[0] and y == fichaI[1]:
                k = x; j = y
                while(k<len(matriz)):
                    lista.append(matriz[k][j])
                    k+=1 ; j-=1

    mapitaEquis(lista,color, matriz)


def vertical(fichaI, color, matriz): #Metodo que saca una lista para que el map cambie las fichas de color
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz)):

            if y == fichaI[1]:
                lista.append(matriz[x][y])

    mapitaCruz(lista, color,fichaI,0, matriz)


def horizontal(fichaI,color, matriz): #Metodo que saca una lista para que el map cambie las fichas de color
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz)):

            if x == fichaI[0]:
                lista.append(matriz[x][y])

    mapitaCruz(lista, color, fichaI, 1, matriz)  # HACER BRETE DE SACAR LOS QUE SE TENGAN QUE SACAR DE LA LISTA

#metodo map que agarra lista que recibe del los metodos anteriores, cambia de color y vuelve a mater a la matriz
def mapitaEquis(lista, color, matriz):#Solo sirve para el caso equis (diagonales)
    indices = [-15, -15]
    aux = 1
    indices[0] = aux
    while (aux < len(lista)):

        if (lista[aux].getColor() == '\u2B1c'):
            break

        elif (lista[aux].getColor() == lista[0].getColor()):
            indices[1] = aux
            break
        aux += 1

    # CAMBIA DE COLOR TODOS LOS QUE SE HAYAN ENCONTRADO
    newlist = list(map(lambda elem: Ficha(color, elem.id, elem.x, elem.y), lista[indices[0]:indices[1]]))

    #LOS REINCERTA EN LA MATRIZ YA MODIFICADOS
    for k in range(len(newlist)):
        matriz[newlist[k].x][newlist[k].y] = newlist[k]

    return matriz

#metodo map que agarra lista que recibe del los metodos anteriores, cambia de color y vuelve a mater a la matriz

def mapitaCruz(lista, color, fichaI, posCruz, matriz):  #Solo sirve para el caso cruz (vertical,horizontal)
    indices = [-15, -15]
    x = fichaI[posCruz]
    aux = fichaI[posCruz] + 1
    # EN CASO DE QUE LOS PUNTAJES SEAN A LA DERECHA DE LA LISTA
    if aux<len(lista) and lista[x + 1].getColor() != '\u2B1c' and lista[x + 1].getColor() != lista[x].getColor():
        indices[0] = x
        while (aux < len(lista)):

            if (lista[aux].getColor() == '\u2B1c'):
                break

            elif (lista[aux].getColor() == lista[x].getColor()):
                indices[1] = aux
                break
            aux += 1

    # EN CASO DE QUE LOS PUNTAJES SEAN A LA IZQUIERDA DE LA LISTA
    aux = fichaI[posCruz] - 1 #OJO A ESTE CAMBIO
    if(indices[1]==-15):
        if aux>0 and lista[x - 1].getColor() != '\u2B1c' and lista[x - 1].getColor() != lista[x].getColor():
            indices[1] = x

            while (aux >= 0):
                if (lista[aux].getColor() == '\u2B1c'):
                    break

                elif (lista[aux].getColor() == lista[x].getColor()):
                    indices[0] = aux
                    break
                aux -= 1

    #CAMBIA DE COLOR TODOS LOS QUE SE HAYAN ENCONTRADO
    newlist = list(map(lambda elem: Ficha(color, elem.id,elem.x,elem.y), lista[indices[0]:indices[1]]))

    for k in range(len(newlist)):
        matriz[newlist[k].x][newlist[k].y] = newlist[k]

    return matriz

def imprimeMatriz(size, matriz):  #METODO PARA IMPRIMIR LA MATRIZ
    tabla = ""
    for x in range(size):
        for y in range(size):
            tabla += str(matriz[x][y].getColor()) + " "
        tabla += "\n"
    print(tabla)
    return matriz



