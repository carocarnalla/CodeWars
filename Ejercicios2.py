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
#     l=[]
#     for letra in a:
#         l.append(letra)
        
#     #l=[[0 for i in range(0,len(a[i]))] for i in range(0,len(a))]
#     #for i in a:
#     # for i in range(0,len(a)):
#     #       for j in range(0,len(a[i])):
#     #          l=[[a[j] for j in range(0,len(a[i]))] for i in range(0,len(a))]
#         #print(len(a[i]))
#         #l.append(a[i])
#     #l=[*a(i)]
#     print(l)

# lista_res.append('#', '#', '#', '#','#', 'E','#', '#','#', '#''#', '#'])
# [
# ['#', ' ', ' ', '#',' ', 'E¿#','#', '#','#', ' ', ' ', '#']

# Creates a list containing 5 lists, each of 8 items, all set to 0
# w, h = 8, 5
# Matrix = [[0 for x in range(w)] for y in range(h)] 

# a='abcdefg'
# l=[*a]

# print(l)



# with open('texto.txt') as file:
#     a=file.readlines()
#     l=[]
#     for i in range(0,len(a)):
#         l.append(a[i])
#     print(l)






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


# with open('texto.txt') as file:
#     a=file.readlines()
#     b=file.readlines()
#     while (file.readlines()):
#         print('*')
    # l=[]
    # for i in a:
    #     l.append()
    # print(l)
    # print(a)
    # print(b)

#************************************************************************************************************
myfile = open("texto.txt", "r")
myline = myfile.readline()
l=[]
while myline:
    l.append(list(myline))
    myline = myfile.readline()
myfile.close() 
#************************************************************************************************************
# print(l)
# a=l.index('E')
# print(a)
# print(l)
# print(len(l[0]))

#************************************************************************************************************
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if l[i][j]=='#':
            continue
        elif l[i][j]=='E':
            Ei=i
            Ej=j
            #print(Ei,Ej)
        else:
            continue
pia=Ei
pja=Ej

pi=Ei+1
pj=Ej

# Variables para guardar la bifurcación
xi=0
xj=0
yi=0
yj=0

# Valores para reinicio. Estos no se modifican
pier=Ei
pjer=Ej
pir=Ei+1
pjr=Ej

#************************************************************************************************************
    

# for i in range(0,len(l)):
#     for j in range(0,len(l[i])):
#         if l[i][j]=='#':
#             continue
#         elif l[i][j]=='E':
#             Ei=i
#             Ej=j
#             #print(Ei,Ej)
#         else:
#             continue
# pi=Ei+1
# pj=j
# print('Las coordenadas de inicio son {},{}'.format(Ei,Ej))
# # Abajo
# # if l[Ei+1][Ej]==' ':
# #     nueva=Ei+1
# # elif l[Ei+1][Ej]=='#':
# #     print('No')

# a=1
# b=0
# def recu(a, b):
#     print(a)
#     if(a==1):
#         recu(2,3)
#         return 0
#     if(a==2):
#         recu(3,3)
#         return 0
#     return 0

#     #recu(1,2)

# recu(a,b)







# print(l[pi][pj])
#****************************************Sí funciona*********************************************************************************
# Este es cuando hay un solo camino

# def lab(pi, pj):
#     print(pi,pj)
#     if l[pi][pj-1]=='#' and l[pi][pj+1]=='#' and (l[pi+1][pj]!='#'):
#         print('abajo')
#         l[pi][pj]='#'
#         lab(pi+1,pj)
#         return 0
#     if l[pi][pj-1]=='#' and ((l[pi][pj+1]!='#')) and l[pi+1][pj]=='#':
#         print('der')
#         l[pi][pj]='#'
#         lab(pi,pj+1)
#         return 0
#     if ((l[pi][pj-1]!='#')) and (l[pi][pj+1]=='#') and l[pi+1][pj]=='#':
#         print('izq')
#         l[pi][pj]='#'
#         lab(pi,pj-1)
#         return 0
#     if l[pi][pj]=='@':
#         print('listo')
#     return 0

#     #recu(1,2)

# lab(pi,pj)
#*************************************************************************************************************************************



# l[pi][pj]
# arriba = l[pi-1][pj]

# abajo = l[pi+1][pj]

# izq = l[pi][pj-1]

# der = l[pi][pj+1]



