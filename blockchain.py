from block import Block

class Blockchain:
    prize_money = 0
    final_response = None
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        self.chain.append(new_block)

    def print_blocks(self):
        recent_block = self.chain[-1]
        print("Block {}".format(recent_block))
        recent_block.print_contents()

    def print_multblocks(self):
        if len(self.chain) > 0:
            for i in range(len(self.chain)):
                current_block = self.chain[i]
                print("Block {} {}".format(i, current_block))
                current_block.print_contents()
        else:
            return "There are no blocks"

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print("Current hash does not equal generated hash")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print("Previous block's hash got changed")
                return False
        return True

    
    def proof_of_work(self, block, difficulty=3):
        moves = 0
        proof = block.generate_hash()
        print("Type \"l\" to begin mining")
        while proof[:difficulty] != "0"*difficulty:
            prompt = input()
            if prompt == "l":
                block.nonce += 1
                moves += 1
                print("You have tried {moves} times to attempt the current problem!".format(moves=moves))
                print(proof)
                proof = block.generate_hash()
            elif prompt == "/exit":
                break
                
            
            else:
                print("The command is not valid")
        
        if prompt != "/exit":
            if self.validate_chain == True:
                print("Congratulations, you have solved the problem! ")
                prize_money = random.randint(1000, 1000000)
                self.prize_money += prize_money
                block.nonce = 0
                moves = 0
                final_response = proof
                return proof 
            else:
                print("Oops, hard luck! You have completed the computational problem but your block does not seem to be mathcing with the others")
                question = input("Would you like to keep trying or would you like to reset the blockchain? *Caution* Your current data will be lost if you reset the blockchain")
                if question == "yes" or question == " yes":
                    self.chain = []
                    block.nonce = 0
                    moves = 0
                    print(prompt())
                elif question == "no" or question == "no ":
                    final_response = None
                    return 
                else:
                    print('Seems liek that is an incorrect answer')      
        else:
            final_response = 'You have exited '
            return 'You have exited '
            
    
