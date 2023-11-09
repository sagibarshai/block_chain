from hashlib import sha256
import json

waiting_for_input = True

owner = {
    "name":"Sagi",
    "balance":100
}

def create_participant(name):
    return {"name" : name , "balance":0}


participants = [
                owner, 
                create_participant(name="Shelly"),
                create_participant(name="Nerdit"),
                create_participant(name="Maor"),
                create_participant(name="Sapir"),
                create_participant(name="Zuza"),
                create_participant(name="Catia"),
                create_participant(name="Alex"),
                create_participant(name="Rahel")
                ]

genisis_block = {
    "previous_hash":"",
    "data":"Genisis Block",
    "index":0,
    "transactions":[],
    "previous_proof":0
}

blockchain = [genisis_block]
open_transactions = []

    
def add_new_transaction():
    
  
    names = [obj["name"] for obj in participants]
    recipient = None    
    while recipient not in names:
          print("Enter a recipient name")
          recipient = input()
          
        
    
    sender = None
    sender_balnce = None
    
    while sender not in names:
          print("Enter a sender name")
          sender = input()
          
    while sender_balnce == None:
        for participant in participants:
            print(sender_balnce)    
            if participant["name"] == sender:
                sender_balnce = participant["balance"]


    print(sender_balnce)
    amount = None
    while amount == None:
        print("Enter an amount")
        check_amount = input() 
        if check_amount.isnumeric() and int(check_amount) <= sender_balnce:
            amount = int(check_amount)
            sender_balnce -= amount
        
    open_transactions.append({"recipient":recipient,"amount": amount, "sender": sender})
    for participent in participants:
        print(participants)
        if participent["name"] == sender:
            participent["balance"] = sender_balnce
        if participent["name"] == recipient:
            participent["balance"] += amount
    
    


#  return bytes
def to_digest(new_proof,previous_proof,index,data):
   digest =  str(new_proof + previous_proof ** 2 + index * 1/2 + index ) +  json.dumps(data)
   return digest.encode()


def proof_of_work(previous_proof,index,data):
    new_proof = 1
    check_proof = False    
    
    while not check_proof:
        digest = to_digest(new_proof,previous_proof,index,data)
        hash_value = sha256(digest).hexdigest()
        print(hash_value)
        
        if hash_value[0:4] == "112f":
            check_proof = True
        else:
            new_proof+=1
    return new_proof


def mine_block():
    global open_transactions
    last_block = blockchain[-1]
    
    last_block_json = json.dumps(last_block, sort_keys=True)
    last_block_hash = sha256(last_block_json.encode()).hexdigest()
    proof = proof_of_work(last_block["previous_proof"],len(blockchain),open_transactions)
    block = {
        "previous_hash":last_block_hash,
        "index":len(blockchain),
        "previous_proof":last_block["previous_proof"],
        "transactions":open_transactions,
        "proof":proof,
        
    }
    
    
    blockchain.append(block)
    
    open_transactions = []

    



def __init__():
    global waiting_for_input    
    
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    
    user_choise = input()
    
    if user_choise == "1":
        add_new_transaction()
        print(open_transactions)
    elif user_choise == "2":
        mine_block()
    elif user_choise == "3":
        print(blockchain)
    elif user_choise == "4":
        print(participants)
    elif user_choise == "5":
        pass
    elif user_choise == "h":
        pass
    elif user_choise == "q":
        waiting_for_input = False    
    else: 
        pass
    
    
while waiting_for_input:
    __init__()