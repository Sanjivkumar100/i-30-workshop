from random import randint
pscore=0
cscore=0

def maingame(n):
    print("Enter rock or paper or scissors")
    rounds=0
    game=['rock','paper','scissors']
    computer=game[randint(0,2)]
    global pscore
    global cscore
   
    while(rounds!=n):
        player=input("Player game:")
        if player=='rock':
                if computer==game[2]:
                   
                    pscore+=1
                    print(f"Player score:{pscore}")
                    print(f"Computer score :{cscore}")
                elif computer==game[1]:
                        
                        cscore+=1
                        print(f"Player score:{pscore}")
                        print(f"Computer score :{cscore}")
                else:
                    print("Same")
        elif player=='scissors':
                if computer==game[0]:
                    
                    cscore+=1
                    print(f"Player score:{pscore}")
                    print(f"Computer score :{cscore}")
                elif computer==game[1]:
                    
                    pscore+=1
                    print(f"Player score:{pscore}")
                    print(f"Computer score :{cscore}")
                else:
                        print("Same")
        elif player=='paper':
                    if computer==game[0]:
                        
                        pscore+=1
                        print(f"Player score:{pscore}")
                        print(f"Computer score :{cscore}")
                    elif computer==game[2]:
                            
                            cscore+=1
                            print(f"Player score:{pscore}")
                            print(f"Computer score :{cscore}")
                    else:
                        print("Same")
        rounds+=1
        
def score():
    global pscore
    global cscore
    if pscore>cscore:
                print("Player wins")
    elif cscore>pscore:
                print("Computer wins")
    else:
            print("Tie")   


       
        
