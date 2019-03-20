import unittest

from fraction import Fraction


class FractionInitTests(unittest.TestCase):

    def test_denominator_and_nom_negative(self):
        a = Fraction(-2, -3)

        self.assertEqual(repr(a), "2/3")

    def test_top_cannot_be_float(self):
        with self.assertRaises(ValueError) as context:
            Fraction(2.5, 8)

        self.assertTrue("Value must be integer" in str(context.exception))

    def test_bottom_cant_be_float(self):
        with self.assertRaises(ValueError) as context:
            Fraction(2, 8.4)

        self.assertTrue("Value must be integer" in str(context.exception))

    def test_bottom_cant_be_zero(self):
        with self.assertRaises(ValueError) as context:
            Fraction(2, 0)

        self.assertTrue("Denominator cannot be zero" in str(context.exception))

    def test_repr_of_class(self):
        a = Fraction(0, 5)
        self.assertEqual(repr(a), "0")

    def test_init_from_string(self):
        a = Fraction.fromstring("0/5")

        self.assertEqual(repr(a), "0")

    def test_init_from_string3(self):
        a = Fraction.fromstring("6")

        self.assertEqual(repr(a), "6")

    def test_init_from_string1(self):
        with self.assertRaises(ValueError) as context:
            Fraction.fromstring("s/5")

        self.assertTrue("Not valid string; must in a format %d/%d" in str(context.exception))

    def test_init_from_string2(self):
        with self.assertRaises(ValueError) as context:
            Fraction.fromstring("s/5")

        self.assertTrue("Not valid string; must in a format %d/%d" in str(context.exception))


class FractionAdditionTests(unittest.TestCase):

    def test_addition_leading_to_one(self):
        a = Fraction(3, 5)
        b = Fraction(2, 5)

        self.assertEqual(repr(a + b), "1")

    def test_addition_with_simplifying(self):
        a = Fraction(1, 14)
        b = Fraction(1, 14)

        self.assertEqual(repr(a + b), "1/7")

    def test_addition_with_diff_bottoms(self):
        a = Fraction(1, 5)
        b = Fraction(2, 3)

        self.assertEqual(repr(a + b), "13/15")

    def test_casual_addition(self):
        a = Fraction(1, 5)
        b = Fraction(2, 5)

        self.assertEqual(repr(a + b), "3/5")

    def test_casual_addition_with_one_as_bottom(self):
        a = Fraction(1, 5)
        b = Fraction(5, 1)

        self.assertEqual(repr(a + b), "26/5")

    def test_with_int(self):
        a = Fraction(1, 2)
        b = 1

        self.assertEqual(repr(a + b), "3/2")

    def test_with_str(self):
        a = Fraction(1, 5)
        b = "2"

        with self.assertRaises(ValueError) as context:
            a + b

        self.assertTrue("Not integer or fraction type while adding" in str(context.exception))


class FractionSubtractionTests(unittest.TestCase):

    def test_normal(self):
        a = Fraction(3, 5)
        b = Fraction(1, 5)

        self.assertEqual(repr(a - b), "2/5")

    def test_to_negative(self):
        a = Fraction(1, 5)
        b = Fraction(3, 5)

        self.assertEqual(repr(a - b), "-2/5")


class FractionMultiTests(unittest.TestCase):

    def test_normal(self):
        a = Fraction(24, 35)
        b = Fraction(25, 36)

        self.assertEqual(repr(a * b), "10/21")

    def test_with_negatives(self):
        a = Fraction(-6, 5)
        b = Fraction(3, 5)

        self.assertEqual(repr(a * b), "-18/25")

    def test_with_negatives2(self):
        a = Fraction(-6, 5)
        b = Fraction(-3, 5)

        self.assertEqual(repr(a * b), "18/25")

    def test_with_negatives3(self):
        a = Fraction(-6, -5)
        b = Fraction(3, 5)

        self.assertEqual(repr(a * b), "18/25")

    def test_with_integers(self):
        a = Fraction(-6, -5)
        b = 3

        self.assertEqual(repr(a * b), "18/5")


class FractionDivisionTests(unittest.TestCase):

    def test_common(self):
        a = Fraction(3, 6)
        b = Fraction(2, 3)

        self.assertEqual(repr(a / b), "3/4")

    def test_common1(self):
        a = Fraction(4, 7)
        b = Fraction(0, 5)

        with self.assertRaises(ValueError):
            c = a / b


class FractionPowTests(unittest.TestCase):

    def test_pow(self):
        a = Fraction(3, 5)

        self.assertEqual(repr(a ** 2), "9/25")

    def test_pow1(self):
        a = Fraction(0, 3)

        self.assertEqual(repr(a ** 2), "0")
