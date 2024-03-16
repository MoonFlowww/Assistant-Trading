def Tribonacci():
    n = 20

    def tribonacci(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a, b, c = 0, 1, 1
            for _ in range(3, n + 1):
                a, b, c = b, c, a + b + c
            return c

    def TribonacciProcess(nombre_terms):
        suite = [tribonacci(i) for i in range(nombre_terms) if 10 <= tribonacci(i) <= 9999]
        return suite

    Resultat = TribonacciProcess(n)
    return Resultat

Tribonacci()
