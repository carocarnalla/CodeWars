# Para leer archivos .txt

# with open('texto.txt') as file:
#      next_line = file.readline()
#      while next_line:
#         if 'e' in next_line:
#             print('si')
#             next_line = file.readline()
#         else:
#             print('no')
#             next_line = file.readline()


# def datos(a):
#     t=[]
#     for i in range(0,(len(a))):
#         t.append(a[i])
#     return t

# print(datos('abc'))


# with open('texto.txt') as file:
#     t=[]
#     sig_fila = file.readline()
#     for i in sig_fila:
#         t.append(sig_fila[i])
#     print(t)

# Revisar
# with open('texto.txt') as file:
#     t=[]
#     next_line = file.readline()
#     while next_line:
#         t.append(next_line)
#         next_line=file.readline()
#         print(t)


#Sí jala
# with open('texto.txt') as file:
#     fila_inicial = file.readline()
#     E=fila_inicial.rfind('E')
#     fila_sig=file.readline()
#     if fila_sig[E] == ' ':
#         fila_sig=file.readline()
#         if fila_sig[E]=='@':
#             print('Fin')
#     else:
#         print('Se reinicia')


# Sí jala
# with open('texto.txt') as file:
#     fila_inicial = file.readline()
#     E=fila_inicial.rfind('E')
#     fila_sig=file.readline()
#     if fila_sig[E] == ' ':
#         print(fila_sig[E-1:E+2])
#     else:
#         print('Se reinicia')


# with open('texto.txt') as file:
#     a=file.readlines()[0]
#     print(a)











# from array import *

# with open('texto.txt') as file:
#     a=file.readlines()
#     l=[[0 for i in range(0,len(a[i]))] for i in range(0,len(a))]
#     #for i in a:
#     for i in range(0,len(a)):
#          for j in range(0,len(a[i])):
#             l=[[a[j] for j in range(0,len(a[i]))] for i in range(0,len(a))]
#         #print(len(a[i]))
#         #l.append(a[i])
#     print(l)
# lista_res = []
# lista_res.append('#', '#', '#', '#','#', 'E','#', '#','#', '#''#', '#'])
# [
# ['#', ' ', ' ', '#',' ', 'E¿#','#', '#','#', ' ', ' ', '#']

# Creates a list containing 5 lists, each of 8 items, all set to 0
# w, h = 8, 5
# Matrix = [[0 for x in range(w)] for y in range(h)] 





with open('texto.txt') as file:
    a=file.readlines()
    l=[]
    for i in range(0,len(a)):
        l.append(a[i])
    print(l)






# print(len(l))
# print(l[20])
# for i in l:
#     for j in i:




# Para en las matrices bidimensionales:
# Son de la forma T=[[1,2,3,4],[5,6,7,8]]
# Si queremos mandar llamar el número 7:
# T[[1][2]] que es el la posición 2 (0-1) y en el lugar 3 (0-1-2)

# Para insertar valores
# T.insert[1,[4.2, 4.4, 4.6, 4.8]]
# En el lugar 2 queda el listado 
# T=[[1,2,3,4],[4.2, 4.4, 4.6, 4.8],[5,6,7,8]]


# In [162]: text = "March 1st 2013 ntp[22485] Time server offset -.0070 sec"

# In [181]: text.rfind('offset')
# Out[181]: 38
# So you can cut the string after 'offset ' like this:

# In [183]: text[text.rfind('offset ')+len('offset '):]
# Out[183]: '-.0070 sec'


# def datos(a):
#     t=[]
#     for i in range(0,(len(a))):
#         t.append(a[i])
#     return t

# print(datos('abc'))
