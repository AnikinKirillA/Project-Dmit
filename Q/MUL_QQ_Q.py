def MUL_QQ_Q(q1: Rational, q2: Rational) -> Rational:
    """
    Сделал: Чумаков Никита Ярославович
    Умножение двух рациональных чисел.
    q1, q2 — объекты класса Rational.
    Результат — новый Rational.
    """
    # Умножаем числители и знаменатели
    new_numerator = MUL_ZZ_Z(q1.numerator, q2.numerator)
    new_denominator = MUL_NN_N(q1.denominator, q2.denominator) # здесь надо использовать MUL_NN_N, но по условию она не включена??

    # Формируем новую дробь
    result = Rational(new_numerator, new_denominator)

    return result