import hashlib
import json
from time import time
from uuid import uuid4


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
        
    def proof_of_work(self, last_proof):
        # A simple Proof of work algorithm
        # Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        # p is the previous proof, and p' is the new proof

        proof = 0

        while self.valid_proof(last_proof, proof) is False
            proof += 1

        return proof

    @staticmethod

    def hash(block):
        # Returns the Hash of the Block
        # shall be using the hashlib library for the work
        # using SHA-256 hasing function :P
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        
    def valid_proof(last_proof, proof)
        # An algorithm that helps to validate the proof
        # The guess var is typical hash function with 2 inputs of 'last proof' and 'proof'

        guess = 'f{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha3_256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property

    def last_block(self):
        # Returns the hash of the Last Block in the Chain

        return self.chain[-1]

    