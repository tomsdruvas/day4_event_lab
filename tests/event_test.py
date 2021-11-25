import unittest
from src.event import Event
from src.performer import Performer

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.houdini = Performer("Houdini")
        self.paul = Performer("Paul Daniels")
        self.performers = [self.houdini, self.paul]
        self.magicShow = Event("Magic Show", 25, self.performers)

    def test_ticket_sale_increases_revenue(self):
        self.magicShow.increase_revenue(self.magicShow.ticket_price)
        self.assertEqual(25, self.magicShow.revenue)