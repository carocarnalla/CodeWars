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

di=0
dj=0


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

def lab (pi, pj, pia, pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj):
    arriba = l[pi-1][pj]
    abajo = l[pi+1][pj]
    izq = l[pi][pj-1]
    der = l[pi][pj+1]
    
    if pi>pia and pj==pja:

        if abajo=='@':
            print(pi+1,pj)
            return 0

        if izq=='@':
            print(pi,pj-1)
            return 0

        if der=='@':
            print(pi,pj+1)
            return 0
            
        if izq=='#' and der=='#' and (abajo!='#'):
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if izq=='#' and ((der!='#')) and abajo=='#':
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq!='#')) and (der=='#') and abajo=='#':
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq!='#')) and (der!='#') and abajo=='#':
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0
            

        if izq=='#' and (der!='#') and (abajo!='#'):
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (izq!='#') and der=='#' and (abajo!='#'):
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
            di=pi+1
            dj=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (izq!='#') and (der!='#') and (abajo!='#'):
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
            di=pi+1
            dj=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq=='#')) and (der=='#') and abajo=='#':
                pia=yi
                pja=yj
                pi=xi
                pj=xj
                xi=ai
                xj=aj
                yi=bi
                yj=bj
                l[di][dj]='#'
                lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
                return 0



    if pi<pia and pj==pja:

        if arriba=='@':
            print(pi-1,pj)
            return 0

        if izq=='@':
            print(pi,pj-1)
            return 0

        if der=='@':
            print(pi,pj+1)
            return 0
        
        if izq=='#' and der=='#' and (arriba!='#'):
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if izq=='#' and ((der!='#')) and arriba=='#':
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq!='#')) and (der=='#') and arriba=='#':
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq!='#')) and (der!='#') and arriba=='#':
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if izq=='#' and (der!='#') and (arriba!='#'):
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (izq!='#') and der=='#' and (arriba!='#'):
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
            di=pi
            dj=pj-1
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0
        
        if (izq!='#') and (der!='#') and (arriba!='#'):
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
            di=pi
            dj=pj-1
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq=='#')) and (der=='#') and arriba=='#':
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            xi=ai
            xj=aj
            yi=bi
            yj=bj
            l[di][dj]='#'
            lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0



    if pi==pia and pj>pja:

        if abajo=='@':
            print(pi+1,pj)
            return 0

        if arriba=='@':
            print(pi-1,pj)
            return 0

        if der=='@':
            print(pi,pj+1)
            return 0

        if der=='#' and abajo=='#' and (arriba!='#'):
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if der=='#' and ((abajo!='#')) and arriba=='#':
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((der!='#')) and (abajo=='#') and arriba=='#':
            pia=pi
            pja=pj
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if der=='#' and ((abajo!='#')) and (arriba!='#'):
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
            di=pi+1
            dj=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (der!='#') and (abajo!='#') and arriba=='#':
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (der!='#') and abajo=='#' and (arriba!='#'):
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0
        
        if (der!='#') and (abajo!='#') and (arriba!='#'):
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
            di=pi
            dj=pj+1
            lab(pi,pj+1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0   

        if ((der=='#')) and (abajo=='#') and arriba=='#':
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            xi=ai
            xj=aj
            yi=bi
            yj=bj
            l[di][dj]='#'
            lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0
        


    if pi==pia and pj<pja:

        if abajo=='@':
            print(pi+1,pj)
            return 0

        if arriba=='@':
            print(pi-1,pj)
            return 0

        if izq=='@':
            print(pi,pj-1)
            return 0

        if izq=='#' and abajo=='#' and (arriba!='#'):
            pia=pi
            pja=pj
            lab(pi-1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if izq=='#' and ((abajo!='#')) and arriba=='#':
            pia=pi
            pja=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq!='#')) and (abajo=='#') and arriba=='#':
            pia=pi
            pja=pj
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0
        
        if izq=='#' and ((abajo!='#')) and (arriba!='#'):
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
            di=pi+1
            dj=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (izq!='#') and abajo=='#' and (arriba!='#'):
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
            di=pi
            dj=pj-1
            lab(pi,pj-1,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (izq!='#') and (abajo!='#') and arriba=='#':
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
            di=pi+1
            dj=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if (izq!='#') and (abajo!='#') and (arriba!='#'):
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
            di=pi+1
            dj=pj
            lab(pi+1,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

        if ((izq=='#')) and (abajo=='#') and arriba=='#':
            pia=yi
            pja=yj
            pi=xi
            pj=xj
            xi=ai
            xj=aj
            yi=bi
            yj=bj
            l[di][dj]='#'
            lab(pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)
            return 0

    return 0

lab (pi,pj,pia,pja,xi,xj,yi,yj,ai,aj,bi,bj,di,dj)



for i in l:
    for j in i:
        print(j, end=" ")
    print()