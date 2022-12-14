dic = {}
hola = ('a', '0', 'b')

dic['B'] = [('A', '0', 'B'), ('B', '1', 'C')]
dic['A'] = [hola]
dic['J'] = [hola]

#       dic = {'estado_A': [('A', '0', 'B'), ('B', '1', 'C')], 'ESTADO_B': [('a', '0', 'b')]}

keys = dic.keys()
print(keys)
sorted_keys = sorted(keys)
print(sorted_keys)

sorted_dic = {}
for key in sorted_keys:
  sorted_dic[key] = dic[key]

print(sorted_dic)

print('')