import unittest
from fraction_parser import FractionParser


class FractionParserTest(unittest.TestCase):

    def test_priority(self):
        f = FractionParser()

        self.assertEqual(f.process("2+1*1/2"), "5/2")

    def test_adding_ints2(self):
        f = FractionParser()

        self.assertEqual(f.process("1+1+1"), "3")

    def test_adding_ints3(self):
        f = FractionParser()

        self.assertEqual(f.process("1/2"), "1/2")

    def test_adding_with_ints(self):
        f = FractionParser()

        self.assertEqual(f.process("1/2 + 1/2"), "1")

    def test_adding_with_ints2(self):
        f = FractionParser()

        self.assertEqual(f.process("1/5 + 1/5 + 1/5"), "3/5")

    def test_computing(self):
        f = FractionParser()

        self.assertEqual(f.process("0*3"), "0")

    def test_computing1(self):
        f = FractionParser()

        self.assertEqual(f.process("1/5 / 1/5"), "1")

    def test_computing2(self):
        f = FractionParser()

        self.assertEqual(f.process("1/5 + 3/5 * 1/3"), "2/5")

    def test_computing3(self):
        f = FractionParser()

        self.assertEqual(f.process("1/2+2/2/1/3"), "7/2")

    def test_computing4(self):
        f = FractionParser()

        self.assertEqual(f.process("4/2-(1/2)"), "3/2")

    def test_computing5(self):
        f = FractionParser()

        self.assertEqual(f.process("1/7 + 2 * (2/7 + 3/7 + 7/7 * 1/7) / 2"), "1")

    def test_computing6(self):
        f = FractionParser()

        self.assertEqual(f.process("((1/2) + (2/3)) - ((2/7) / (1/8))"), "-47/42")

    def test_computing7(self):
        f = FractionParser()

        self.assertEqual(f.process("7/6 - 16/7"), "-47/42")

    def test_computing8(self):
        f = FractionParser()

        with self.assertRaises(ValueError):
            print(f.process("1/2 - 1/2("))

    def test_computing_complex(self):
        f = FractionParser()

        self.assertEqual(f.process("1/(2/(3/(4)))"), "3/8")

    def test_computing_with_negative(self):
        f = FractionParser()

        self.assertEqual(f.process("1*-2"), "-2")

    def test_computing_with_negative1(self):
        f = FractionParser()

        self.assertEqual(f.process("4/2-(-1/2)"), "5/2")

    def test_not_valid(self):
        f = FractionParser()

        with self.assertRaises(ValueError):
            f.process("1/5 + 1/5 + ")

    def test_not_valid1(self):
        f = FractionParser()

        with self.assertRaises(ValueError):
            f.process("1/7 + 2 * (2/7 + 3/7 + 7/7 * 1/7#) : 2)")
