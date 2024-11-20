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

def send_funds(account_holder: str, user_role: str, withdrawal_account: str, receiving_account: str, fund_amount: float):
    # Check if both accounts exist
    if withdrawal_account not in ACCOUNTS_DB or receiving_account not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[withdrawal_account]["balance"] < fund_amount:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[withdrawal_account]["balance"] -= fund_amount
    ACCOUNTS_DB[receiving_account]["balance"] += fund_amount
    return f"Successfully transferred ${fund_amount} from {withdrawal_account} to {receiving_account}"