# def lab(pi, pj):
#     arriba = l[pi-1][pj]
#     abajo = l[pi+1][pj]
#     izq = l[pi][pj-1]
#     der = l[pi][pj+1]
#     print(pi,pj)
#     if izq=='#' and der=='#' and (abajo!='#'):
#         print('abajo')
#         l[pi][pj]='#'
#         lab(pi+1,pj)
#         return 0
#     if izq=='#' and ((der!='#')) and abajo=='#':
#         print('der')
#         l[pi][pj]='#'
#         lab(pi,pj+1)
#         return 0
#     if ((izq!='#')) and (der=='#') and abajo=='#':
#         print('izq')
#         l[pi][pj]='#'
#         lab(pi,pj-1)
#         return 0
#     if l[pi][pj]=='@':
#         print('listo')
#     return 0

# lab(pi,pj)

###


#*************************************************************************************************************************************
#Con dos pares de variables



# def lab(pi, pj, pia, pja):
#     arriba = l[pi-1][pj]
#     abajo = l[pi+1][pj]
#     izq = l[pi][pj-1]
#     der = l[pi][pj+1]
#     print(pia,pja)
#     print(pi,pj)
    
#     if pi>pia and pj==pja:
#         if izq=='#' and der=='#' and (abajo!='#'):
#             print('abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja)
#             return 0
#         if izq=='#' and ((der!='#')) and abajo=='#':
#             print('der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja)
#             return 0
#         if ((izq!='#')) and (der=='#') and abajo=='#':
#             print('izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')

#     if pi<pia and pj==pja:
#         if izq=='#' and der=='#' and (arriba!='#'):
#             print('arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja)
#             return 0
#         if izq=='#' and ((der!='#')) and arriba=='#':
#             print('der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja)
#             return 0
#         if ((izq!='#')) and (der=='#') and arriba=='#':
#             print('izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')

#     if pi==pia and pj>pja:
#         if der=='#' and abajo=='#' and (arriba!='#'):
#             print('arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja)
#             return 0
#         if der=='#' and ((abajo!='#')) and arriba=='#':
#             print('abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja)
#             return 0
#         if ((der!='#')) and (abajo=='#') and arriba=='#':
#             print('der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')
    
#     if pi==pia and pj<pja:
#         if izq=='#' and abajo=='#' and (arriba!='#'):
#             print('arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja)
#             return 0
#         if izq=='#' and ((abajo!='#')) and arriba=='#':
#             print('abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja)
#             return 0
#         if ((izq!='#')) and (abajo=='#') and arriba=='#':
#             print('izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')
#     return 0

# lab (pi,pj,pia,pja)

#*************************************************************************************************************************************






    # if izq=='#' and der=='#' and (abajo!='#'):
    #     print('abajo')
    #     l[pi][pj]='#'
    #     lab(pi+1,pj)
    #     return 0
    # if izq=='#' and ((der!='#')) and abajo=='#':
    #     print('der')
    #     l[pi][pj]='#'
    #     lab(pi,pj+1)
    #     return 0
    # if ((izq!='#')) and (der=='#') and abajo=='#':
    #     print('izq')
    #     l[pi][pj]='#'
    #     lab(pi,pj-1)
    #     return 0
    # if l[pi][pj]=='@':
    #     print('listo')
    # return 0

    


# Bifurcación izquierda-derecha

# def lab(pi, pj, pia, pja,xi,xj,yi,yj):
#     arriba = l[pi-1][pj]
#     abajo = l[pi+1][pj]
#     izq = l[pi][pj-1]
#     der = l[pi][pj+1]
#     print(pia,pja)
#     print(pi,pj)
    
#     if pi>pia and pj==pja:
#         if izq=='#' and der=='#' and (abajo!='#'):
#             print('abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and abajo=='#':
#             print('der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and abajo=='#':
#             print('izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and abajo=='#':
#             print('Bifurcación')
#             print('Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')
#             return 0
#         if ((izq=='#')) and (der=='#') and abajo=='#':
#             print('Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
        
#     if pi<pia and pj==pja:
#         if izq=='#' and der=='#' and (arriba!='#'):
#             print('arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and arriba=='#':
#             print('der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and arriba=='#':
#             print('izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq=='#')) and (der=='#') and arriba=='#':
#             print('Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')

