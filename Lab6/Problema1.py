f = open("1_in")
g = open("1_out","w")

import random

n = int(f.readline()) # n = numarul de puncte al poligonului
sir_afisare = ""

class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if float(self.x) == int(self.x) and float(self.y) == int(self.y):
            return "(" + str(int(self.x)) + ", " + str(int(self.y)) + ")"
        else:
            return  "(" + str(self.x) + ", " + str(self.y) + ")"

def test_orientare(P, Q, R):
    naturaViraj = ""
    # Initializam matricea
    a = [[1, 1, 1], [P.x, Q.x, R.x], [P.y, Q.y, R.y]]
    #print(a)
    # Calculam determinantul folosind regula lui Sarrus
    det = a[0][0] * a[1][1] * a[2][2] + a[0][2] * a[1][0] * a[2][1] + a[0][1] * a[1][2] * a[2][0] - a[0][2] * a[1][1] * \
          a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1]

    if det > -0.01 and det < 0.01: # E posibil sa avem o eroare de cateva zecimale
        naturaViraj = "coliniare"
    elif det < 0:
        naturaViraj = "dreapta"
    else:
        naturaViraj = "stanga"

    return naturaViraj





def orientare(P, Q, R):
    # Functie care stabileste sensul punctelor
    val = (float(Q.y - P.y) * (R.x - Q.x)) - (float(Q.x - P.x) * (R.y - Q.y))

    if (val > 0):
        return 1 # In sensul acelor de ceasornic

    elif (val < 0):
        return 2 # In sens trigonometric

    else:
        return 0 # Puncte coliniare



def verif_intersectie(A, B, C, D):
    #Functie care verifica daca segmentul [AB] intersecteaza segmentul [CD]
    # Ne folosim de functia de orientare

    o1 = orientare(A, B, C)
    o2 = orientare(A, B, D)
    o3 = orientare(C, D, A)
    o4 = orientare(C, D, B)

    if ((o1 != o2) and (o3 != o4)):
        return True

    return False





x_maxim = -99999999
y_maxim = -99999999

P = []
muchii = []
for i in range(n):
    Xp, Yp = f.readline().split()
    Xp = float(Xp)
    Yp = float(Yp)

    if Xp > x_maxim:
        x_maxim = Xp
    if Yp > y_maxim:
        y_maxim = Yp

    Punctul = Punct(Xp,Yp)

    P.append(Punctul)

    if i >= 1:
        muchii.append([P[i-1],P[i]])

muchii.append([P[n-1],P[0]])


# Luam un punct martor.Vrem sa ne asiguram ca este in afara poligonului asa ca generam niste
#coordonate random si ne asiguram ca acestea sunt mai mari decat x-ul maxim si y-ul maxim
# care apar in poligon, astfel martorul va fi situat in partea din dreapta sus

Xm = random.randrange(x_maxim + 0,x_maxim + 1000)
Ym = random.randrange(y_maxim + 0,y_maxim + 1000)
M = Punct(Xm,Ym)


print(M)

nr_Q = int(f.readline())

for l in range(nr_Q):
    gasit = False
    Xq, Yq = f.readline().split()
    Xq = float(Xq)
    Yq = float(Yq)
    Q = Punct(Xq,Yq)


    for j in range(len(muchii)):

        if(test_orientare(muchii[j][0],Q,muchii[j][1]) == "coliniare"):
            """Daca punctul este coliniar cu capetele laturii segmentului
            verific si daca acesta ase afla pe latura
            """
            if muchii[j][0].y == Q.y == muchii[j][1].y:
                if (muchii[j][0].x <= Q.x <= muchii[j][1].x) or (muchii[j][0].x >= Q.x >= muchii[j][1].x):
                    sir_afisare += str(Q) + " - pe una dintre laturi\n"
                    gasit = True
                    break
            elif muchii[j][0].x == Q.x == muchii[j][1].x:
                if (muchii[j][0].y <= Q.y <= muchii[j][1].y) or (muchii[j][0].y >= Q.y >= muchii[j][1].y):
                    sir_afisare += str(Q) + " - pe una dintre laturi\n"
                    gasit = True
                    break
    if gasit == False: # Daca punctul nu se afla pe niciuna din laturile poligonului il cautam in afara si in interiorul acestuia
    # Verific de cate ori se intersecteaza segmentul [MQ], format din martor si punctul nostru cu o latura a poligonului
        nr_intersectii = 0
        for j in range(len(muchii)):
            A = muchii[j][0]
            B = muchii[j][1]
            if verif_intersectie(A,B,M,Q) == True:
                nr_intersectii += 1
            #print(A,B,M,Q,verif_intersectie(A,B,M,Q))

        # Daca am un numar impar de intersectii inseamna ca ultima data segmentul meu "a intrat" in poligon, deci va fi in interiorul acestuia
        # Daca este numar par inseamna ca segmentul nu a trecut deloc prin poligon, sau a intrat si ultima data a iesit, deci este in exterior
        if nr_intersectii % 2 == 0:
            sir_afisare += str(Q) + " - exterior\n"
        else:
            sir_afisare += str(Q) + " - interior\n"





g.write(sir_afisare)
f.close()
g.close()

