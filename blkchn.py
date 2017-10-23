import hashlib
import json
from time import time
from uuid import uuid4
from textwrap import dedent
from flask import Flask, jsonify, request

class Blockchain():


    def __init__(self):
        self.chain = []
        self.current_transaction = []
        self.nodes = set()
        # Creating the Root Block(Genesis)
        self.new_block(proof = 100, previous_hash = 1)


    def new_block(self, proof, previous_hash=None):
        # Will Create a new Block and adds it to the chain
        
        # This is the structure of the Blocks in the blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transaction,
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

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod

    def hash(block):
        # Returns the Hash of the Block
        # shall be using the hashlib library for the work
        # using SHA-256 hasing function :P
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        
    def valid_proof(last_proof, proof):
        # An algorithm that helps to validate the proof
        # The guess var is typical hash function with 2 inputs of 'last proof' and 'proof'

        guess = 'f{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha3_256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property

    def last_block(self):
        # Returns the hash of the Last Block in the Chain

        return self.chain[-1]

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])


def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block()
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    block = blockchain.new_block(proof)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])

def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])

def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

    
    
    

    