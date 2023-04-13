table = ["_","_","_",
         "_","_","_",
         "_","_","_"
        ]
def PrintTable(): 
    print(table[0] , " | " , table[1] , " | " , table[2])
    print(table[3] , " | " , table[4] , " | " , table[5])
    print(table[6] , " | " , table[7] , " | " , table[8])
PrintTable()

def EndGame():
    if(table[0] == table[1] == table[2] != "_") or \
      (table[3] == table[4] == table[5] != "_") or \
      (table[6] == table[7] == table[8] != "_") or \
      (table[0] == table[3] == table[6] != "_") or \
      (table[1] == table[4] == table[7] != "_") or \
      (table[2] == table[5] == table[8] != "_") or \
      (table[0] == table[4] == table[8] != "_") or \
      (table[2] == table[4] == table[6] != "_"):
        return "win"
    elif  "_" not in table:
            return "Tie"
    else:
            return "Play"
    
def Turn(player):
    print(player+"'s turn.")
    position = input("Enter the Poistion from 1-9.\n")
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        print("Enter the proper position.")
        break
    position = int(position)-1
    while table[position] != "_":
         position = int(input("Position has alread taken.")) - 1
    table[position] =  player
    PrintTable()
def Start():
    CurrentPosition = "X"
    GameOver = False
    while not GameOver:
        Turn(CurrentPosition)
        game_result = EndGame()
        if game_result == "win":
            print(CurrentPosition + " wins!")
            GameOver = True
        elif game_result == "tie":
            print("It's a tie!")
            GameOver = True
        else:
            CurrentPosition = "O" if CurrentPosition == "X" else "X"
Start()
