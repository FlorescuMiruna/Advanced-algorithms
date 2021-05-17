f = open("3.in")
g = open("3.out","w")

sir_afisare = ""

# Vrem sa avem obiecte de tip Punct care sa aiba coordonatele x si y
class Punct:
    def __init__(self,nume,x,y):
        self.x = x
        self.y = y
        self.nume = nume

    def __str__(self):
        return  self.nume + " x = " + str(self.x) +  ", y = "+ str(self.y)
    # def __str__(self):
    #     return  str(self.x) +  " "+ str(self.y)
    #


def cautareBinaraSup(st,dr,arr,punct):

    while st < dr:
        mijloc = (st + dr) // 2 + 1
        if arr[mijloc-1].x <= punct.x and punct.x <= arr[mijloc].x: # Cautam cele doua puncte intre care se afla punctul nostru in functie de axa Ox
            return ( arr[mijloc],arr[mijloc-1]) # Intorc punctele in sens trigonometric
            break
        elif punct.x > arr[mijloc].x:
            st = mijloc
        elif punct.x < arr[mijloc].x:
            dr = mijloc - 1

def cautareBinaraInf(st,dr,arr,punct):

    while st < dr:
        mijloc = (st + dr) // 2 + 1

        if arr[mijloc-1].x <= punct.x and punct.x <= arr[mijloc].x: # Cautam cele doua puncte intre care se afla punctul nostru in functie de axa Ox

            if (arr[mijloc].x == punct.x == arr[mijloc+1].x and arr[mijloc].y <= punct.y <= arr[mijloc+1].y): # Cazul particular in care punctul se afla pe muchia urmatoare
                return (arr[mijloc],arr[mijloc+1])
                break
            else:
                return (arr[mijloc-1], arr[mijloc])
                break
        elif punct.x > arr[mijloc].x:
            st = mijloc
        elif punct.x < arr[mijloc].x:
            dr = mijloc - 1





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


n = int(f.readline())

P = [] # lista de puncte din polinom

minim = Punct("",999999999,999999999)
maxim = Punct("",-999999999,-999999999)

for i in range(0,n):
    Xp, Yp = (f.readline()).split()
    Xp = int(Xp)
    Yp = int(Yp)
    Punctul = Punct("P" + str(i+1),Xp,Yp)
    P.append(Punctul)

    # Vrem sa obtinem punctul cel mai din stanga si punctul cel mai din dreapta

    if Punctul.x < minim.x:
        minim = Punctul
        S = i
    if Punctul.x == minim.x: # In caz ca am 2 puncte cu acelasi x, vreau sa il aleg pe cel cu y-ul cel mai mare, adica acel segment sa fie inclus in frontiera inferioara
        if Punctul.y > minim.y:
            minim = Punctul
            S = i

    if Punctul.x > maxim.x:
        maxim = Punctul
        D = i
    if Punctul.x == maxim.x:
        if Punctul.y > maxim.y:
            maxim = Punctul
            D = i



if S < D:
    frontiera_inferioara = P[S:D+1]
    frontiera_superipara = P[D:n] + P[0:S+1]
else:
    frontiera_inferioara = P[S:n] + P[0:D+1]
    frontiera_superipara = P[D:S+1]


frontiera_superipara.reverse() # Inversez punctele din frontiera inferioara ca sa pot aplica mai usor cautarea binara

print("Frontiera inferioara: ")
for i in range(0,len(frontiera_inferioara)):
    print(frontiera_inferioara[i])

print("Frontiera superioara: ")
for i in range(0,len(frontiera_superipara)):
    print(frontiera_superipara[i])


nr_puncte = int(f.readline())

Q = []
while nr_puncte != 0:
    Xq, Yq = (f.readline()).split()
    Xq = float(Xq)
    Yq = float(Yq)
    Q.append(Punct("Q: " + str(i+1),Xq,Yq))
    nr_puncte -= 1




for i in range(0,len(Q)):

    # Cautam binar intre ce puncte se afla situal punctul nostru in functie de axa Ox,
    # mai intai pe frontiera inferioara, apoi pe cea superioara

    muchie_inf = cautareBinaraInf(0,len(frontiera_inferioara)-1,frontiera_inferioara,Q[i])
    muchie_sup = cautareBinaraSup(0,len(frontiera_superipara)-1,frontiera_superipara,Q[i])

    # print("Muchie inf:", muchie_inf[0],muchie_inf[1])
    # print("Muchie sup:", muchie_sup[0], muchie_sup[1])
    A_inf = muchie_inf[0]
    B_inf = muchie_inf[1]
    A_sup = muchie_sup[0]
    B_sup = muchie_sup[1]

    # Calculam natura virajului punctului nostru fata de muchie


    if test_orientare(A_inf,B_inf,Q[i]) == "coliniare" or test_orientare(A_sup,B_sup,Q[i]) == "coliniare":
        sir_afisare += "on edge\n"
    elif test_orientare(A_inf, B_inf, Q[i]) == "dreapta" or test_orientare(A_sup, B_sup, Q[i]) == "dreapta":
            sir_afisare += "outside\n"
    elif test_orientare(A_inf,B_inf,Q[i]) == "stanga" and test_orientare(A_sup,B_sup,Q[i]) == "stanga":
        sir_afisare += "inside\n"



g.write(sir_afisare)

