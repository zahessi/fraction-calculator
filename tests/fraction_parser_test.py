import unittest
from fraction_classes.fraction_parser import FractionParser


class FractionParserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.f = FractionParser()

    def test_priority(self):
        self.assertEqual(self.f.process("2+1*1/2"), "5/2")

    def test_adding_ints2(self):
        self.assertEqual(self.f.process("1+1+1"), "3")

    def test_adding_ints3(self):
        self.assertEqual(self.f.process("1/2"), "1/2")

    def test_adding_with_ints(self):
        self.assertEqual(self.f.process("1/2 + 1/2"), "1")

    def test_adding_with_ints2(self):
        self.assertEqual(self.f.process("1/5 + 1/5 + 1/5"), "3/5")

    def test_computing(self):
        self.assertEqual(self.f.process("0*3"), "0")

    def test_computing1(self):
        self.assertEqual(self.f.process("1/5 / 1/5"), "1")

    def test_computing2(self):
        self.assertEqual(self.f.process("1/5 + 3/5 * 1/3"), "2/5")

    def test_computing3(self):
        self.assertEqual(self.f.process("1/2+2/2/1/3"), "7/2")

    def test_computing4(self):
        self.assertEqual(self.f.process("4/2-(1/2)"), "3/2")

    def test_computing5(self):
        self.assertEqual(self.f.process("1/7 + 2 * (2/7 + 3/7 + 7/7 * 1/7) / 2"), "1")

    def test_computing6(self):
        self.assertEqual(self.f.process("((1/2) + (2/3)) - ((2/7) / (1/8))"), "-47/42")

    def test_computing7(self):
        self.assertEqual(self.f.process("7/6 - 16/7"), "-47/42")

    def test_computing8(self):
        with self.assertRaises(ValueError):
            self.f.process("1/2 - 1/2(")

    def test_computing9(self):
        self.assertEqual(self.f.process("(((42)))"), "42")

    def test_computing_complex(self):
        self.assertEqual(self.f.process("1/(2/(3/(4)))"), "3/8")

    def test_computing_with_negative(self):
        self.assertEqual(self.f.process("1*-2"), "-2")

    def test_computing_with_negative1(self):
        self.assertEqual(self.f.process("4/2-(-1/2)"), "5/2")

    def test_not_valid(self):
        with self.assertRaises(ValueError):
            self.f.process("1/5 + 1/5 + ")

    def test_not_valid1(self):
        with self.assertRaises(ValueError):
            self.f.process("1/7 + 2 * (2/7 + 3/7 + 7/7 * 1/7#) : 2)")
