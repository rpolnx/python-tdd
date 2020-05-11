import unittest

from bankTransfer import BankTransfer as bankTransfer


class BankTransferTest(unittest.TestCase):
    def test_create_account_should_return_account_number(self):
        account = bankTransfer.create_account('test')
        self.assertEqual(35, len(account))

    def test_new_account_starts_with_money_zero(self):
        account_id = bankTransfer.create_account('test')
        account = bankTransfer.get_account(account_id)
        self.assertEqual(0, account['currentMoney'])

    def test_cannot_transfer_invalid_balance(self):
        sender_account_id = bankTransfer.create_account('sender')
        receiver_account_id = bankTransfer.create_account('receiver')
        with self.assertRaises(Exception):
            bankTransfer.transfer_money(sender_account_id, receiver_account_id, 'a')

    def test_cannot_transfer_negative_balance(self):
        sender_account_id = bankTransfer.create_account('sender')
        receiver_account_id = bankTransfer.create_account('receiver')
        with self.assertRaises(Exception):
            bankTransfer.transfer_money(sender_account_id, receiver_account_id, -20.5)

    def test_cannot_transfer_more_money_than_account_balance(self):
        sender_account_id = bankTransfer.create_account('sender')
        receiver_account_id = bankTransfer.create_account('receiver')
        with self.assertRaises(Exception):
            bankTransfer.transfer_money(sender_account_id, receiver_account_id, 2)

    def test_should_transfer_money_from_account_one_to_account_two(self):
        sender_account_id = bankTransfer.create_account('sender', 15)
        receiver_account_id = bankTransfer.create_account('receiver', 25)

        bankTransfer.transfer_money(sender_account_id, receiver_account_id, 10)

        sender_account_final_balance = bankTransfer.get_account(sender_account_id)['currentMoney']
        receiver_account_final_balance = bankTransfer.get_account(receiver_account_id)['currentMoney']

        self.assertEqual(5, sender_account_final_balance)
        self.assertEqual(35, receiver_account_final_balance)


if __name__ == '__main__':
    unittest.main()
