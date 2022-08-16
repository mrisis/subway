import unittest
from Subway.models.bank import *


class TestBank(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount('Mehdi mirzaie', 23, 3242157397, 10000)
        self.account2 = BankAccount('Reza amin', 22, 3152134397, 10000)

    def test_create(self):
        self.assertEqual(self.account1.full_name, 'Mehdi mirzaie')
        self.assertEqual(self.account1.age, 23)
        self.assertEqual(self.account1.national_code, 3242157397)
        self.assertEqual(self.account1.balance, 10000)
        self.assertEqual(self.account1.__repr__(), f"Bank account with {self.account1.account_number}\
 account number for {self.account1.full_name} with {self.account1.balance}\
 balance has created.")

        self.assertEqual(self.account2.full_name, 'Reza amin')
        self.assertEqual(self.account2.age, 22)
        self.assertEqual(self.account2.national_code, 3152134397)
        self.assertEqual(self.account2.balance, 10000)
        self.assertEqual(self.account1.__repr__(), f"Bank account with {self.account1.account_number}\
 account number for {self.account1.full_name} with {self.account1.balance}\
 balance has created.")

    def test_load_all(self):
        obj1 = list(self.account1.load_all())[0].values()
        self.assertIsInstance(*obj1, BankAccount)

        obj2 = list(self.account2.load_all())[0].values()
        self.assertIsInstance(*obj2, BankAccount)

    def test_fullname(self):
        self.assertRaises(FullNameError, BankAccount, 10, 23, 3242157397, 10000)
        self.assertRaises(FullNameError, BankAccount, 'Me', 23, 3242157397, 10000)
        self.assertRaises(FullNameError, BankAccount, 'Mehdi#', 23, 3242157397, 10000)

    def test_age(self):
        self.assertRaises(AgeError, BankAccount, 'Mehdi mirzaie', 23.5, 3242157397, 10000)
        self.assertRaises(AgeError, BankAccount, 'Mehdi mirzaie', -2, 3242157397, 10000)

    def test_national_code(self):
        self.assertRaises(NationalCodeError, BankAccount, 'Mehdi mirzaie', 23, '3242157397', 10000)
        self.assertRaises(NationalCodeError, BankAccount, 'Mehdi mirzaie', 23, 2342, 10000)

    def test_balance(self):
        self.assertRaises(BalanceError, BankAccount, 'Mehdi mirzaie', 23, 3242157397, '10000')
        self.assertRaises(BalanceError, BankAccount, 'Mehdi mirzaie', 23, 3242157397, 10)

    def test_login_bank(self):
        self.assertRaises(LoginError, self.account1.login_bank, '2341')
        self.assertRaises(LoginError, self.account1.login_bank, 2341.5)
        self.assertRaises(LoginError, self.account1.login_bank, 2341)
        self.assertEqual(BankAccount.login_bank(self.account1.account_number), self.account1)

    def test_show_balance(self):
        self.assertEqual(self.account1.show_balance(), 9990)

    def test_deposit(self):
        self.assertRaises(DepositError, self.account1.deposit, '233')
        self.assertRaises(DepositError, self.account1.deposit, 58)
        self.account1.deposit(1000)
        self.assertEqual(self.account1.balance, 11000)

    def test_withdraw(self):
        self.assertRaises(WithDrawError, self.account1.withdraw, '233')
        self.assertRaises(WithDrawError, self.account1.withdraw, 8)
        self.assertRaises(WithDrawError, self.account1.withdraw, 10000)
        self.account1.withdraw(1000)
        self.assertEqual(self.account1.balance, 9000)


if __name__ == '__main__':
    unittest.main()
