import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.bob = Customer("Bob Slob", 50.00, "The Great Waldo")

    def test_check_money_in_wallet(self):
        self.assertEqual(50.00, self.bob.wallet)

    def test_check_reduce_wallet(self):
        self.bob.reduce_wallet(10.00)
        self.assertEqual(40.00, self.bob.check_wallet())

