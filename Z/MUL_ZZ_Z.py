def __mul__(self, other):
    """
    Сделал: Соколовский Артём
    Умножение целых чисел: self * other.
    """
    result_sign = 1 if self.s != other.s else 0
    A = int(''.join(map(str, self.A))) if self.A else 0
    B = int(''.join(map(str, other.A))) if other.A else 0
    product = A * B

    digits = [int(ch) for ch in str(abs(product))]
    return {"sign": result_sign, "digits": digits}