#     if pi==pia and pj>pja:
#         if der=='#' and abajo=='#' and (arriba!='#'):
#             print('arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if der=='#' and ((abajo!='#')) and arriba=='#':
#             print('abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((der!='#')) and (abajo=='#') and arriba=='#':
#             print('der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((der=='#')) and (abajo=='#') and arriba=='#':
#             print('Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')
    
#     if pi==pia and pj<pja:
#         if izq=='#' and abajo=='#' and (arriba!='#'):
#             print('arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((abajo!='#')) and arriba=='#':
#             print('abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (abajo=='#') and arriba=='#':
#             print('izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('listo')
#             return 0
#         if ((izq=='#')) and (abajo=='#') and arriba=='#':
#             print('Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#     return 0

# lab (pi,pj,pia,pja,xi,xj,yi,yj)



## 4 Bifurcaciones derecha-izquierda arriba-abajo

# def lab(pi, pj, pia, pja,xi,xj,yi,yj):
#     arriba = l[pi-1][pj]
#     abajo = l[pi+1][pj]
#     izq = l[pi][pj-1]
#     der = l[pi][pj+1]
#     print(pia,pja)
#     print(pi,pj)
    
#     if pi>pia and pj==pja:
#         if izq=='#' and der=='#' and (abajo!='#'):
#             print('abajo-abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and abajo=='#':
#             print('abajo-der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and abajo=='#':
#             print('abajo-izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and abajo=='#':
#             print('abajo - Bifurcación')
#             print('abajo - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('abajo - listo')
#             return 0
#         if ((izq=='#')) and (der=='#') and abajo=='#':
#             print('abajo - Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
        
#     if pi<pia and pj==pja:
#         if l[pi][pj]=='@':
#             print('arriba - listo')
#             return 0
#         if izq=='#' and der=='#' and (arriba!='#'):
#             print('arriba - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and arriba=='#':
#             print('arriba - der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and arriba=='#':
#             print('arriba - izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and arriba=='#':
#             print('arriba - Bifurcación')
#             print('arriba - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi+1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq=='#')) and (der=='#') and arriba=='#':
#             print('arriba - Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0

#     if pi==pia and pj>pja:
#         if der=='#' and abajo=='#' and (arriba!='#'):
#             print('derecha - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if der=='#' and ((abajo!='#')) and arriba=='#':
#             print('derecha - abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((der!='#')) and (abajo=='#') and arriba=='#':
#             print('derecha - der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('derecha - listo')
#             return 0

#         if der=='#' and ((abajo!='#')) and (arriba!='#'):
#             print('arriba - Bifurcación')
#             print('arriba - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj-1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0


#         if ((der=='#')) and (abajo=='#') and arriba=='#':
#             print('derecha - Cerrado')
#             print('derecha - Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
        
    
#     if pi==pia and pj<pja:
#         if izq=='#' and abajo=='#' and (arriba!='#'):
#             print('izquierda - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((abajo!='#')) and arriba=='#':
#             print('izquierda - abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (abajo=='#') and arriba=='#':
#             print('izquierda - izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('izquierda - listo')
#             return 0


#         if izq=='#' and ((abajo!='#')) and (arriba!='#'):
#             print('arriba - Bifurcación')
#             print('arriba - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj+1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0


#         if ((izq=='#')) and (abajo=='#') and arriba=='#':
#             print('izquierda - Cerrado')
#             print('izquierda - Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#     return 0

# lab (pi,pj,pia,pja,xi,xj,yi,yj)



# Medias bifurcaciones en codo

# def lab(pi, pj, pia, pja,xi,xj,yi,yj):
#     arriba = l[pi-1][pj]
#     abajo = l[pi+1][pj]
#     izq = l[pi][pj-1]
#     der = l[pi][pj+1]
#     print(pia,pja)
#     print(pi,pj)
    
#     if pi>pia and pj==pja:
#         if izq=='#' and der=='#' and (abajo!='#'):
#             print('abajo-abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and abajo=='#':
#             print('abajo-der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and abajo=='#':
#             print('abajo-izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and abajo=='#':
#             print('abajo - Bifurcación')
#             print('abajo - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0



#         if izq=='#' and (der!='#') and (abajo!='#'):
#             print('abajo - Bifurcación')
#             print('abajo - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
        

