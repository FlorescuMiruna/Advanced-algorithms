f = open("2_in")
g = open("2_out","w")

sir_afisare = ""

# Vrem sa avem obiecte de tip Punct care sa aiba coordonatele x si y
class Punct:
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return  self.name + " "  + str(self.x) +  " "+ str(self.y)

nr_poligoane = int(f.readline())

for l in range(nr_poligoane):

    n = int(f.readline())
    P = [] # Lista mea de puncte
    X_minim = 999999
    Y_minim = 999999
    X_maxim = -999999
    Y_maxim = -999999

    for i in range(n):
        Xp,Yp = f.readline().split()
        Xp = float(Xp)
        Yp = float(Yp)
        P.append(Punct(Xp,Yp,"P" + str(i+1)))

        if Xp < X_minim:
            X_minim = Xp
            poz_X_minim = i
        if Yp < Y_minim:
            Y_minim = Yp
            poz_Y_minim = i

        if Xp > X_maxim:
            X_maxim = Xp
            poz_X_maxim = i
        if Yp > Y_maxim:
            Y_maxim = Yp
            poz_Y_maxim = i


    print(P)

    for i in range(n):
        print(P[i])


    """Ca poligonul sa poata fi X-monoton trebuie sa putem "cobori" in 2 moduri din varful de sus la varful cel mai de jos
    fara sa urcam deloc inapoi, astfel impartim poligonul in 2 frontiere, una care coboara de la cel mai de sus punct la cel
    mai de jos si una care urca la cel mai de jos la cel mai de sus si verificam pentru fiecare daca indeplineste conditia.
    
    Pentru poligoanele Y-monotone aplicam acelasi principiu, doar ca ne vom folosi de coordonatele x, de cel mai din stanga punct
    si de cel mai din dreaota"""

    if poz_Y_maxim < poz_Y_minim:
        Parcurgere_sus_jos = P[poz_Y_maxim:poz_Y_minim+1]
        print(poz_Y_maxim)
        Parcurgere_jos_sus = P[poz_Y_minim :n] + P[0:poz_Y_maxim +1]
    else:
        Parcurgere_sus_jos = P[poz_Y_maxim:n] + P[0:poz_Y_minim+1]
        Parcurgere_jos_sus = P[poz_Y_minim:poz_Y_maxim+1]

    if poz_X_minim < poz_X_maxim:
        Parcurgere_stanga_dreapta = P[poz_X_minim:poz_X_maxim+1]
        Parcurgere_dreapta_stanga = P[poz_X_maxim:n] + P[0:poz_X_minim+1]
    else:
        Parcurgere_stanga_dreapta = P[poz_X_minim:n] + P[0:poz_X_maxim+1]
        Parcurgere_dreapta_stanga = P[poz_X_maxim:poz_X_minim+1]


    Y_monoton = True
    X_monoton = True

    print("Parcurgere_stanga_dreapta")
    for i in range(len(Parcurgere_stanga_dreapta)):
        print(Parcurgere_stanga_dreapta[i])

    print("Parcurgere_dreapta_stanga")
    for i in range(len(Parcurgere_dreapta_stanga)):
        print(Parcurgere_dreapta_stanga[i])

    for i in range(1,len(Parcurgere_sus_jos)):
        if(Parcurgere_sus_jos[i].y >= Parcurgere_sus_jos[i-1].y):
            Y_monoton = False
            break

    for i in range(1,len(Parcurgere_jos_sus)):
        if(Parcurgere_jos_sus[i].y <= Parcurgere_jos_sus[i-1].y):
            Y_monoton = False
            break

    for i in range(1,len(Parcurgere_stanga_dreapta)):
        if(Parcurgere_stanga_dreapta[i].x >= Parcurgere_stanga_dreapta[i-1].x):
            X_monoton = False
            break

    for i in range(1,len(Parcurgere_dreapta_stanga)):
        if(Parcurgere_dreapta_stanga[i].x <= Parcurgere_dreapta_stanga[i-1].x):
            X_monoton = False
            break

    sir_afisare += "Poligonul " + str(l+1) + ":\n"
    if X_monoton:
        sir_afisare += "este x-monoton\n"
    else:
        sir_afisare += "nu este x-monoton\n"

    if Y_monoton:
        sir_afisare += "este y-monoton\n"
    else:
        sir_afisare += "nu este y-monoton\n"



g.write(sir_afisare)

f.close()
g.close()
