import hashlib
from transaction_handler import process_payment

def hash_to_transfer(hash_value, routing_number, account_number, amount):
    verified = validate_hash(hash_value, routing_number, account_number)
    
    if verified:
        process_payment(routing_number, account_number, amount)
        print(f"Transferred {amount} to {account_number} via {routing_number}")
    else:
        print("Hash verification failed. Transaction rejected.")

def validate_hash(hash_value, routing_number, account_number):
    expected_hash = hashlib.sha256(f"{routing_number}{account_number}".encode()).hexdigest()
    return expected_hash == hash_value
