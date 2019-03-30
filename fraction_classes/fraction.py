import re


class Fraction:

    def __init__(self, top, bottom):
        self._validate_int(top, bottom)

        gcd = self._simplify(abs(top), abs(bottom)) * (-1 if top < 0 and bottom < 0 else 1)

        if gcd != 1:
            bottom = int(bottom / gcd)
            top = int(top / gcd)

        self.top = top
        self.bottom = bottom

    def __add__(self, other):
        other = self._validate(other)

        if self.bottom == other.bottom:
            denom = self.bottom
            nom = self.top + other.top
        else:
            denom = self.bottom * other.bottom
            nom = self.top * other.bottom + other.top * self.bottom

        return Fraction(nom, denom)

    def __sub__(self, other):
        other.top = -other.top
        return self + other

    def __mul__(self, other):
        other = self._validate(other)

        return Fraction(self.top * other.top, self.bottom * other.bottom)

    def __truediv__(self, other):
        other = self._validate(other)

        return self * Fraction(other.bottom, other.top)

    def __pow__(self, power, modulo=None):
        if modulo:
            raise NotImplementedError

        return Fraction(pow(self.top, power), pow(self.bottom, power))

    @classmethod
    def fromstring(cls, string):
        if re.match(r"-?\d+/\d+", string):
            digits = re.findall(r"-?\d+", string)
            return cls(*list(map(lambda x: int(x), digits)))
        elif re.match(r"-?\d+", string):
            return cls(int(string), 1)
        else:
            raise ValueError("Not valid string; must in a format %d/%d")

    def _validate(self, n):
        if not isinstance(n, Fraction):
            if isinstance(n, int):
                return Fraction(n, 1)
            else:
                raise ValueError("Not integer or fraction type while adding")
        return n

    def _validate_int(self, *a):
        for i in a:
            if not isinstance(i, int):
                raise ValueError("Value must be integer")

    def _simplify(self, a, b):
        if a == 0 or b == 0: return 1

        if b > a:
            return self._simplify(b, a)

        if a % b == 0:
            return b

        return self._simplify(b, a % b)

    @property
    def top(self):
        return self.top

    @property
    def bottom(self):
        return self.bottom

    @top.setter
    def top(self, a):
        self._top = a

    @top.getter
    def top(self):
        return self._top

    @bottom.getter
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, a):
        if a == 0:
            raise ValueError("Denominator cannot be zero")
        self._bottom = a

    def __repr__(self):
        if self.bottom == 1:
            text = str(self.top)
        elif self.top == 0:
            text = "0"
        else:
            text = "%d/%d" % (self.top, self.bottom)
        return text
