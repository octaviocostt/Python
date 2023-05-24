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


