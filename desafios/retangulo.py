#!/usr/bin/env python3

# retangulo.py


class Retangulo:
    def __init__(self, lado_x, lado_y):
        self.lado_x = lado_x
        self.lado_y = lado_y

    @property
    def perimetro(self):
        return self.lado_x * 2 + self.lado_y * 2

    @property
    def area(self):
        return self.lado_x * self.lado_y
