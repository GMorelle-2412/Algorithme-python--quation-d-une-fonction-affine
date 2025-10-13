def eq_fonction_affine (xA,yA,xB,yB):
    if xA==xB:
        print("Calcul imposible")
    else:
        a = (yB-yA)/(xB-xA)
        b = yA-a*xA
        print("y=",a,"x","+",b)
