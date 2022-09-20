import random

humansScore = 0
pooterScore = 0


def humansChoice():
    while True:
        humansSelection = input("\nPlease select: rock | paper | scissors: ")
        if humansSelection == 'rock' or humansSelection == 'paper' or humansSelection == 'scissors':
            break
        else:
            continue
    return humansSelection

'''
def humansChoice():
    validInput = False
    while validInput == False:
        humansSelection = input("\nPlease select: rock | paper | scissors: ")
        if humansSelection == 'rock' or humansSelection == 'paper' or humansSelection == 'scissors':
            validInput = True
    return humansSelection
'''

def pootersChoice():
    gameOptions = ['rock', 'paper', 'scissors']
    pootersSelection = random.choice(gameOptions)
    return pootersSelection

def mainGame():
    rounds = 1
    
    #while rounds < 5:
    for i in range(5):
        print(f'\n\nRound: {rounds}')
        rounds = rounds +1
        humansSelection = humansChoice()
        pootersSelection = pootersChoice()
        print(f"Human: {humansSelection}")
        print(f'Computer: {pootersSelection}')

        if humansSelection == pootersSelection:
            print("its a draw!")        
        elif humansSelection == 'rock' and pootersSelection == 'scissors' or humansSelection == 'scissors' and pootersSelection == 'paper' or humansSelection == 'paper' and pootersSelection == 'rock':
            global humansScore
            humansScore = humansScore +1
            print(f"HUMAN WINS ROUND {rounds-1}\n-----------------")
        else:
            print(f"POOTER WINS ROUND {rounds-1}\n-----------------")
            global pooterScore
            pooterScore = pooterScore +1

def finalScoreAnalysis():
    if humansScore == pooterScore:
        print("IT WAS A DRAW")
    elif humansScore > pooterScore:
        print(f"HUMANITY WINS: \nhumans: {humansScore} : {pooterScore} machines")
    else: 
        print(f"MACHINES RULE: \nhumans: {humansScore} : {pooterScore} machines")

def main():
    mainGame()
    finalScoreAnalysis()

main()