#         if l[pi][pj]=='@':
#             print('abajo - listo')
#             return 0
#         if ((izq=='#')) and (der=='#') and abajo=='#':
#             print('abajo - Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
        





#     if pi<pia and pj==pja:
#         if l[pi][pj]=='@':
#             print('arriba - listo')
#             return 0
#         if izq=='#' and der=='#' and (arriba!='#'):
#             print('arriba - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and arriba=='#':
#             print('arriba - der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and arriba=='#':
#             print('arriba - izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and arriba=='#':
#             print('arriba - Bifurcación')
#             print('arriba - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi+1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0

#         if izq=='#' and (der!='#') and (arriba!='#'):
#             print('derecha - Bifurcación')
#             print('derecha - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi+1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0

#         if ((izq=='#')) and (der=='#') and arriba=='#':
#             print('arriba - Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0







#     if pi==pia and pj>pja:
#         if der=='#' and abajo=='#' and (arriba!='#'):
#             print('derecha - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if der=='#' and ((abajo!='#')) and arriba=='#':
#             print('derecha - abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((der!='#')) and (abajo=='#') and arriba=='#':
#             print('derecha - der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('derecha - listo')
#             return 0

#         if der=='#' and ((abajo!='#')) and (arriba!='#'):
#             print('derecha - Bifurcación')
#             print('derecha - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj-1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0

#         if (der!='#') and (abajo!='#') and arriba=='#':
#             print('derecha - Bifurcación')
#             print('derecha - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj-1
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0

#         if ((der=='#')) and (abajo=='#') and arriba=='#':
#             print('derecha - Cerrado')
#             print('derecha - Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
        
    




#     if pi==pia and pj<pja:
#         if izq=='#' and abajo=='#' and (arriba!='#'):
#             print('izquierda - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((abajo!='#')) and arriba=='#':
#             print('izquierda - abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (abajo=='#') and arriba=='#':
#             print('izquierda - izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('izquierda - listo')
#             return 0

#         if izq=='#' and ((abajo!='#')) and (arriba!='#'):
#             print('arriba - Bifurcación')
#             print('arriba - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj+1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0

#         if (izq!='#') and abajo=='#' and (arriba!='#'):
#             print('arriba - Bifurcación')
#             print('arriba - Vamos hacia la izquierda')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj+1
#             pia=pi
#             pja=pj
#             l[pi][pj-1]='#'
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0

#         if ((izq=='#')) and (abajo=='#') and arriba=='#':
#             print('izquierda - Cerrado')
#             print('izquierda - Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)


#     return 0

# lab (pi,pj,pia,pja,xi,xj,yi,yj)






## Bifurcaciones completas


# def lab(pi, pj, pia, pja,xi,xj,yi,yj):
#     arriba = l[pi-1][pj]
#     abajo = l[pi+1][pj]
#     izq = l[pi][pj-1]
#     der = l[pi][pj+1]
#     print(pia,pja)
#     print(pi,pj)
    
#     if pi>pia and pj==pja:
#         if izq=='#' and der=='#' and (abajo!='#'):
#             print('abajo-abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and abajo=='#':
#             print('abajo-der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and abajo=='#':
#             print('abajo-izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and abajo=='#':
#             print('abajo - Bifurcación')
#             print('abajo - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and (der!='#') and (abajo!='#'):
#             print('abajo - Bifurcación')
#             print('abajo - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if (izq!='#') and der=='#' and (abajo!='#'):
#             print('abajo - Bifurcación')
#             print('abajo - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi-1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('abajo - listo')
#             return 0
#         if ((izq=='#')) and (der=='#') and abajo=='#':
#             print('abajo - Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
        





#     if pi<pia and pj==pja:
#         if l[pi][pj]=='@':
#             print('arriba - listo')
#             return 0
#         if izq=='#' and der=='#' and (arriba!='#'):
#             print('arriba - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((der!='#')) and arriba=='#':
#             print('arriba - der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der=='#') and arriba=='#':
#             print('arriba - izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (der!='#') and arriba=='#':
#             print('arriba - Bifurcación')
#             print('arriba - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi+1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and (der!='#') and (arriba!='#'):
#             print('arriba - Bifurcación')
#             print('arriba - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi+1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if (izq!='#') and der=='#' and (arriba!='#'):
#             print('arriba - Bifurcación')
#             print('arriba - Vamos a la izquierda')
#             xi=pi
#             xj=pj
#             yi=pi+1
#             yj=pj
#             pia=pi
#             pja=pj
#             l[pi][pj-1]='#'
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq=='#')) and (der=='#') and arriba=='#':
#             print('arriba - Cerrado')
#             print('Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0







