import unittest
from src.performer import Performer

class TestPerformer(unittest.TestCase):
    def setUp(self):
        self.earnings = 10
        self.performer = Performer("The Great Waldo")

    def test_performer_has_name(self):
        self.assertCountEqual("The Great Waldo", self.performer.name)