def __truediv__(self, other):
    """
    Сделал: Чумаков Никита Ярославович
    Деление рациональных чисел q1 / q2.
    Делитель q2 ≠ 0.
    Возвращает новый Rational.
    """
    # Проверим, что делитель не равен нулю (числитель делителя != 0)
    if all(d == 0 for d in other.numerator.A):
        raise ZeroDivisionError("Деление на ноль в рациональных числах")

    # По формуле: (a/b) ÷ (c/d) = (a*d) / (b*c) перемножаем
    new_numerator = self.numerator * other.denominator.TRANS_N_Z()
    new_denominator = self.denominator * other.numerator.ABS_Z_N()

    # Формируем новое рациональное число
    result = Rational(new_numerator, new_denominator)

    return result