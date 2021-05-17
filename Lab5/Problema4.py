f = open("4.in")
g = open("4.out","w")



class Punct:
    def __init__(self,nume,x,y):
        self.x = x
        self.y = y
        self.nume = nume

    # def __str__(self):
    #     return  self.nume + " x = " + str(self.x) +  ", y = "+ str(self.y)
    def __str__(self):
        return  str(self.x) +  " "+ str(self.y)

def test_orientare(P,Q,R):
    """Functie care testeaza natura virajului pentru 3 puncte date"""
    naturaViraj = ""

    # Initializam matricea
    a = [[1, 1, 1], [P.x, Q.x, R.x], [P.y, Q.y, R.y]]

    # Calculam determinantul folosind regula lui Sarrus
    det = a[0][0]*a[1][1]*a[2][2] + a[0][2]*a[1][0]*a[2][1] + a[0][1]*a[1][2]*a[2][0] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]

    if det < 0:
        naturaViraj = "dreapta"
    elif det > 0:
        naturaViraj = "stanga"
    else:
        naturaViraj = "coliniare"


    return naturaViraj



def distanta(A,B):
    "Functie care calculeaza distanta dintre 2 puncte (costul)"
    return ((B.x - A.x)**2 + (B.y - A.y)**2)**0.5


def acoperireConvexa(P):
    """Obtinem acoperirea convexa a multimii de puncte folosind algoritmul din curs, in O(n^3)"""
    E = []  # lista muchilor orientate din acoperirea convexa

    valid = False
    for i in range(0, len(P)):
        for j in range(0, len(P)):
            if i != j:
                valid = True
                for r in range(0, len(P)):
                    if r != i and r != j:
                        if test_orientare(P[i], P[j], P[r]) == "dreapta" :
                            valid = False
                if valid == True:
                    E.append((P[i], P[j]))


    frontiera = []
    frontiera.append(E[0][0])
    frontiera.append(E[0][1])

    nr_puncte = len(E)

    # Vrem sa retinem frontiera si sub forma de puncte
    while nr_puncte - 2 != 0:
        punct_cautat = frontiera[len(frontiera) - 1]
        for i in range(1, len(E)):
            if E[i][0] == punct_cautat:
                frontiera.append(E[i][1])
                nr_puncte -= 1

    return frontiera

n = int(f.readline())
sir_afisare = ""
P = []
x_minim = 999999999
St = 0
for i in range(0,n):
    Xp,Yp = f.readline().split()
    Xp = int(Xp)
    Yp = int(Yp)
    if Xp < x_minim:
        x_minim = Xp
        St = i  # Aflu elementul cel mai din stanga, adica cel cu x-ul cel mai mic
    Punctul = Punct("P" + str(i+1),Xp,Yp)
    P.append(Punctul)

frontiera = acoperireConvexa(P)
interior = [punct for punct in P if punct not in frontiera] # Lista de puncte din interiorul poligonului, care nu se afla pe frontiera


Stop = False
while Stop == False:
    # print("Frontiera")
    # for i in range(0, len(frontiera)):
    #     print(frontiera[i])

    muchii = [] # Aici vom retine muchiile care alcatuiesc frontiera poligonului
    for i in range(0,len(frontiera)-1):
        muchii.append([frontiera[i],frontiera[i+1]])
    muchii.append([frontiera[len(frontiera)-1],frontiera[0]])

    triplete = []


    for r in range(0,len(interior)):
       # print(interior[r])

        R = interior[r]
        minim = 9999999999

        for i in range(0,len(muchii)): # Pentru fiecare punct din interiorul poligonului vrem sa gasim muchia cea mai apropiata
            I = muchii[i][0]
            J = muchii[i][1]
            if( distanta(I,R) + distanta(R,J) - distanta(I,J) ) < minim: # Ne folosim de prima metrica din algoritm pt a afla muchia cea mai apropiata
                minim = distanta(I,R) + distanta(R,J) - distanta(I,J)
                triplet = [I,J,R] # Retinem punctul interior si capetele muchiei sub forma unui triplet

        triplete.append(triplet)

    # for i in range(len(triplete)):
    #     print(triplete[i][0],triplete[i][1],triplete[i][2])

    metrica_minim = 999999999

    for i in range(len(triplete)): # Cautam punctul interior cu metrica cea mai mica
        I = triplete[i][0]
        J = triplete[i][1]
        R = triplete[i][2]
        metrica = (distanta(I,R) + distanta(R,J))/distanta(I,J)
        if metrica < metrica_minim:
            metrica_minim = metrica
            triplet_minim = triplete[i]

    #print(triplet_minim[0],triplet_minim[1],triplet_minim[2])

    poz = 0
    for i in range(0,len(frontiera)):  # Vreau sa aflu pozitia unde voi insera punctul
        if frontiera[i] == triplet_minim[0]:
            poz = i+1
            break

    # Dupa ce am gasit punctul pentru care metrica mea este minima si pozitia unde trebuie pus, il inserez pe traseu
    frontiera.insert(poz,triplet_minim[2])

    # print("Frontiera")
    # for i in range(0, len(frontiera)):
    #     print(frontiera[i])

    interior.remove(triplet_minim[2]) # Sterg punctul din lista de puncte interioare

    # print("Interior")
    # for i in range(0, len(interior)):
    #     print(interior[i])

    if not interior:  # Daca am adaugat toate nodurile interioare pe traseu algoritmul meu se opreste
        stop = True
        break



frontiera = frontiera[St:] + frontiera[0:St] # Rotim drumul pentru ca primul element sa fie cel mai din stanga
frontiera.append(frontiera[0]) # Punem la sfarsit si primul element deoarece aici ne vom intoarce pe traseul nostru complet
for i in range(0, len(frontiera)):
    sir_afisare += str(frontiera[i]) + "\n"

g.write(sir_afisare)