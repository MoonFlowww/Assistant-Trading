def Pell():
    n = 50

    def PellTerm(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, 2 * b + a
            return b

    def PellProcess(nombre_terms):
        suite = [PellTerm(i) for i in range(nombre_terms) if 10 <= PellTerm(i) <= 9999]
        return suite

    Resultat = PellProcess(n)
    return Resultat

Pell()
