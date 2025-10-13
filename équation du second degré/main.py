a = float(input("Donne a:"))
b = float(input("Donne b:"))
c = float(input("Donne c:"))


Delta = b*b - 4*a*c


if (Delta < 0):
    print("L’équation admet 0 solution réelle.")

elif (Delta == 0):
    print("L’équation admet 1 solution réelle.")
    X0 = -b / 2*a
    print(X0)

elif(Delta > 0):
    print("L’équation admet 2 solution réelle.")
    X1 = -b -Delta/Delta / 2*a
    X2 = -b + Delta/Delta / 2*a
    print(X1)
    print(X2)