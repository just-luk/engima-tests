ACCOUNTS_DB = {
    "ACC001": {
        "account_number": "ACC001",
        "owner_id": "USER1",
        "balance": 1000.0
    },
    "ACC002": {
        "account_number": "ACC002",
        "owner_id": "USER2",
        "balance": 500.0
    }
}

def execute_transfer(employee_id: str, role_value: str, source_acct: str, target_acct: str, total_amount: float):
    # Check if both accounts exist
    if source_acct not in ACCOUNTS_DB or target_acct not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[source_acct]["balance"] < total_amount:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[source_acct]["balance"] -= total_amount
    ACCOUNTS_DB[target_acct]["balance"] += total_amount
    return f"Successfully transferred ${total_amount} from {source_acct} to {target_acct}"