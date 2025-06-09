import random


def shell_game(self):
    print("Let's gamble!")
    bet = int(input("What is your bet? "))
    while bet > 0 and bet <= self.gold:
        print("Okey, we have 3 cups. Let's guess under witch one is gold.")
        cups = [0, 0, 1]
        random.shuffle(cups)
        print("[0] [1] [2]")
        cup_select = int(input("Choose your cup: "))
        if cup_select in [0, 1, 2]:
            self.gold -= bet
            if cups[cup_select] == 1:
                self.gold += 1.5*bet
                print(f"Congratulation! You win! Now, you have {self.gold}")
            else:
                print("You Lose!")
            replay = int(input("Do you want to play again?\n1 - Yes\n2 - No\n"))
            if replay in [1, 2]:
                if replay == 1:
                    bet = int(input("What is your bet? "))
                elif replay == 2:
                    print("Bye, Bye!")
                    break
            else:
                print("Wrong answer! Try again")
        else:
            print("Cup not exists!")
    if bet > self.gold:
        print("Sorry, not enough money.")