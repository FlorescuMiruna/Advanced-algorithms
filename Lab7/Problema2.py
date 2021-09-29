f = open("2_in.txt")
g = open("2_out.txt","w")

nr_exemple = int(f.readline())



for l in range(nr_exemple):

    g.write("exemplul " + str(l+1) +":\n")

    Qx, Qy = f.readline().split()
    Qx = float(Qx)
    Qy = float(Qy)

    n = int(f.readline())
    min_x = 999999999
    min_y= 999999999
    max_x = -999999999
    max_y = -999999999

    min_x_init = False # Vrem sa stim daca avem limite superioare sau inferioare pentru x si y
    min_y_init = False
    max_x_init = False
    max_y_init  = False

    exista_drepunghi = True
    intersectie_verticala = []
    intersectie_orizontala = []

    for t in range(n):
        a, b, c = f.readline().split()
        a = float(a)
        b = float(b)
        c = float(c)
        if b == 0:  # scriem in functie de x
            if a > 0:
                lim_sup = ((-1) * c) / a
                # print("lim sup:", lim_sup)
                if lim_sup <= min_x:
                    min_x = lim_sup
                    min_x_init = True  # Inseamna ca a fost initializat
            elif a < 0:
                lim_inf = ((-1) * c) / a
                # print("lim inf:", lim_inf)
                if lim_inf >= max_x:
                    max_x = lim_inf
                    max_x_init = True

        if a == 0:  # In functie de y
            if b > 0:
                lim_sup = ((-1) * c) / b
                # print("lim sup:", lim_sup)
                if lim_sup <= min_y:
                    min_y = lim_sup
                    min_y_init = True
            if b < 0:
                lim_inf = ((-1) * c) / b
                # print("lim inf:", lim_inf)
                if lim_inf >= max_y:
                    max_y = lim_inf
                    max_y_init = True

    print("min x: ", min_x)
    print("max x: ", max_x)
    print("min y: ", min_y)
    print("max y: ", max_y)
    # Daca intersectia planurilor este vida sau nevida si nemarginita inseamna automat ca nu avem un dreptunghi

    if min_x_init == True and max_x_init == True:  # Daca avem si un x minim si unul maxim, inseamna ca avem semiplane "in directii opuse"
        # print(min_x, max_x)
        if min_x < max_x:  # Verificam daca acestea se intersecteaza
            exista_drepunghi = False  # Daca nu se intersecteaza, intersectia este vida indiferent de alte semiplane
        else:
            intersectie_verticala = [max_x, min_x]  # Daca se intersecteaza, retinem punctele lor de intersectie din x
    # Nu tinem cont de cazurile in care avem mai multe planuri in partea stanga sau dreapta, acestea sunt tratae ca unul singur
    # pentru ca am ales minimul si maximul

    # Aplicam acelasi lucru si pentry y
    if min_y_init == True and max_y_init == True:
        # print(min_y, max_y)
        if min_y < max_y:
            exista_drepunghi = False
        else:
            intersectie_orizontala = [max_y, min_y]





    if exista_drepunghi:
        # Daca cele 2 planuri se intersecteaza, verific daca intersectia este marginita

        if intersectie_verticala == [] or intersectie_orizontala == []:

                # Daca intersectia verticala este vida inseamna ca nu am un plan in stanga sau in dreapta
                # Iar daca cea orizontala este vida inseamna ca nu am plan in partea de  sus sau de jos, ceea ce inseamna
                # ca intersectia este nemarginita

            exista_drepunghi = False

    if exista_drepunghi == False:
        g.write("(a) nu exista un dreptunghi cu proprietatea ceruta\n\n")
    else:
        # Daca nu am nici intersectie vida, nici intersectie nevida nemarginita, inseamna ca exista un dreptunghi format de laturi,
        # dar trebuie sa verific daca Q este in interiorul lui

        print(intersectie_orizontala)
        print(intersectie_verticala)

        # Verificam daca punctul Q se afla in interiorul dreptunghiului delimitat de laturi

        if Qy < intersectie_orizontala[0] or Qy > intersectie_orizontala[1]:
            exista_drepunghi = False
        if Qx < intersectie_verticala[0] or Qy > intersectie_orizontala[1]:
            exista_drepunghi = False


        if exista_drepunghi == False:
            g.write("(a) nu exista un dreptunghi cu proprietatea ceruta\n\n")
        else:
            g.write("(a) exista un dreptunghi cu proprietatea ceruta\n")

            # Calculam aria pentru dreptunghi
            # Stim deja ca este cel mai mic dreptunghi pentru ca am ales de fiecare data minimul si maximul lui x si al lui y

            aria = (intersectie_orizontala[1] - intersectie_orizontala[0]) * (intersectie_verticala[1] - intersectie_verticala[0])
            if int(aria) == aria:
                aria = int(aria)
            g.write("Aria minima este " + str(aria)+ "\n\n")


