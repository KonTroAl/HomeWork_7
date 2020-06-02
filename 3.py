class Cell:
    def __init__(self, my_p):
        self.my_p = my_p

    """Сложение"""

    def __add__(self, other):
        return Cell(self.my_p + other.my_p)

    """Вычитание"""

    def __sub__(self, other):
        return Cell(self.my_p - other.my_p)

    """Умножение"""

    def __mul__(self, other):
        return Cell(self.my_p * other.my_p)

    """Деление"""

    def __truediv__(self, other):
        return Cell(self.my_p // other.my_p)

    def __str__(self):
        return f"{self.my_p}"

    def make_order(self, x):
        b = self.my_p % x
        z = "0"
        if b != 0:
            return f"{z * x}\n{z * b}"
        else:
            return f"{z * self.my_p}"


cell_1 = Cell(20)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))
