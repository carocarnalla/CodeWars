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
pia = Ei
pja = Ej

pi = Ei + 1
pj = Ej

entradai=Ei
entradaj=Ej

inicioi=Ei+1
inicioj=Ej


# Coordenadas de bifurcación

xi = inicioi
xj = inicioj
yi = entradai
yj = entradaj

# Coordenadas bifurcación anterior

ai = inicioi
aj = inicioj
bi = entradai
bj = entradaj

#Laberinto
## Todas las bifurcaciones

def lab (pi, pj, pia, pja,xi,xj,yi,yj,ai,aj,bi,bj):
    arriba = l[pi-1][pj]
    abajo = l[pi+1][pj]
    izq = l[pi][pj-1]
    der = l[pi][pj+1]
    print(pia,pja)
    print(pi,pj)
    
    if pi>pia and pj==pja:

        if abajo=='@':
            print('listo')
            print(pi+1,pj)
            return 0

        if izq=='@':
            print('listo')
            print(pi,pj-1)
            return 0

        if der=='@':
            print('listo')
            print(pi,pj+1)
            return 0
            
        if izq=='#' and der=='#' and (abajo!='#'):
            print('abajo-abajo')
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if izq=='#' and ((der!='#')) and abajo=='#':
            print('abajo-der')
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq!='#')) and (der=='#') and abajo=='#':
            print('abajo-izq')
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq!='#')) and (der!='#') and abajo=='#':
            print('abajo - Bifurcación')
            print('abajo - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0
            

        if izq=='#' and (der!='#') and (abajo!='#'):
            print('abajo - Bifurcación')
            print('abajo - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (izq!='#') and der=='#' and (abajo!='#'):
            print('abajo - Bifurcación')
            print('abajo - Vamos hacia abajo')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (izq!='#') and (der!='#') and (abajo!='#'):
            print('abajo - Tres caminos')
            print('abajo - Vamos hacia abajo')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi-1
            yj=pj
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq=='#')) and (der=='#') and abajo=='#':
                print('abajo - Cerrado')
                print('Regresamos')
                pia=yi
                pja=yj
                pi=xi
                pj=xj
                xi=ai
                xj=aj
                yi=bi
                yj=bj
                lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
                return 0



    if pi<pia and pj==pja:

        if arriba=='@':
            print('listo')
            print(pi-1,pj)
            return 0

        if izq=='@':
            print('listo')
            print(pi,pj-1)
            return 0

        if der=='@':
            print('listo')
            print(pi,pj+1)
            return 0
        
        if izq=='#' and der=='#' and (arriba!='#'):
            print('arriba - arriba')
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if izq=='#' and ((der!='#')) and arriba=='#':
            print('arriba - der')
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq!='#')) and (der=='#') and arriba=='#':
            print('arriba - izq')
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq!='#')) and (der!='#') and arriba=='#':
            print('arriba - Bifurcación')
            print('arriba - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if izq=='#' and (der!='#') and (arriba!='#'):
            print('arriba - Bifurcación')
            print('arriba - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (izq!='#') and der=='#' and (arriba!='#'):
            print('arriba - Bifurcación')
            print('arriba - Vamos a la izquierda')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0
        
        if (izq!='#') and (der!='#') and (arriba!='#'):
            print('arriba - Tres caminos')
            print('arriba - Vamos a la izquierda')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi+1
            yj=pj
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq=='#')) and (der=='#') and arriba=='#':
            print('arriba - Cerrado')
            print('Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            xi=ai
            xj=aj
            yi=bi
            yj=bj
            lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0



    if pi==pia and pj>pja:

        if abajo=='@':
            print('listo')
            print(pi+1,pj)
            return 0

        if arriba=='@':
            print('listo')
            print(pi-1,pj)
            return 0

        if der=='@':
            print('listo')
            print(pi,pj+1)
            return 0

        if der=='#' and abajo=='#' and (arriba!='#'):
            print('derecha - arriba')
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if der=='#' and ((abajo!='#')) and arriba=='#':
            print('derecha - abajo')
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((der!='#')) and (abajo=='#') and arriba=='#':
            print('derecha - der')
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if der=='#' and ((abajo!='#')) and (arriba!='#'):
            print('derecha - Bifurcación')
            print('derecha - Vamos hacia abajo')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (der!='#') and (abajo!='#') and arriba=='#':
            print('derecha - Bifurcación')
            print('derecha - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (der!='#') and abajo=='#' and (arriba!='#'):
            print('derecha - Bifurcación')
            print('derecha - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0
        
        if (der!='#') and (abajo!='#') and (arriba!='#'):
            print('derecha - Tres caminos')
            print('derecha - Vamos a la derecha')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj-1
            pia=pi
            pja=pj
            l[pi][pj+1]='#'
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0   

        if ((der=='#')) and (abajo=='#') and arriba=='#':
            print('derecha - Cerrado')
            print('derecha - Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            xi=ai
            xj=aj
            yi=bi
            yj=bj
            lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0
        


    if pi==pia and pj<pja:

        if abajo=='@':
            print('listo')
            print(pi+1,pj)
            return 0

        if arriba=='@':
            print('listo')
            print(pi-1,pj)
            return 0

        if izq=='@':
            print('listo')
            print(pi,pj-1)
            return 0

        if izq=='#' and abajo=='#' and (arriba!='#'):
            print('izquierda - arriba')
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if izq=='#' and ((abajo!='#')) and arriba=='#':
            print('izquierda - abajo')
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if ((izq!='#')) and (abajo=='#') and arriba=='#':
            print('izquierda - izq')
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0
        
        if izq=='#' and ((abajo!='#')) and (arriba!='#'):
            print('izquierda - Bifurcación')
            print('izquierda - Vamos hacia abajo')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (izq!='#') and abajo=='#' and (arriba!='#'):
            print('izquierda - Bifurcación')
            print('izquierda - Vamos hacia la izquierda')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi][pj-1]='#'
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (izq!='#') and (abajo!='#') and arriba=='#':
            print('izquierda - Bifurcación')
            print('izquierda - Vamos hacia abajo')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0

        if (izq!='#') and (abajo!='#') and (arriba!='#'):
            print('izquierda - Tres caminos')
            print('izquierda - Vamos hacia abajo')
            ai=xi
            aj=xj
            bi=yi
            bj=yj
            xi=pi
            xj=pj
            yi=pi
            yj=pj+1
            pia=pi
            pja=pj
            l[pi+1][pj]='#'
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0


        if ((izq=='#')) and (abajo=='#') and arriba=='#':
            print('izquierda - Cerrado')
            print('izquierda - Regresamos')
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            xi=ai
            xj=aj
            yi=bi
            yj=bj
            lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)
            return 0


    return 0

lab (pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj)