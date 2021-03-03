from datetime import datetime
import random


class Account:
    amount = 0

    def __init__(self):
        counter = 0
        random_init = random.randint(1, 1000)
        self.value = 5

        while True:
            prompt = input()

            if prompt == "a":
                self.amount += self.value
            elif prompt == "/view":
                print("Current date and time {date}".format(date=datetime.now()))
                print("You currently have ${amount}".format(amount=self.amount))
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





            


test = Account()