#     if pi==pia and pj>pja:
#         if der=='#' and abajo=='#' and (arriba!='#'):
#             print('derecha - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if der=='#' and ((abajo!='#')) and arriba=='#':
#             print('derecha - abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((der!='#')) and (abajo=='#') and arriba=='#':
#             print('derecha - der')
#             pia=pi
#             pja=pj
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('derecha - listo')
#             return 0
#         if der=='#' and ((abajo!='#')) and (arriba!='#'):
#             print('derecha - Bifurcación')
#             print('derecha - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj-1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if (der!='#') and (abajo!='#') and arriba=='#':
#             print('derecha - Bifurcación')
#             print('derecha - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj-1
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if (der!='#') and abajo=='#' and (arriba!='#'):
#             print('derecha - Bifurcación')
#             print('derecha - Vamos a la derecha')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj-1
#             pia=pi
#             pja=pj
#             l[pi][pj+1]='#'
#             lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
#             return 0            
#         if ((der=='#')) and (abajo=='#') and arriba=='#':
#             print('derecha - Cerrado')
#             print('derecha - Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)
#             return 0
        
    




#     if pi==pia and pj<pja:
#         if izq=='#' and abajo=='#' and (arriba!='#'):
#             print('izquierda - arriba')
#             pia=pi
#             pja=pj
#             lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if izq=='#' and ((abajo!='#')) and arriba=='#':
#             print('izquierda - abajo')
#             pia=pi
#             pja=pj
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq!='#')) and (abajo=='#') and arriba=='#':
#             print('izquierda - izq')
#             pia=pi
#             pja=pj
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if l[pi][pj]=='@':
#             print('izquierda - listo')
#             return 0
#         if izq=='#' and ((abajo!='#')) and (arriba!='#'):
#             print('izquierda - Bifurcación')
#             print('izquierda - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj+1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if (izq!='#') and abajo=='#' and (arriba!='#'):
#             print('izquierda - Bifurcación')
#             print('izquierda - Vamos hacia la izquierda')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj+1
#             pia=pi
#             pja=pj
#             l[pi][pj-1]='#'
#             lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
#             return 0
#         if (izq!='#') and (abajo!='#') and arriba=='#':
#             print('izquierda - Bifurcación')
#             print('izquierda - Vamos hacia abajo')
#             xi=pi
#             xj=pj
#             yi=pi
#             yj=pj+1
#             pia=pi
#             pja=pj
#             l[pi+1][pj]='#'
#             lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
#             return 0
#         if ((izq=='#')) and (abajo=='#') and arriba=='#':
#             print('izquierda - Cerrado')
#             print('izquierda - Regresamos')
#             pia=yi
#             pja=yj
#             pi=xi
#             pj=xj
#             lab(pi,pj,pia,pja,xi,xj,yi,yj)


#     return 0

# lab (pi,pj,pia,pja,xi,xj,yi,yj)









## Todos los caminos

