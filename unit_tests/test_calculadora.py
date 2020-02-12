# calculadora_test.py

import unittest
from desafios import dividir


class CalculadoraTest(unittest.TestCase):
    def test_dividir_valido(self):
        resultado = dividir(10, 5)
        self.assertEqual(resultado, 2.0)

    def test_dividir_valido_dois(self):
        resultado = dividir(120, 10)
        self.assertEqual(resultado, 12)

    def test_divisao_por_zero(self):
        self.assertRaises(ZeroDivisionError, dividir, 10, 0)


if __name__ == '__main__':
    unittest.main()
