import unittest
import mojprogram

class TestTDD1(unittest.TestCase):

    def test_zwroc_100(self):
        wynik = mojprogram.zwroc_100()
        self.assertEqual(wynik,100)

    def test_inna_metoda(self):
        self.assertEqual(mojprogram.inna_metoda(124), 124)

    def test_hello(self):
        wynik = mojprogram.hello()
        self.assertEqual(wynik,"Hello_world")

    def test_add(self):
        wynik = mojprogram.add()
        self.assertEqual(wynik,1+3)

    def test_substract(self):
        wynik = mojprogram.substract()
        self.assertEqual(wynik,4-3)

    def test_calc(self):
        wynik = mojprogram.calc()
        self.assertEqual(wynik,2*3)

    def test_div(self):
        wynik = mojprogram.div()
        self.assertEqual(wynik,6/3)

if __name__ == '__main__':
    unittest.main()
