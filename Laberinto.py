# Llama al archivo y guarda en una matriz el laberinto

myfile = open("texto.txt", "r")
myline = myfile.readline()
l=[]
while myline:
    l.append(list(myline))
    myline = myfile.readline()
myfile.close() 

# Busca la entrada y guarda sus coordenadas

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

xi=0
xj=0
yi=0
yj=0

# Valores para reinicio. Estos no se modifican
pier=Ei
pjer=Ej
pir=Ei+1
pjr=Ej

#Laberinto
## Hasta las 4 Bifurcaciones derecha-izquierda arriba-abajo

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
            print('derecha - Bifurcación')
            print('derecha - Vamos a la derecha')
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj)
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
            print('arriba - Bifurcación')
            print('arriba - Vamos hacia abajo')
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
            print('arriba - Bifurcación')
            print('arriba - Vamos hacia la izquierda')
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj)
            return 0

        


        if ((izq=='#')) and (abajo=='#') and arriba=='#':
            print('izquierda - Cerrado')
            print('izquierda - Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            lab(pi,pj,pia,pja,xi,xj,yi,yj)





    return 0

lab (pi,pj,pia,pja,xi,xj,yi,yj)

