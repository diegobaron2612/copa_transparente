#!/usr/bin/env python3

from math import pi


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return self.raio ** 2 * pi

    @property
    def perimetro(self):
        return self.raio * 2 * pi
