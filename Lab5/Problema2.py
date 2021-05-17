f = open("2.in")
g = open("2.out","w")

sir_afisare = ""

# Vrem sa avem obiecte de tip Punct care sa aiba coordonatele x si y
class Punct:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return  str(self.x) +  " "+ str(self.y)



def test_orientare(P,Q,R):
    """Functie care testeaza natura virajului pentru 3 puncte date"""
    naturaViraj = ""

    # Initializam matricea
    a = [[1, 1, 1], [P.x, Q.x, R.x], [P.y, Q.y, R.y]]

    # Calculam determinantul folosind regula lui Sarrus
    det = a[0][0]*a[1][1]*a[2][2] + a[0][2]*a[1][0]*a[2][1] + a[0][1]*a[1][2]*a[2][0] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]
    if det == 0:
        naturaViraj = "coliniare"
    elif det < 0:
        naturaViraj = "dreapta"
    else:
        naturaViraj = "stanga"

    return naturaViraj



n = int(f.readline())

P = [] # lista mea de puncte
poz = 0
minim = 99999999999

for i in range(0,n):
    Xp, Yp = (f.readline()).split()
    Xp = int(Xp)
    Yp = int(Yp)
    P.append(Punct(Xp,Yp))
    if Xp < minim: # Vrem sa aflam elementul cu cel mai mic x, adica punctul cel mai din stanga
        minim = Xp
        poz = i

f.close()
P = P[poz:] + P[:poz] # "rotim" lista punctelor astfel incat primul element sa fie cel mai din stanga punct

# Inial punem in lista primele 2 puncte
frontiera = [P[0],P[1]]


for i in range(2,n):
    # Adaugam de fiecare data un nou punct din lista
    frontiera.append(P[i])

    # Cat timp ultimele 3 puncte din frontiera nu formeaza un viraj la stanga elimin penultimul element
    while len(frontiera) > 2 and test_orientare(frontiera[len(frontiera)-3],frontiera[len(frontiera)-2],frontiera[len(frontiera)-1]) != "stanga":
        frontiera.pop(len(frontiera) - 2)


for i in range(0, len(frontiera)):
    sir_afisare += str(frontiera[i]) + "\n"

g.write(sir_afisare)
g.close()
