import json

def log_transaction(hash_value, destination, amount):
    transaction_record = {
        "hash": hash_value,
        "destination": destination,
        "amount": amount
    }
    
    with open("transactions.json", "a") as file:
        json.dump(transaction_record, file)
        file.write("\n")
    
    print(f"Logged transaction: {transaction_record}")

# Example transaction logging
log_transaction("hashed_key_123", "Account789456", 5000)
