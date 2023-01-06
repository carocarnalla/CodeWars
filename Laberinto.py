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