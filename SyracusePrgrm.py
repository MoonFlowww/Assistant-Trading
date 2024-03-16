def Syracuse(n):

    def syracuse(n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    def SyracuseCycle(initial_value):
        cycle = syracuse(initial_value)
        return cycle

    Resultat = SyracuseCycle(n)
    return Resultat


