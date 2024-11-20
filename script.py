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

def shift_funds(initiator_id: str, initiator_role: str, withdraw_account: str, deposit_account: str, transfer_value: float):
    # Check if both accounts exist
    if withdraw_account not in ACCOUNTS_DB or deposit_account not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[withdraw_account]["balance"] < transfer_value:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[withdraw_account]["balance"] -= transfer_value
    ACCOUNTS_DB[deposit_account]["balance"] += transfer_value
    return f"Successfully transferred ${transfer_value} from {withdraw_account} to {deposit_account}"