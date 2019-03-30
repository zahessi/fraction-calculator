import unittest

# import test modules
from fraction_classes import fraction_tests as fraction_test
import fraction_classes.fraction_tests.fraction_parser_test as parser_test


class TestRunner:
    test_cases = [fraction_test, parser_test]

    def __init__(self):
        self.loader = unittest.TestLoader()
        self.suite = unittest.TestSuite()
        self.runner = unittest.TextTestRunner()

    def run(self):
        for test in self.test_cases:
            self.suite.addTest(self.loader.loadTestsFromModule(test))
        result = self.runner.run(self.suite)
        return result.failures

