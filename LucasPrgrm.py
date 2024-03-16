def Lucas():
    n = 50


    def LucasTerm(n):
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def LucasProcess(nombre_terms):
        suite = [LucasTerm(i) for i in range(nombre_terms) if 10 <= LucasTerm(i) <= 9999]
        return suite

    Resultat = LucasProcess(n)  
    return Resultat


Lucas()