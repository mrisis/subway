import unittest
from Subway.models.trip import *


class TestTrip(unittest.TestCase):
    def setUp(self):
        fullname = 'Mehdi mirzaie'
        age = 23
        self.account1 = BankAccount(fullname, age, 3242157397, 100000)
        self.user1 = User(fullname, age, self.account1)
        self.user1.buy_card('single_trip')
        self.user1.buy_card('credit')

    def test_create(self):
        trip1 = Trip('kermanshah', 'tehran', 10, self.user1, 'single_trip')
        self.assertEqual(trip1.origin, 'kermanshah')
        self.assertEqual(trip1.destination, 'tehran')
        self.assertEqual(trip1.cost, 10)
        self.assertEqual(trip1.passenger, self.user1)
        self.assertEqual(trip1.__repr__(), f"origin: {trip1.origin}|destination: {trip1.destination}")

    def test_cost(self):
        self.assertRaises(CostError, Trip, 'kermanshah', 'tehran', '32', self.user1, 'single_trip')
        self.assertRaises(CostError, Trip, 'kermanshah', 'tehran', -2, self.user1, 'single_trip')

    def test_check_status(self):
        Trip('tehran', 'kermanshah', 10, self.user1, 'single_trip')
        self.assertRaises(TripError, Trip.check_status, 'tehran', 'kermanshah')

    def test_payment(self):
        trip3 = Trip('kermanshah', 'rasht', 10, self.user1, 'single_trip')
        self.assertRaises(CardError, trip3.payment, 'term')


if __name__ == '__main__':
    unittest.main()
