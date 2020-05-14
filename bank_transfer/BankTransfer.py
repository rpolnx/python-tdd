import random

database = {'transactions': {}, 'accounts': {}}


def create_account(owner: str, value: float = 0) -> str:
    account_identifier: str = generate_id()
    database['accounts'][account_identifier] = {"owner": owner, "currentMoney": value}
    return account_identifier


def get_account(identification: object) -> dict:
    return database.get('accounts').get(identification)


def transfer_money(sender_account_id: str, receiver_account_id: str, value: float) -> str:
    validate_transfer_value(value)

    sender_account: dict = get_account(sender_account_id).copy()
    receiver_account: dict = get_account(receiver_account_id).copy()

    if value > sender_account['currentMoney']:
        raise Exception('Cannot transfer more money than current\'s account balance')

    sender_account['id'] = sender_account_id
    receiver_account['id'] = receiver_account_id

    transaction_id: str = create_transaction_registry(sender_account, receiver_account, value)

    database['accounts'][receiver_account_id]['currentMoney'] = receiver_account['currentMoney'] + value
    database['accounts'][sender_account_id]['currentMoney'] = sender_account['currentMoney'] - value

    return transaction_id


def get_transaction_by_id(transaction_id: str) -> dict:
    return database.get('transactions').get(transaction_id)


def generate_id() -> str:
    number: int = 32
    alphabet: str = 'abcdef0123456789'
    base_uuid: str = ''
    for x in range(number):
        random_position: int = random.randint(1, len(alphabet))
        base_uuid += alphabet[random_position - 1]
    return base_uuid[0:8] + "-" + base_uuid[8:12] + "-" + base_uuid[12:16] + "-" + base_uuid[16:20] + "-" \
           + base_uuid[20:number - 1]


def validate_transfer_value(value):
    if not isinstance(value, float) and not isinstance(value, int):
        raise Exception('Invalid transfer number')

    if value <= 0:
        raise Exception('Cannot transfer less or equal than zero')


def create_transaction_registry(sender_account: dict, receiver_account: dict, value: float) -> str:
    identification: str = generate_id()

    database['transactions'][identification] = {'sender': {'id': sender_account['id'], 'name': sender_account['owner']},
                                                'receiver': {'id': receiver_account['id'],
                                                             'name': receiver_account['owner']},
                                                'value': value}
    return identification


def get_transactions_by_account_id(account_id: str) -> list:
    return [(k, v) for (k, v) in database['transactions'].items() if
            v['sender']['id'] == account_id or v['receiver']['id'] == account_id]
