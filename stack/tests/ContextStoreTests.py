import unittest

from stack.src.ContextStore import *

class ExpectedBehaviors():
    def test_listEmptyIsSafe(self, c):
        actual = c.list()

        self.assertEqual(0, len(actual))

    def test_listOneReturnsOne(self, c):
        expected = "Don't forget to do that one thing"
        c.push(StackContext(expected))

        actual = c.list()

        self.assertEqual(1, len(actual))
        self.assertEqual(expected, actual[0].description)

    def test_listReturnsMultipleInStackOrder(self, c):
        c.push(StackContext('1'))
        c.push(StackContext('2'))
        c.push(StackContext('3'))

        actual = c.list()

        self.assertEqual(3, len(actual))
        self.assertEqual('3', actual[0].description)
        self.assertEqual('2', actual[1].description)
        self.assertEqual('1', actual[2].description)

    def test_listReturnsLimit(self, c):
        c.push(StackContext('1'))
        c.push(StackContext('2'))
        c.push(StackContext('3'))
        c.push(StackContext('4'))
        c.push(StackContext('5'))

        actual = c.list()

        self.assertEqual(5, len(actual))
        self.assertEqual('5', actual[0].description)
        self.assertEqual('4', actual[1].description)
        self.assertEqual('3', actual[2].description)
        self.assertEqual('2', actual[3].description)
        self.assertEqual('1', actual[4].description)

    def test_listReturnsUpToLimit(self, c):
        c.push(StackContext('1'))
        c.push(StackContext('2'))
        c.push(StackContext('3'))
        c.push(StackContext('4'))
        c.push(StackContext('5'))
        c.push(StackContext('6'))

        actual = c.list()

        self.assertEqual(5, len(actual))
        self.assertEqual('6', actual[0].description)
        self.assertEqual('5', actual[1].description)
        self.assertEqual('4', actual[2].description)
        self.assertEqual('3', actual[3].description)
        self.assertEqual('2', actual[4].description)

    def test_popReturnsNoneWhenEmpty(self, c):
        actual = c.pop()

        self.assertEqual(None, actual)

    def test_popReturnsOnly(self, c):
        c.push(StackContext('1'))

        actual = c.pop()

        self.assertEqual('1', actual.description)

    def test_popReturnsTopWhenMultiple(self, c):
        c.push(StackContext('1'))
        c.push(StackContext('2'))

        actual = c.pop()

        self.assertEqual('2', actual.description)

implementations = [
    ('inMemory', lambda: create_ctx(True)),
    ('onDisk', lambda: create_ctx(False, location = './test.db'))
]

class TestHost(unittest.TestCase):
    pass

def add_dynamic_test_method(method_name, context, test_instance):
    test_method = getattr(ExpectedBehaviors, method_name)
    test_method_name = f'{method_name}_{impl[0]}'
    test_method_decorator = lambda _self: test_method(_self, test_instance)
    setattr(TestHost, test_method_name, test_method_decorator)

for method_name in [m for m in dir(ExpectedBehaviors) if not m.startswith('_')]:
    for impl in implementations:
        add_dynamic_test_method(method_name, impl[0], impl[1]())

if __name__ == '__main__':
    unittest.main()






