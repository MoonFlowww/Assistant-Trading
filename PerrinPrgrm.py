def Perrin():
    n = 50

    def PerrinTerm(n):
        if n == 0:
            return 3
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            a, b, c = 3, 0, 2
            for _ in range(3, n + 1):
                a, b, c = b, c, a + b
            return c

    def PerrinProcess(nombre_terms):
        suite = [PerrinTerm(i) for i in range(nombre_terms) if 10 <= PerrinTerm(i) <= 9999]
        return suite

    Resultat = PerrinProcess(n)
    return Resultat

Perrin()
