import unittest
from src.performer import Performer

class TestPerformer(unittest.TestCase):
    def setUp(self):
        self.waldo = Performer("The Great Waldo")
        self.waldo.earnings = 10

    def test_performer_has_name(self):
        self.assertCountEqual("The Great Waldo", self.waldo.name)

    def test_performer_has_earnings(self):
        self.assertEqual(10, self.waldo.earnings)