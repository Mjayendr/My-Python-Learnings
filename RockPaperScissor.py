# this is aprogram to play the game "Rock, paper, Scissors"
# 1=rock, 2=paper, 3 = scissors
def main():
    P1 = input("Player one please input your choice, 1,2 or 3?")
    P2 = input("Player two please input your choice, 1,2 or 3?")
   
    if P1 == P2:
        print "Draw!, No Winner" 
   
    elif P1==1:
        if P2==3:
            print "Rock beat Scissors!, Player1 Wins"
        else:
            print "Paper cover Rock!,Player2 wins"
    elif P1==2:
        if P2==3:
            print "Scissor cuts Paper!,Player2 Wins"
        else:
            print "Paper cover Rock!,Player1 wins"
    elif P1==3:
        if P2==1:
            print "Rock beats Scissor!,Player2 Wins"
        else:
            print "Scissor cuts Paper,Player1 wins"
main()




    