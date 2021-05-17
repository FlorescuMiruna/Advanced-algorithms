f = open("4_in")
g = open("4_out","w")


import numpy as np
sir_afisare = "" # Ne ajuta sa scriem rezultatul in fisier

# Vrem sa avem obiecte de tip Punct care sa aiba coordonatele x si y
class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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





def pozitie_relativa(A,B,C,D):
    """Calculam determinantul de ordinul 4"""

    mat = np.array([[A.x,A.y,A.x**2 + A.y**2,1], [B.x,B.y,B.x**2 + B.y**2,1],[C.x,C.y,C.x**2 + C.y**2,1],[D.x,D.y,D.x**2 + D.y**2,1]])
    det = np.linalg.det(mat)
    det = np.around(det, decimals=4)

    if det > 0:
        return "in interior" # Daca determinantul e mai mare decat 0, punctul D se afla in interiorul cercului circumscris triunghiului ABC
    elif det < 0:
        return "in exterior" # Daca e mai mic decat 0 se afla in exterior
    elif det == 0:
        return "pe cerc" # Daca este egal cu 0 va fi chiar pe cerc


Xa, Ya = (f.readline()).split()
A = Punct(int(Xa),int(Ya))

Xb, Yb = (f.readline()).split()
B = Punct(int(Xb),int(Yb))

Xc, Yc = (f.readline()).split()
C = Punct(int(Xc),int(Yc))

Xd, Yd = (f.readline()).split()
D = Punct(int(Xd),int(Yd))

# Testam muchia AC
if test_orientare(A,B,C) == "stanga":
# Avem nevoie ca cele 3 puncte sa formeze un viraj la stanga, daca nu este viraj la stanga trebuie sa ne folosim de triunghiul CBA
    if pozitie_relativa(A,B,C,D) == "in interior":
        sir_afisare += "AC este muchie ilegala\n"
    else:
        sir_afisare += "AC nu este muchie ilegala\n"
else:
    if pozitie_relativa(C,B,A,D) == "in interior":
        sir_afisare += "AC este muchie ilegala\n"
    else:
        sir_afisare += "AC nu este muchie ilegala\n"

# Testam muchia BD
if test_orientare(B,A,D) == "stanga":
# Avem nevoie ca cele 3 puncte sa formeze un viraj la stanga, daca nu este viraj la stanga trebuie sa ne folosim de triunghiul DAB
    if pozitie_relativa(B,A,D,C) == "in interior":
        sir_afisare += "BD este muchie ilegala\n"
    else:
        sir_afisare += "BD nu este muchie ilegala\n"
else:
    if pozitie_relativa(D,A,B,C) == "in interior":
        sir_afisare += "BD este muchie ilegala\n"
    else:
        sir_afisare += "BD nu este muchie ilegala\n"


g.write(sir_afisare)

f.close()
g.close()





