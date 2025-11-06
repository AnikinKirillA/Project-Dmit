def GCF_NN_N(a: Natural, b: Natural) -> Natural:
    """
    Сделал: Чумаков Никита Ярославович
    НОД (наибольший общий делитель) двух натуральных чисел.
    """
    # Создаём копии, чтобы не испортить исходные
    A = Natural(a.len, a.A[:])
    B = Natural(b.len, b.A[:])

    while NZER_N_B(B):  # пока B != 0
        # Проверяем, какое больше
        cmp = COM_NN_D(A, B)

        if cmp == 1:  # A < B -> поменяем их местами
            A, B = B, A

        # Теперь A >= B, можно брать остаток
        R = A % B
        A, B = B, R

    return A