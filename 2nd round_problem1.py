#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:11:29 2018

@author: arry
"""

# module 2 create a cryptocurrency

import datetime
import hashlib
import json
import requests
from urllib.parse import urlparse

#building blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        
        self.nodes =  set()
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions
                 }
        self.transactions = []
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index +=1
        return True
    
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1
    
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
        
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
    
    
#mining blockchain

def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congrats, you just mined a block!',
                'index': block['index'],
                'timestamp':block['timestamp'],
                'proof':block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    return json.dumps(response)

def get_chain():
   response = {'chain': blockchain.chain,
               'length': len(blockchain.chain)} 
   return json.dumps(response), 200

def verify_chain():
    return json.dumps(blockchain.is_chain_valid(blockchain.chain))


def add_transaction(sender, receiver, amount):
    index = blockchain.add_transaction(sender, receiver, amount*0.9)
    blockchain.add_transaction(sender, loyalty, amount*0.1)
    response = {'message': f'This transaction will be added to Block {index}'}
    return json.dumps(response)

def refund_transaction(merchant, sender, amount):
    index = blockchain.add_transaction(merchant, sender, amount*0.9)
    blockchain.add_transaction(merchant, sender, amount*0.1)
    response = {'message': f'This transaction will be added to Block {index}'}
    return json.dumps(response)

def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The nodes had different chains so the chain was replaced',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'All good. The chain is the largest one.',
                    'actual_chain': blockchain.chain}
    return json.dumps(response)

# creating a blockchain main()
    
blockchain = Blockchain()
loyalty = "loyalty"
sender = "arisht"
merchant = "merchant"

print(add_transaction(sender, merchant, 100))
print(mine_block())
print(add_transaction(sender, merchant, 100))
print(mine_block())
print(add_transaction(sender, merchant, 100))
print(mine_block())
print(add_transaction(sender, merchant, 100))
print(mine_block())
print(add_transaction(sender, merchant, 100))
print(mine_block())

print(refund_transaction(merchant,sender, 100))
print(mine_block())
print(refund_transaction(merchant, sender, 100))
print(mine_block())