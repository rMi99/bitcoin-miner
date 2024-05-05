import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.difficulty = 4  # Set the difficulty level
        self.mining_reward = 10  # Set the mining reward

        # Genesis block
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash
        }
        self.transactions = []  # Reset transactions list
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def mine_block(self):
        previous_block = self.chain[-1]
        previous_hash = self.hash_block(previous_block)
        self.add_transaction(sender="0", receiver="Your Wallet", amount=self.mining_reward)
        new_block = self.create_block(previous_hash)
        return new_block

    def hash_block(self, block):
        block_str = str(block['index']) + str(block['timestamp']) + str(block['transactions']) + block['previous_hash']
        return hashlib.sha256(block_str.encode()).hexdigest()

    def show_balance(self, wallet_address):
        balance = 0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['sender'] == wallet_address:
                    balance -= transaction['amount']
                elif transaction['receiver'] == wallet_address:
                    balance += transaction['amount']
        return balance

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    wallet_address = "Your Wallet"

    while True:
        print("\nOptions:")
        print("1. Mine Bitcoin")
        print("2. Show mined Bitcoins")
        print("3. Transfer Bitcoins to Binance wallet")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mined_block = blockchain.mine_block()
            print("Block mined successfully!")
            print("Block details:")
            print(mined_block)

        elif choice == "2":
            balance = blockchain.show_balance(wallet_address)
            print("Your balance:", balance, "BTC")

        elif choice == "3":
            binance_wallet_address = "Binance Wallet"
            amount_to_transfer = float(input("Enter amount to transfer: "))
            if amount_to_transfer > 0 and blockchain.show_balance(wallet_address) >= amount_to_transfer:
                blockchain.add_transaction(sender=wallet_address, receiver=binance_wallet_address, amount=amount_to_transfer)
                print("Transaction successful!")
            else:
                print("Invalid amount or insufficient balance.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")
