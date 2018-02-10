# >>> Text Alignment
# >>> https://www.hackerrank.com/challenges/text-alignment/problem
#Replace all ______ with rjust, ljust or center. 

thickness = 5# int(input()) #This must be an odd number
c = 'H'

largo = (thickness * 2) - 1
margen = int((largo - thickness) / 2)
maximo = (margen * 2) + (thickness * 5)
#Top Cone
for i in range(thickness):
    texto =''.join([c for s in range(((i+1) * 2) - 1)]) 
    print (texto.center(largo,' '))

#Top Pillars
for i in range(thickness + 1):
    texto =''.join(' ' for s in range(margen)) + ''.join([c for s in range(thickness)]) + ''.join(' ' for s in range(thickness * 3)) + ''.join([c for s in range(thickness)]) + ''.join(' ' for s in range(margen))
    print (texto.center(maximo,' '))

#Middle Belt
for i in range((thickness+1)//2):
    texto =''.join(' ' for s in range(margen)) + ''.join([c for s in range(thickness * 5)]) + ''.join(' ' for s in range(margen))
    print (texto.center(maximo,' '))

#Bottom Pillars
for i in range(thickness + 1):
    texto =''.join(' ' for s in range(margen)) + ''.join([c for s in range(thickness)]) + ''.join(' ' for s in range(thickness * 3)) + ''.join([c for s in range(thickness)]) + ''.join(' ' for s in range(margen))
    print (texto.center(maximo,' '))

#Bottom Cone
for i in range(thickness):
    tope = (thickness * 4)
    cantidad = ((thickness - i) * 2) - 1
    texto =''.join(' ' for s in range(tope)) + ''.join(' ' for s in range(int((largo - cantidad) / 2))) + ''.join([c for s in range(cantidad)]) 
    print (texto.rjust(tope,' '))