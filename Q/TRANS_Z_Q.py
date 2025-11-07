def TRANS_Z_Q(self):
    """
    Богданов Никита Константинович
    Преобразование целого в дробное
    """
    # Создаем натуральное 1 для знаменателя
    one_natural = Natural(0, [1]) 

    return Rational(self, one_natural)
