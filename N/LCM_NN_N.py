def LCM_NN_N(A: Natural, B: Natural) -> Natural:
    """
    Сделала: Имховик Наталья
    Нахождение НОК натуральных чисел
    Используем НОК(a, b) = (a * b) / НОД(a, b)
    Возвращает натуральное
    """
    gcd = GCF_NN_N(A, B)
    return A * B // gcd