import unittest
from Subway.models.user import *
from Subway.models.bank import *


class TestUser(unittest.TestCase):
    def setUp(self):
        fullname = 'Mehdi mirzaie'
        age = 23
        self.account1 = BankAccount(fullname, age, 3242157397, 100000)
        self.user1 = User(fullname, age, self.account1)

    def test_create(self):
        self.assertEqual(self.user1.fullname, 'Mehdi mirzaie')
        self.assertEqual(self.user1.age, 23)
        self.assertEqual(self.user1.account, self.account1)
        self.assertEqual(self.user1.__repr__(), f"user: {self.user1.fullname} with id: {self.user1._User__id_code}")

    def test_load_all(self):
        obj1 = list(self.user1.load_all())[0].values()
        self.assertIsInstance(*obj1, User)

    def test_login_user(self):
        self.assertRaises(LoginError, self.user1.login_user, '23')
        self.assertRaises(LoginError, self.user1.login_user, 21351351235)
        self.assertEqual(User.login_user(self.user1._User__id_code), self.user1)

    def test_buy_card(self):
        self.assertRaises(CardError, self.user1.buy_card, 'card', 100)

        self.user1.buy_card('single_trip')
        self.assertIn('single_trip', self.user1.wallet)

        self.user1.buy_card('credit')
        self.assertIn('credit', self.user1.wallet)

        self.user1.buy_card('term')
        self.assertIn('term', self.user1.wallet)


if __name__ == '__main__':
    unittest.main()
