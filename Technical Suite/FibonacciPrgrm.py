def Fibonacci():
    n = 20  # Nombre de termes à générer (ajustez selon vos besoins)

    def FiboTerm(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            result = []

            for _ in range(n):
                term = a
                if 10 <= term <= 9999:
                    result.append(term)
                a, b = b, a + b

            return result

    def FibonacciProcess(nombre_terms):
        suite = FiboTerm(nombre_terms)
        return suite

    Resultat = FibonacciProcess(n)
    return Resultat

Fibonacci()
