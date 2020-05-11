import random

database = {}


def create_account(owner, value=0):
    identifier = generate_id()
    node = {"owner": owner, "currentMoney": value}
    database[identifier] = node
    return identifier


def get_account(id):
    return database.get(id)


def transfer_money(sender_account_id, receiver_account_id, value):
    if not isinstance(value, float) and not isinstance(value, int):
        raise Exception('Invalid transfer number')

    if value <= 0:
        raise Exception('Cannot transfer less or equal than zero')

    sender_account_value = get_account(sender_account_id)['currentMoney']
    receiver_account_value = get_account(receiver_account_id)['currentMoney']

    if value > sender_account_value:
        raise Exception('Cannot transfer more money than current\'s account balance')

    database[receiver_account_id]['currentMoney'] = receiver_account_value + value
    database[sender_account_id]['currentMoney'] = sender_account_value - value


def generate_id():
    number = 32
    alphabet = 'abcdef0123456789'
    base_uuid = ''
    for x in range(number):
        random_position = random.randint(1, len(alphabet))
        base_uuid += alphabet[random_position - 1]
    return base_uuid[0:8] + "-" + base_uuid[8:12] + "-" + base_uuid[12:16] + "-" + base_uuid[16:20] + "-" \
           + base_uuid[20:number - 1]
