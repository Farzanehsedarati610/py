from hash_transfer import hash_to_transfer
from logging_system import log_transaction

# Sample batch of transactions
transaction_batch = [
    {"hash": "hashed_key_123", "destination": "Account789456", "amount": 5000},
    {"hash": "hashed_key_456", "destination": "Account654321", "amount": 7500},
    {"hash": "hashed_key_789", "destination": "Account321654", "amount": 10000},
]

# Process and log each transaction
for transaction in transaction_batch:
    hash_to_transfer(transaction["hash"], transaction["destination"], transaction["amount"])
    log_transaction(transaction["hash"], transaction["destination"], transaction["amount"])

