class Matrix:
    def __init__(self, my_m):
        self.str = [my_m[i][0] for i in range(len(my_m))]
        self.col = [my_m[i][1] for i in range(len(my_m))]

    def __add__(self, other):
        A = []
        B = []
        for el in range(len(self.str)):
            result_1 = self.str[el] + other.str[el]
            A.append(str(result_1))
        for arg in range(len((self.col))):
            result_2 = self.col[arg] + other.col[arg]
            B.append(str(result_2))

        a = " ".join(A)
        b = " ".join(B)
        return f"{a}\n{b}"


matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[7, 8], [9, 10]])


print(matrix_1 + matrix_2)
