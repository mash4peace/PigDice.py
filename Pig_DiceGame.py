import random
#Here, I am defining game rules
def game_Rules(n):
    print(n + ", hello, let's play PIG game ")
    print("Roll the dice as many you would like ")
    print("If you roll a 1 , you gonna lose all point you have accomulated ")
    print("Holding will save your pointed for the turn !!")
    print("")
#Play function
def play():
    #Assigning the trun to start @1
    turn = 1
    score = 0  #Score equals 0
    gameOve = False #A boolean operater to assign False
    while not gameOve:
        turn, score, gameOve = takeTurn(turn, score, gameOve)
    print()
    print("Game Over !!!!")
def takeTurn(turn, score, gameOver): #Turning
    print("Turn ", turn)
    scoreThisTurn = 0
    turnOver = False
    while not turnOver:
        #Here, letting the user input
        choice = input("Roll or hold ? (r/h)")
        if choice == "r": #If choice equals "r" Roll the dice
            turn, score, scoreThisTurn, turnOver = \
                roll_die(turn, score, scoreThisTurn)
        elif choice == "h" :
            turn, score, turnOver, gameOver = \
                holdTurn(turn, score, scoreThisTurn)
        else:
            print("Invalid choice. Try again . ")
    return  turn, score, gameOver
#Roll dice
def roll_die(turn, score, scoreThistrun):
    die = random.randint(1,6) #A random from 1 to 6
    print("Die: ", str(die))
    if die == 1: #If the roll die equals 1 , Yoy wanna lose all points
        scoreThistrun = 0 #Re assigning to be Zero
        turn += 1
        print("Turn Over. No score.\n")
        turnOver = True
    else:
        scoreThistrun += die
        turnOver = False
    return turn, score, scoreThistrun, turnOver
#Here, holding the game to save your points and allowing other player to play
def holdTurn(turn, score, scoreThisTurn ):
    print("Score for turn , scoreThisTurn")
    score += scoreThisTurn
    print("Total Score : ", score, "\n")

    turnOver = True
    gameOver = False
    if(score >= 20) :
        print("You finished in ", turn, " turns!")
        gameOver = True
        return  turn,score ,turnOver, gameOver
    turn += 1
    return  turn, score, turnOver, gameOver
#Main function
def main():
    choice = "y"
    while choice.lower() == "y" or choice.upper() == "Y":
        print("Welcome to this program !!!")
        name = input("What is your name ? : ")
        game_Rules(name)
        play()
        choice = input("Continue (Y/N)")
        print()
    print(name + ", thanks for using this program !!!!")
#Calling the main
main()





