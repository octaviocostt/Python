class Triangulo:
    """Triângulo é um polígono de três lados e três ângulos."""

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def side_list(self) -> list:
        return [self.a, self.b, self.c]

    def perimetro(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 0

        return self.a + self.b + self.c

    def tipo_lado(self) -> str:
        side_name = ''
        sides = len(set(self.side_list()))

        if sides == 3:
            side_name = 'escaleno'
        elif sides == 2:
            side_name = 'isósceles'
        elif sides == 1:
            side_name = 'equilátero'

        return side_name

    def retangulo(self) -> bool:
        *side, hypotenuse = sorted(self.side_list())
        side_sum = (side[0] ** 2 + side[1] ** 2)

        return True if hypotenuse ** 2 == side_sum else False

    def semelhantes(self, triangulo) -> bool:
        t1 = self.side_list()
        t2 = triangulo.side_list()
        proportions = set([x[0]/x[1] for x in zip(t1, t2)])

        return True if len(proportions) == 1 else False
