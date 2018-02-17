# >>> Server Room Safety
# >>> https://www.hackerrank.com/contests/rookierank-4/challenges/server-room-safety

#!/bin/python3

import sys

# def validaIzquierda(height, position, lugar, situacion):
#     estado = True if position[lugar] + height[lugar] >= position[lugar + 1] else False
#     caida = position[lugar] + height[lugar]
#     siguiente = (lugar + 1) if (lugar + 1) > caida else caida
#     print('posicion: {} + altura: {} = {}'.format(position[lugar], height[lugar], position[lugar] + height[lugar]))
#     print('Caera hasta el: {} - resultado: {} - posicion: {} - caida: {} - siguiente: {} - estado: {}'.format(position[lugar] + height[lugar], position[lugar + 1], lugar, caida, siguiente, estado))
#     if lugar == 1 or estado == False:
#         return estado
#     else:
#         return validaIzquierda(height, position, siguiente, estado)

# def validaDerecha(height, position, lugar, situacion):
#     estado = True if position[lugar] - height[lugar] <= position[lugar - 1] else False
#     if lugar == len(height) - 1  or estado == False:
#         return estado
#     else:
#         return validaDerecha(height, position, lugar + 1, estado)

# def checkAll(n, height, position):
#     izq = False if n == 1 else position[0] + height[0] >= position[1]
#     der = False if n == 1 else position[n - 1] - height[n -1] <= position[n - 2]
#     if izq:
#         izq = validaIzquierda(height, position, n- 2, izq)
#     if der:
#         der = validaDerecha(height, position, 1, der)
#     if not izq and not der:
#         return 'NONE'
#     else:
#         if izq and der:
#             return 'BOTH'
#         else:
#             return 'LEFT' if izq else 'RIGHT'

# def derecha(n, height, position, lugar):
#     estado = True if position[lugar] - height[lugar] <= position[lugar - 1] else False
#     siguiente = position[lugar] - height[lugar]
#     maximo = max(position)
#     termino = (siguiente >= maximo) or (lugar == n - 1) or not estado
#     if termino:
#         return estado
#     else:
#         return derecha(n, height, position, lugar + 1 if (lugar + 1) > siguiente else siguiente)

# def izquierda(n, height, position, lugar):
#     estado = True if position[lugar] + height[lugar] >= position[lugar + 1] else False
#     siguiente = position[lugar] + height[lugar]
#     termino = not estado or (lugar == 1) or 

def derecha(n, height, position, lugar, alcance):
    estado = True if position[lugar] - height[lugar] <= position[lugar - 1] else False
    if position[lugar -1] < alcance and not estado:
        estado = True
    siguiente = position[lugar] - height[lugar]
    termino = not estado or siguiente <= 1 or lugar == 1
    tmp_alcance = siguiente if siguiente < alcance else alcance
    print('DER[{}] - EST:{} - SIG:{} - TER:{} - ALC:{} - TMPALC:{}'.format(lugar, estado, siguiente, termino, alcance, tmp_alcance))
    if termino:
        return estado
    else:
        return derecha(n, height, position, lugar - 1, siguiente)

def izquierda(n, height, position, lugar, alcance):
    estado = True if position[lugar] + height[lugar] >= position[lugar + 1] else False
    if position[lugar + 1] < alcance and not estado:
        estado = True
    siguiente = position[lugar] + height[lugar]
    termino = not estado or siguiente > max(position) or lugar == n - 2
    tmp_alcance = siguiente if siguiente > alcance else alcance
    print('IZQ[{}] - EST:{} - SIG:{} - TER:{} - ALC:{} - TMPALC:{}'.format(lugar, estado, siguiente, termino, alcance, tmp_alcance))
    if termino:
        return estado
    else:
        return izquierda(n, height, position, lugar + 1, tmp_alcance)

def checkAll(n, height, position):
    der = derecha(n, height, position, n - 1, 0)
    izq = izquierda(n, height, position, 0, 0)
    if not izq and not der:
        return 'NONE'
    else:
        if izq and der:
            return 'BOTH'
        else:
            return 'LEFT' if izq else 'RIGHT'

if __name__ == "__main__":
    n = 5 #int(input().strip())
    position = [1,2,3,4,8] #list(map(int, input().strip().split(' ')))
    height = [1,1,1,1,1] #list(map(int, input().strip().split(' ')))
    ret = checkAll(n, height, position)
    print(ret)