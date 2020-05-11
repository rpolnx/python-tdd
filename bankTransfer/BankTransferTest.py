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

    def test_should_create_transaction_history(self):
        sender_account_id = bankTransfer.create_account('sender', 15)
        receiver_account_id = bankTransfer.create_account('receiver', 25)

        transaction_id = bankTransfer.transfer_money(sender_account_id, receiver_account_id, 10)

        transaction = bankTransfer.get_transaction_by_id(transaction_id)

        self.assertTrue(transaction)

    def test_should_get_all_transactions_from_account(self):
        sender_account_id = bankTransfer.create_account('sender', 15)
        receiver_account_id_1 = bankTransfer.create_account('receiver', 25)
        receiver_account_id_2 = bankTransfer.create_account('receiver2', 0)

        bankTransfer.transfer_money(sender_account_id, receiver_account_id_1, 10)
        bankTransfer.transfer_money(sender_account_id, receiver_account_id_2, 5)

        sender_transactions = bankTransfer.get_transactions_by_account_id(sender_account_id)
        receiver_transactions = bankTransfer.get_transactions_by_account_id(receiver_account_id_1)
        receiver_transactions_2 = bankTransfer.get_transactions_by_account_id(receiver_account_id_2)

        self.assertEqual(2, len(sender_transactions))
        self.assertTrue(1, len(receiver_transactions))
        self.assertTrue(1, len(receiver_transactions_2))


if __name__ == '__main__':
    unittest.main()
