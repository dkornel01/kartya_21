def tesztek():
    jatekosvesztett_kevesebb_pontal()
    jatekosvesztett_kifutas_teszt()
    dontetlen_tesztek_jatekosvesztett_lapdb()
    gep_vesztett_kevesebb_pontal()
    gepvesztett_kifutassal_teszt()
    dontetlen_tesztek_gep_vesztett_lapdb()
    mindketto_kifutott_teszt()
    dontetlen_tesztek_dontetlen()


def pontszamitas(lapok):
    pontok = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok


def eredmeny(jatekoslapok, geplapok):
    s = ""
    jP = pontszamitas(jatekoslapok)
    gP = pontszamitas(geplapok)
    jDb = len(jatekoslapok)
    gDb = len(geplapok)
    if jP <= 21 and gP <= 21:
        if jP > gP:
            s = "gep vesztett kevesebb pont"
        elif gP > jP:
            s = "jatekos vesztett kevesebb pont"
        elif gP == jP:
            if jDb > gDb:
                s = "jatekos vesztett kevesebb lap"
            elif jDb < gDb:
                s = "gep vesztett kevesebb lap"
            else:
                s = "döntetlen osztoztok a nyereségen"
    else:
        if jP > 21:
            s = "jatekos vesztett kifutott"
        elif gP > 21:
            s = "gep vesztett kifutott "
        if jP > 21 and gP > 21:
            s = "döntetlen a Ház nyert"
    return s


def jatekosvesztett_kifutas_teszt():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "jatekos vesztett kifutott"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("jatekos vesztett kifutott")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def gepvesztett_kifutassal_teszt():
    jatekos = [10, 9]
    gep = [10, 9, 3]
    vart_eredmeny = "gep vesztett kifutott "
    kapotteredmeny = eredmeny(jatekos, gep)
    print("gep vesztett kifutott ")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def mindketto_kifutott_teszt():
    jatekos = [10, 9,3]
    gep = [10, 9,3]
    vart_eredmeny = "döntetlen a Ház nyert"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("döntetlen a Ház nyert")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def gep_vesztett_kevesebb_pontal():
    jatekos = [10, 9]
    gep = [10, 8]
    vart_eredmeny = "gep vesztett kevesebb pont"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("gep vesztett kevesebb pont")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def jatekosvesztett_kevesebb_pontal():
    jatekos = [10, 8]
    gep = [10, 9]
    vart_eredmeny = "jatekos vesztett kevesebb pont"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("jatekos vesztett kevesebb pont")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def dontetlen_tesztek_gep_vesztett_lapdb():
    jatekos = [10, 9]
    gep = [10, 8, 1]
    vart_eredmeny = "gep vesztett kevesebb lap"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("gep vesztett kevesebb lap")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")

def dontetlen_tesztek_jatekosvesztett_lapdb():
    jatekos = [10, 8, 3]
    gep = [10, 11]
    vart_eredmeny = "jatekos vesztett kevesebb lap"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("jatekos vesztett kevesebb lap")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def dontetlen_tesztek_dontetlen():
    jatekos = [10, 8, 3]
    gep = [10, 8, 3]
    vart_eredmeny = "döntetlen osztoztok a nyereségen"
    kapotteredmeny = eredmeny(jatekos, gep)
    print("döntetlen osztoztok a nyereségen")
    if kapotteredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")



tesztek()