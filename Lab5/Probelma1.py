f = open("1.in")
g = open("1.out","w")

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
    if det == 0:
        naturaViraj = "coliniare"
    elif det < 0:
        naturaViraj = "dreapta"
    else:
        naturaViraj = "stanga"

    return naturaViraj


n = int(f.readline())
while n != 0:

    Xp, Yp = (f.readline()).split()
    P = Punct(int(Xp),int(Yp))

    Xq, Yq = (f.readline()).split()
    Q = Punct(int(Xq),int(Yq))

    Xr, Yr = (f.readline()).split()
    R = Punct(int(Xr), int(Yr))

    sir_afisare += test_orientare(P,Q,R) + "\n"

    n -= 1

g.write(sir_afisare)

f.close()
g.close()