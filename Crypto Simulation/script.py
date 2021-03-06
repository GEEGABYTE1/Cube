from blockchain import Blockchain
#from user_value import Account
import time
from os import system
import random
from datetime import datetime


class Introduction: 
    users = []
    local_blockchain = Blockchain()
    amount = 0
    transaction = 0
    value = 5
    moves = 0
    blocks_mined = 0
    total_trans = []
    def bucks(self):
        counter = 0
        random_init = random.randint(1, 1000)

        while True:
            prompt = input()

            if prompt == "a":
                self.amount += self.value
            elif prompt == "/view":
                print("Current date and time {date}".format(date=datetime.now()))
                print("You currently have ${amount}".format(amount=self.amount))
            elif prompt == "/view_value":
                print("Your value is increasing by $" + str(self.value) + " per a currently")
            
            elif prompt == "/exit":
                self.amount = self.amount
                break

            else:
                print("You have not entered a correct value")
            if counter % 7200 == 0:
                if random_init % 10 == 0:
                    self.value *= 6
                    counter += 1

                elif random_init % 8 == 0:
                    self.value *= 5
                    counter += 1

                elif random_init % 5 == 0:
                    self.value *= 4
                    counter += 1

                elif random_init % 4 == 0:
                    self.value *= 3
                    counter += 1

                elif random_init % 2 == 0:
                    self.value *= 2
                    counter += 1
                else:
                    counter += 1
            else:
                pass
            counter += 1


    def mine(self):
        print("Welcome to mining") 
        
        if len(self.local_blockchain.chain) >= 15:
            print("Congratulations, looks like you have some block(s) you can mine! ")
            print("Here are your blocks that you currently have " + str(self.local_blockchain.print_multblocks()))
            time.sleep(1)
            while True:
                index = input("Please select the number of the block of which you want to mine! ")
                if int(index) < len(self.local_blockchain.chain):
                    cur_block = self.local_blockchain.chain[int(index)]
                    print(self.local_blockchain.proof_of_work(cur_block))

                    if self.local_blockchain.final_response == 'You have exited ':
                        break

                    elif self.local_blockchain.final_response != None and self.local_blockchain.final_response != 'You have exited ':
                        self.amount += self.local_blockchain.prize_money

                    else:
                        self.amount += self.local_blockchain.prize_money
                        break

                else:
                    print("The index is invalid ")
                
            
            else:
                print('You do not have enough blocks to mine! ')


    
    
    def gameplay(self):
        print("Hello, welcome to Cube! A generalized simulated crypto trading program! ")
        
        time.sleep(1)
        print()

        playing = True 
        while True:
            self.amount = self.amount
            print("You currently have $" + str(self.amount))
            time.sleep(0.5)
            print()
            print("If you want to make some quick bucks, please type /bucks")
            time.sleep(1)
            print("If you want to mine a cube, please type /mine")
            time.sleep(1)
            print("If you want to make a transaction with someome, please type /transaction\n")
            user_prompt = input()

            if user_prompt == "/bucks":
                print("Welcome to the quickest and easiest way to make money")
                print("If you are lucky, you might even increase the value of money you get! ")
                time.sleep(1)
                print("\n")
                print("---------------------------------")
                print("Controls: ")
                time.sleep(1)
                print("Type /amount to see the money you have")
                print("Type \"a\" to start gaining money. The more you type, the more you earn ;)")
                print("Type /view_value to see the rate of money increasing per click")
                print("Type /exit to exit the process")
                time.sleep(1)
                print("Let's start making money!")
                time.sleep(3)
                clear = lambda: system('clear')
                clear()
                

                print(self.bucks())
                user_prompt = None
            
            if user_prompt == "/mine":
                print(self.mine())
            
            elif user_prompt == "/self_transactions":
                print(self.transaction)
            
            elif user_prompt == "/transaction": 
                trading = True
                chance = random.randint(1, 2)
                while trading:
                    print("Welcome to the transactions area where you can sell and trade your money")
                    print("If you can get up to 15 transactions, you will be able to get yourself a block, in which you can start mining!")
                    time.sleep(1)
                    clear = lambda: system('clear')
                    clear()
                    

                    print("Here are the users that are currently online: ")
                    time.sleep(1)
                    print(self.add_user())
                    print("Here is the amount of money you have:$" + str(self.amount))
                    user_transaction = input("Please enter a user that you would like to trade with: ")

                    if user_transaction == "/check_transactions":                                                                               ###Block Initialization
                        if self.transaction >= 15:
                            print("Congratulations, you will receive " + str(self.transaction) + " block(s)! ")
                            for i in self.total_trans:
                                self.local_blockchain.add_block(i)                                                                              #block_transaction
                                print(self.local_blockchain.print_blocks())
                            self.total_trans = []
                            self.transaction = 0 
                        else:
                            print('You currently have ' + str(self.transaction))
                            print('You need ' + str(200 - self.transaction) + ' to obtain a block!')

                    if user_transaction == "/exit" or user_transaction == "nobody" or user_transaction == "no one":
                        break
                    else:
                    
                        base_users = self.users
                        for i in self.users:
                            if user_transaction in i.keys():
                                deal = input("Would you like to give money?: ")

                                if deal == "yes " or deal == "yes":
                                    money = input("Please enter an amount you want to give: ")

                                    money_int = int(money)
                                    
                                    if money_int >= 5:
                                        if self.amount >= money_int:
                                        
                                            i[user_transaction] += money_int
                                            
                                            block_transaction = {"sender": "You", "receiver": user_transaction, "amount": str(money)}
                                            #self.local_blockchain.add_block(block_transaction)
                                            time.sleep(0.5)
                                            print("Here is your recent transaction: ")
                                            time.sleep(1)
                                            print(block_transaction)
                                            self.total_trans.append(block_transaction)
                                            #print(self.local_blockchain.print_blocks())
                                            self.amount -= money_int
                                            self.transaction += 1
                                            time.sleep(1.5)
                                                
                                            
                                        else:
                                            print("You do not have enough money! ")
                                    else:
                                        print("You have to give more than $5!")
                                        time.sleep(1)

                                if deal == "no" or deal == "no " or deal == "/exit" or deal == "/exit ":
                                    break

                                    

                                if chance == 2:
                                    time.sleep(1.5)
                                    random_user = random.randint(0, len(base_users) - 1)
                                    random_amount = random.randint(100, 10000)

                                    chosen_agent = self.users[random_user].keys()
                                    for i in range(len(self.users)):
                                        if random_user == i:
                                            req_key = self.users[i]
                                            
                                            if req_key["user" + str(random_user)] >= random_amount:
                                                block_transaction = {"sender": "user" + str(random_user), "receiver": "you", "amount": random_amount}
                                                #self.local_blockchain.add_block(block_transaction)
                                                print("Looks like, a user sent you money!")
                                                time.sleep(0.5)
                                                print("Here is the recent transaction")
                                                time.sleep(1)
                                                print(block_transaction)
                                                self.total_trans.append(block_transaction)
                                                #print(self.local_blockchain.print_blocks())
                                                self.amount += random_amount 
                                                req_key["user" + str(random_user)] -= random_amount
                                                self.transaction += 1
                                                break
                                        
                                            else:
                                                break
                                            break
                                            
                            else:
                                continue
                            
                            for i in self.users:
                                if not user_transaction in i.keys():
                                    continue 
                            break

                            
                                                    
                        break
                        
                
                        




                

    def add_user(self):
        number = random.randint(1, 1000)
        
        for i in range(number):
            rand_value = random.randint(1, 1000000)
            self.users.append({'user' + str(i): rand_value})

        
        
        for i in self.users:
            print(i.keys())

       

        
        
            


        



test = Introduction()


#test.add_user()
test.gameplay()
