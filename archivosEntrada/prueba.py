'''dic = {}
hola = ('a', '0', 'b')

dic['B'] = [('A', '0', 'B'), ('B', '1', 'C')]
dic['A'] = [hola]
dic['J'] = [hola]'''

#       dic = {'estado_A': [('A', '0', 'B'), ('B', '1', 'C')], 'ESTADO_B': [('a', '0', 'b')]}

Entrada = ' A > 0 B ; A > 1 C'
entrada = 'A>0B;A>1C'
print(Entrada)
listaMAP = map(str, Entrada)

pepe = Entrada.replace(' ', '')
print(pepe)
listaLISTA = list(listaMAP)

listaSTRING = str(listaLISTA)

listaFINAL = eval(listaSTRING)


print('')