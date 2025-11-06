class Integer:
    def __init__(self, s, n, A):
        self.s = s #int знак числа (1 — минус, 0 — плюс)
        self.len = n #int len(A)-1
        self.A = A #[] массив из int   123 -> [1, 2, 3], -123 -> [1, 2, 3]

