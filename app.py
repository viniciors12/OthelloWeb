from flask import Flask, render_template, json, request,jsonify
from werkzeug.local import Local
from Logic import *

app = Flask(__name__)

loc = Local()
loc.matriz = []


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showBoard', methods=['POST'])
def showBoard():
    # read the posted values from the UI
    print('Esta llegando aqui')
    sizee = request.form['boardSize']   #Se piden los datos del tamaño de la matriz
    play1 = request.form['player1'] #Color del jugador 1
    play2 = request.form['player2'] #color del jugador 2
    #jugadaValida()
    print(sizee)
    print(play1)
    print(play2)

    play1Mov = 1
    play2Mov = 0


    loc.matriz = llenaMatriz(int(sizee))  #Se llena la matriz logica
    #Se retorna un tamplate con los datos para mostrar graficamente
    return render_template('board.html', matriz=loc.matriz, size=int(sizee) , play1Mov=play1Mov, play2Mov=play2Mov, play1=play1, play2=play2)

#GET OPTIENE DATA
#POST MODIFICACIÓN DE DATA

@app.route('/A', methods=['POST'])
def prueba():

    roww = request.json['row']   #Mediante un json se capturan la posicion row
    coll = request.json['column'] # y la posicion column

    #Con cada click se piden las movidad actualizadas
    play1movs = request.json['play1Movs']
    play2movs = request.json['play2Movs']
    play1 = request.json['play1']
    play2 = request.json['play2']

    color1 = '\u26AA'
    color2 = '\u26AA'

    if play1 == 'white':
        color1='\u26AA'
    else:
        color1 = '\u26AB'

    if play2 == 'white':
        color2='\u26AA'
    else:
        color2 = '\u26AB'

    color = '\u26AA'

    if(play1movs > play2movs):  #Si el jugador 1 es mayor, es el turno del jugador 2
        color = color1
        play2movs += 1
    else:
        color = color2
        play1movs += 1

    #variable ficha con las posiciones x,y de la matriz
    ficha=(roww-1,coll-1)
    #se llama al metodo logica que valida los movimientos
    loc.matriz = jugadaValida(ficha, color, len(loc.matriz), loc.matriz)
    #Si no hay fichas negras, gana el jugador blanco
    if (hayFicha('\u26AA', loc.matriz)) == False:
            return jsonify(page=render_template('Ganador.html', blanquito='\u26AB' ,puntitos=cuentaPuntos(len(loc.matriz),loc.matriz)))
    #Si no hay fichas blancas, gana el jugador negro
    elif (hayFicha('\u26AB', loc.matriz)) == False:
            return jsonify(page=render_template('Ganador.html', negrito='\u26AA' ,puntitos=cuentaPuntos(len(loc.matriz), loc.matriz)))
    #Si no hay fichas vacias, se saca el que tenga la mayor cantidad de fichas
    elif (hayFicha('\u2B1c', loc.matriz)) == False:
            return jsonify(page=render_template('Ganador.html', puntitos=cuentaPuntos(len(loc.matriz), loc.matriz)))
    #Si no se cumple nada de lo anterior, se sigue jugando
    else:
        return jsonify(page=render_template('temAux.html', matriz=loc.matriz,size=len(loc.matriz)), play1movs=play1movs, play2movs=play2movs)


#Metodo para mostrar la matriz graficamente
@app.route('/b', methods=['POST'])
def show():
    return render_template('board.html', matriz=loc.matriz)


if __name__ == "__main__":
    app.run()
