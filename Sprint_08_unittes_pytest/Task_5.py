# Create class Worker with fields name and salary. If salary negative raise ValueError
#
# Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next step:
#
# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods.
# Don`t use assertRaises in tests.


import unittest


class Worker:
    def __init__(self, name, salary=0.0):
        if salary < 0:
            raise ValueError
        self.salary = salary
        self.name = name

    def get_tax_value(self):
        if self.salary <= 1000:
            return float(0.0)
        elif self.salary <= 3000:
            return 0.1 * (self.salary - 1000)
        elif self.salary <= 5000:
            return 0.15 * (self.salary - 3000) + 200
        elif self.salary <= 10000:
            return 0.21 * (self.salary - 5000) + 500
        elif self.salary <= 20000:
            return 0.30 * (self.salary - 10000) + 1550
        elif self.salary <= 50000:
            return 0.40 * (self.salary - 20000) + 4550
        else:
            return 0.47 * (self.salary - 50000) + 16550


class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('John Doe', 11500)

    def tearDown(self) -> None:
        self.worker = None

    def test_get_tax_value_0_to_1k(self):
        self.worker.salary = 1000
        self.assertEqual(self.worker.get_tax_value(), 0)

    def test_get_tax_value_1_to_3k(self):
        self.worker.salary = 3000
        self.assertEqual(self.worker.get_tax_value(), 200)

    def test_get_tax_value_3_to_5k(self):
        self.worker.salary = 5000
        self.assertEqual(self.worker.get_tax_value(), 500)

    def test_get_tax_value_5_to_10k(self):
        self.worker.salary = 10000
        self.assertEqual(self.worker.get_tax_value(), 1550)

    def test_get_tax_value_other_conds(self):
        self.worker.salary = 20000
        self.assertEqual(self.worker.get_tax_value(), 4550)
        self.worker.salary = 50000
        self.assertEqual(self.worker.get_tax_value(), 16550)
        self.worker.salary = 100000
        self.assertAlmostEqual(self.worker.get_tax_value(), 40050)

    @unittest.expectedFailure
    def test_raises(self):
        Worker("Jane", -1)


