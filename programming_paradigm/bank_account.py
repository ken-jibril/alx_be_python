import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    
    parts = sys.argv[1].split(':')
    command = parts[0]
    
    amount = None
    if len(parts) > 1:
        amount = float(parts[1])
    
    
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    
        
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
            
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

