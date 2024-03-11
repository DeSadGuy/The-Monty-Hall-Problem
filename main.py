# create 3 doors
from enum import Enum 
from random import randint 


class Prize(Enum):
    CAR = 1
    GOAT = 2 

class Door():
    def __init__(self):
        self.secretBehindDoor :Prize = Prize.GOAT
        self.isOpen = False

    def openDoor(self):
        self.isOpen = True

    def setPrize(self):
        self.secretBehindDoor = Prize.CAR

class Stats():
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    def getWinPercentage(self):
        return self.wins / (self.wins + self.losses) * 100

    def getLossPercentage(self):
        return self.losses / (self.wins + self.losses) * 100

    def getStats(self):
        return f"Wins: {self.wins}\nLosses: {self.losses}\nWin Percentage: {self.getWinPercentage():.2f}%\nLoss Percentage: {self.getLossPercentage():.2f}%"

    def game(self):

        # create the 3 doors and show 
        doors = [Door(), Door(), Door()]
        # randomly select one door to have a prize 
        doors[randint(0,2)].setPrize()
        # randomly select one door to be the player's choice 
        playerChoice = randint(0,2) 
        # randomly select one door to be the host's choice The host will never select the door with the prize 
        while True:
            hostChoice = randint(0,2)
            if hostChoice != playerChoice and doors[hostChoice].secretBehindDoor != Prize.CAR:
                break
        # open the door that the host has selected
        doors[hostChoice].openDoor()
        # the player will always switch doors 
        for i in range(3):
            if i != playerChoice and i != hostChoice:
                playerChoice = i
                break
        # open the door that the player has selected
        doors[playerChoice].openDoor()
        # show the results
        print(f"The player chose door {playerChoice+1} and the host chose door {hostChoice+1}")
        for i in range(3):
            print(f"Door {i+1} is {'open' if doors[i].isOpen else 'closed'} and has a {doors[i].secretBehindDoor.name.lower()} behind it")

        # if the player has won
        if doors[playerChoice].secretBehindDoor == Prize.CAR:
            print("You won!")
            self.wins += 1
        else:
            print("You lost!")
            self.losses += 1

    def game2(self):
        doors = [Door(), Door(), Door()]
        doors[randint(0,2)].setPrize()
        while True:
            hostChoice = randint(0,2)
            if doors[hostChoice].secretBehindDoor != Prize.CAR:
                break
        doors[hostChoice].openDoor()
        while True:
            playerChoice = randint(0,2)
            if playerChoice != hostChoice:
                break
        doors[playerChoice].openDoor()
        # show the results
        print(f"The player chose door {playerChoice+1} and the host chose door {hostChoice+1}")
        for i in range(3):
            print(f"Door {i+1} is {'open' if doors[i].isOpen else 'closed'} and has a {doors[i].secretBehindDoor.name.lower()} behind it")

        # if the player has won
        if doors[playerChoice].secretBehindDoor == Prize.CAR:
            print("You won!")
            self.wins += 1
        else:
            print("You lost!")
            self.losses += 1

def main():
    stats = Stats()
    stats2 = Stats()
    for i in range(1000):
        stats.game()
    for i in range(1000):
        stats2.game2()
    print("Game 1 - switch doors first")
    print(stats.getStats())
    print("Game 2 - host opens door first")
    print(stats2.getStats())
if __name__ == "__main__":
    main()
