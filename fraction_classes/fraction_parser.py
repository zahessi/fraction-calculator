import re
from fraction_classes.fraction import Fraction


class FractionParser:
    divide_reg = r"((\d+\/\d+)|\d+)|[+\-\/*]"
    inner_parentheses_reg = r"\([^()]+\)"
    final_reg = r"^-?(\d+\/\d+|\d)$"
    valid_reg = r"^-?(\d+\/\d+|\d+)( *[\-*\/+] *-?(\d+\/\d+|\d+))* *$"

    def __init__(self):
        self.compSigns = {
            "+": Fraction.__add__,
            "-": Fraction.__sub__,
            "/": Fraction.__truediv__,
            "*": Fraction.__mul__
        }

        self.operands = ["*", "/", "+", "-"]

    def process(self, string: str):
        while re.findall(self.inner_parentheses_reg, string):
            inner = next(re.finditer(self.inner_parentheses_reg, string)).group(0)
            string = string.replace(inner, f" {self._compute(inner)} ", 1)
        return self._compute(string)

    def _compute(self, string: str):
        if re.match(r"\(.*\)", string):
            string = string.strip(")").strip("(").strip()
        self._validate(string.strip())
        parts = self._find_negative([x.group(0) for x in re.finditer(self.divide_reg, string)])

        for operand in self.operands:
            while parts.__contains__(operand):
                if operand in parts:
                    index = parts.index(operand)
                    result = repr(self.compSigns[operand](Fraction.fromstring(parts[index - 1]),
                                                          Fraction.fromstring(parts[index + 1])))
                    parts[index - 1:index + 2] = [result]
        return parts[0]

    def _find_negative(self, arr):
        for i, e in enumerate(arr):
            if e == "-":
                if re.match(self.final_reg, arr[i + 1]) and (i == 0 or arr[i - 1] in ["*", "/", "+", "-", "("]):
                    arr[i:i + 2] = ["-" + arr[i + 1]]
        return arr

    def _validate(self, string):
        if not re.match(self.valid_reg, string):
            raise ValueError("Not allowed symbols or sequence")
