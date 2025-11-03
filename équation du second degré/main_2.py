def resol_eq_second_degre (a,b,c):

    Delta = b**2 - 4*a*c


    if (Delta < 0):
        print("L’équation admet 0 solution réelle.")

    elif (Delta == 0):
        print("L’équation admet 1 solution réelle.")
        X0 = -b / (2*a)
        print(X0)

    else:
        print("L’équation admet 2 solution réelles.")
        X1 = (-b -sqrt (Delta)) / (2*a)
        X2 = (-b + (Delta)) / 2*a
        print(X1)
        print(X2)