import unittest

# import test modules
from tests import fraction_class_test
from tests import fraction_parser_test


class TestRunner:
    test_cases = [fraction_parser_test, fraction_class_test]

    def __init__(self):
        self.loader = unittest.TestLoader()
        self.suite = unittest.TestSuite()
        self.runner = unittest.TextTestRunner()

    def run(self):
        for test in self.test_cases:
            self.suite.addTest(self.loader.loadTestsFromModule(test))
        result = self.runner.run(self.suite)
        return result.failures


if __name__ == "__main__":
    TestRunner().run()