def lab(pi, pj, pia, pja,xi,xj,yi,yj):
    arriba = l[pi-1][pj]
    abajo = l[pi+1][pj]
    izq = l[pi][pj-1]
    der = l[pi][pj+1]
    print(pia,pja)
    print(pi,pj)
    
    if pi>pia and pj==pja:
        if izq=='#' and der=='#' and (abajo!='#'):
            print('abajo-abajo')
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if izq=='#' and ((der!='#')) and abajo=='#':
            print('abajo-der')
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if ((izq!='#')) and (der=='#') and abajo=='#':
            print('abajo-izq')
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0
        if ((izq!='#')) and (der!='#') and abajo=='#':
            print('abajo - Bifurcación')
            print('abajo - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if izq=='#' and (der!='#') and (abajo!='#'):
            print('abajo - Bifurcación')
            print('abajo - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if (izq!='#') and der=='#' and (abajo!='#'):
            print('abajo - Bifurcación')
            print('abajo - Vamos hacia abajo')
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        

        if (izq!='#') and (der!='#') and (abajo!='#'):
            print('abajo - Tres caminos')
            print('abajo - Vamos hacia abajo')
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0




        if l[pi][pj]=='@':
            print('abajo - listo')
            return 0
        if ((izq=='#')) and (der=='#') and abajo=='#':
                print('abajo - Cerrado')
                print('Regresamos')
                pia=yi
                pja=yj
                pi=xi
                pj=xj
                lab(pi,pj,pia,pja,xi,xj,yi,yj)
                return 0
        





    if pi<pia and pj==pja:
        if l[pi][pj]=='@':
            print('arriba - listo')
            return 0
        if izq=='#' and der=='#' and (arriba!='#'):
            print('arriba - arriba')
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if izq=='#' and ((der!='#')) and arriba=='#':
            print('arriba - der')
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if ((izq!='#')) and (der=='#') and arriba=='#':
            print('arriba - izq')
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0
        if ((izq!='#')) and (der!='#') and arriba=='#':
            print('arriba - Bifurcación')
            print('arriba - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if izq=='#' and (der!='#') and (arriba!='#'):
            print('arriba - Bifurcación')
            print('arriba - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if (izq!='#') and der=='#' and (arriba!='#'):
            print('arriba - Bifurcación')
            print('arriba - Vamos a la izquierda')
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0
        
        if (izq!='#') and (der!='#') and (arriba!='#'):
            print('arriba - Tres caminos')
            print('arriba - Vamos a la izquierda')
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0




        if ((izq=='#')) and (der=='#') and arriba=='#':
            print('arriba - Cerrado')
            print('Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            lab(pi,pj,pia,pja,xi,xj,yi,yj)
            return 0







    if pi==pia and pj>pja:
        if der=='#' and abajo=='#' and (arriba!='#'):
            print('derecha - arriba')
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if der=='#' and ((abajo!='#')) and arriba=='#':
            print('derecha - abajo')
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if ((der!='#')) and (abajo=='#') and arriba=='#':
            print('derecha - der')
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if l[pi][pj]=='@':
            print('derecha - listo')
            return 0
        if der=='#' and ((abajo!='#')) and (arriba!='#'):
            print('derecha - Bifurcación')
            print('derecha - Vamos hacia abajo')
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if (der!='#') and (abajo!='#') and arriba=='#':
            print('derecha - Bifurcación')
            print('derecha - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        if (der!='#') and abajo=='#' and (arriba!='#'):
            print('derecha - Bifurcación')
            print('derecha - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0
        

        if (der!='#') and (abajo!='#') and (arriba!='#'):
            print('derecha - Tres caminos')
            print('derecha - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
            return 0   




        if ((der=='#')) and (abajo=='#') and arriba=='#':
            print('derecha - Cerrado')
            print('derecha - Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            lab(pi,pj,pia,pja,xi,xj,yi,yj)
            return 0
        
    




    if pi==pia and pj<pja:
        if izq=='#' and abajo=='#' and (arriba!='#'):
            print('izquierda - arriba')
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if izq=='#' and ((abajo!='#')) and arriba=='#':
            print('izquierda - abajo')
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if ((izq!='#')) and (abajo=='#') and arriba=='#':
            print('izquierda - izq')
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0
        if l[pi][pj]=='@':
            print('izquierda - listo')
            return 0
        if izq=='#' and ((abajo!='#')) and (arriba!='#'):
            print('izquierda - Bifurcación')
            print('izquierda - Vamos hacia abajo')
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0
        if (izq!='#') and abajo=='#' and (arriba!='#'):
            print('izquierda - Bifurcación')
            print('izquierda - Vamos hacia la izquierda')
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0
        if (izq!='#') and (abajo!='#') and arriba=='#':
            print('izquierda - Bifurcación')
            print('izquierda - Vamos hacia abajo')
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0

        if (izq!='#') and (abajo!='#') and (arriba!='#'):
            print('izquierda - Tres caminos')
            print('izquierda - Vamos hacia abajo')
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj)
            return 0





        if abajo=='@':
            print('listo')
            print(pi+1,pj)
        if ((izq=='#')) and (abajo=='#') and arriba=='#':
            print('izquierda - Cerrado')
            print('izquierda - Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            lab(pi,pj,pia,pja,xi,xj,yi,yj)
            return 0


    return 0

lab (pi,pj,pia,pja,xi,xj,yi,yj)