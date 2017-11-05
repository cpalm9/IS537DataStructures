import unittest
from main import Date, Person, Franchise
import serialize

class UnitTest(unittest.TestCase):
    fd1 = Date(1900, 8, 1)
    f1 = Franchise('Chris', 'Palmer', fd1)
    b1 = Date(2001, 4, 3)
    p1 = Person('The "Real" Deal', 'M', b1, False, 0.00, 1111, None, None, f1)

    test = serialize.to_json(p1)
    print(test)


if __name__ == '__main__':
    unittest.main()