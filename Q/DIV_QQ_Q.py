def DIV_QQ_Q(q1: Rational, q2: Rational) -> Rational:
    """
    Сделал: Чумаков Никита Ярославович
    Деление рациональных чисел q1 / q2.
    Делитель q2 ≠ 0.
    Возвращает новый Rational.
    """
    # Проверим, что делитель не равен нулю (числитель делителя != 0)
    if all(d == 0 for d in q2.numerator.A):
        raise ZeroDivisionError("Деление на ноль в рациональных числах")

    # По формуле: (a/b) ÷ (c/d) = (a*d) / (b*c) перемножаем
    new_numerator = MUL_ZZ_Z(q1.numerator, TRANS_N_Z(q2.denominator))
    new_denominator = MUL_NN_N(q1.denominator, ABS_Z_N(q2.numerator))

    # Формируем новое рациональное число
    result = Rational(new_numerator, new_denominator)

    return result