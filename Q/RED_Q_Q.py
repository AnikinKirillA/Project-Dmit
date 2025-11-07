def RED_Q_Q(self):
    """ 
    Выполнил: Сурин Максим 
    Сокращение дроби
    """

    """ 
    Приведение числителя к натуральному числу;
    вычисление НОД числителя и знаменателя;
    приведение НОД к виду целого числа
    """
    gcf = Natural(self.numerator.len, self.numerator.A).GCF_NN_N(self.denominator)
    gcf = Integer(0, gcf.len, gcf.A)

    """ Если НОД не равен 1, сокращаем на него числитель и знаменатель """
    if gcf != 1:
        self.numerator //= gcf
        self.denominator //= gcf

    return self