import hashlib
import json
from time import time

class blockchain(object):


    def __init__(self):
        self.chain = []
        self.current_transaction = []

        # Creating the Root Block(Genesis)
        self.new_block(proof = 100, previous_hash = 1)


    def new_block(self, proof, previous_hash=None;):
        # Will Create a new Block and adds it to the chain
        
        # This is the structure of the Blocks in the blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        # Chaining up the Block into the Blockchain

        self.current_transaction =[]
        self.chain.append(block)

        return(block)


    
    def new_transaction(self, sender, recipient, amount ):
         # Creates a new transactions to go into the next mined blocks

        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['Index']  + 1
    
    @staticmethod

    def hash(block):
        # Returns the Hash of the Block
        # shall be using the hashlib library for the work
        # using SHA-256 hasing function :P
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        

    @property

    def last_block(self):
        # Returns the hash of the Last Block in the Chain

        return self.chain[-1]

    