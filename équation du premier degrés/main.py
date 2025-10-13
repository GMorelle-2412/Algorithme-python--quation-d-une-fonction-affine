Xa = float(input("Donne l'abscisse de A:"))
Ya = float(input("Donne l'ordonnée de A:"))

Xb = float(input("Donne l'abscisse de B:"))
Yb = float(input("Donne l'ordonnée de B:"))

if Xa==Xb:
    print("Calcul imposible")
else:
    a = (Yb-Ya)/(Xb-Xa)
    b = Ya-a*Xa

    print("y=",a,"x","+",b)