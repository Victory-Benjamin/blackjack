import random
import os
os.system("cls")



cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
usercards = []
computerscards = []
gameover = False


def dealcard():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    newcard = random.choice(cards)
    return newcard
    
        

def userwantsnewcard():
    usercards.append(dealcard())
    totaluserscard = sum(usercards)
    print (totaluserscard)
    # if totaluserscard >21:
    #     print ("lose, you went overload")



while not gameover:
    for n in range (2):
        usercards.append(dealcard())
        totaluserscard = sum(usercards)      
    print (totaluserscard)
    drawcard = input("do you want to pick another card?\n").lower()
    if drawcard == "yes":
        userwantsnewcard()
        # if totaluserscard ==21 and len(usercards) ==2:
        #     usercards = 0
        #     print ("Blackjack")

        # elif totaluserscard >21:
        #     print ("lose, you went overload")
    if drawcard == "no":
        totalcomputercards = sum(computerscards)
        while totalcomputercards <17:
            computerscards.append(dealcard()) 
            if totalcomputercards ==21 and len(computerscards) ==2:
                computerscards = 0
                print ("Blackjack")

            elif totalcomputercards > 21:
                print (f"computer lost, went overboard with {totalcomputercards} whereas user wins with {totaluserscard}")

    gameover = False
    break
totalcomputercards = sum(computerscards)
totaluserscard = sum(usercards)

if totaluserscard ==21 and len(usercards) ==2:
    usercards = 0
    print ("Blackjack")
if totalcomputercards ==21 and len(computerscards) ==2:
    totalcomputercards = 0
    print ("Blackjack")
elif totaluserscard or totalcomputercards >21:
    print ("lose, you went overload")
elif sum(computerscards) > sum(usercards) and 21 >= sum(computerscards):
    print (f"computer wins with {totalcomputercards}") 
elif totalcomputercards == totaluserscard:
    print (f"it is a draw. you both have {totalcomputercards}")
else: 
    print (f"user wins with {totaluserscard} whereas computer loses with {totalcomputercards}")
  
        # primtnffnjg