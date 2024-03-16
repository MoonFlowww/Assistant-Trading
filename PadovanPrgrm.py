def Padovan():
    n = 50


    def PadovanTerm(n):
        if n == 0:
            return 1
        elif n <= 2:
            return 1
        else:
            return PadovanTerm(n-2) + PadovanTerm(n-3)

    def PadovanProcess(nombre_terms):

        suite = [PadovanTerm(i) for i in range(nombre_terms) if 10 <= PadovanTerm(i) <= 9999]
        return suite
    Resultat = PadovanProcess(n)
    return Resultat


Padovan()