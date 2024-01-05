##Craps


import random
## function for come out roll
def come_out_roll():
    ##call bets from other functions
    passlinebet = pass_line_bet()
    dontpasslinebet = dont_pass_line_bet()
    ## calculate roll
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1 + die2
    print(f"Come Out Roll = {roll}")
    #calculate result and distribute winnings
    if roll == 7 or roll ==  11:
        print("Pass Line Wins")
        if passlinebet > 0 and dontpasslinebet == 0:
            winnings = passlinebet * 2
            print(f"You win ${winnings}")
        else:
            print("You Lost")
    elif roll == 2 or roll == 3 :
        print("Pass Line Loses")
        if passlinebet > 0 and dontpasslinebet == 0:
            print("You Lose")
        elif dontpasslinebet > 0:
            winnings = dontpasslinebet * 2
            print(f"You win ${winnings}")
    elif roll == 12 :
        print("Pass Line Loses")
        if passlinebet > 0 and dontpasslinebet == 0 :
            print("You Lose")
        elif dontpasslinebet > 0:
            print("Push")
        
    else:
        #Establish point and pass arguement to other function
        print(f"Point = {roll}")
        point_play(roll, passlinebet, dontpasslinebet)
        
## Function for point play 
def point_play(roll, passlinebet, dontpasslinebet):
    ## Initialize variable
    result = 0
    ## Call variables from other functions
##    place_bet = place_betting()
##    print(place_bet)
    passline_oddsbet = pass_line_odds_bet()
    ## Create loop to roll until round is terminated
    while result != 7 :
        ## Calculate roll
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        result = die1 + die2
        print(result)
        ## Calculate result of play and distribute winnings
##        if result == place_bet :
##            print("Place bet wins")
##            if result == 4 or result == 10 :
##                payout = place_betamt + (place_betamt * 1.8)
##                print("Payout = ${payout}")
##                continue
##            elif result == 5 or result == 9:
##                payout = place_betamt + (place_betamt * 1.4)
##                print("Payout = ${payout}")
##                continue
##            elif result == 6 or result == 8:
##                payout = place_betamt + (place_betamt * 1.17)
##                print("Payout = ${payout}")
##                continue
            ## calculate when the round stops and distribute winnings
        if result == roll :
            if roll == 4 or roll == 10 :
                if passlinebet > 0 and dontpasslinebet == 0:
                    print("You Win")
                    winnings = (passline_oddsbet * 3) + (passlinebet * 2)
                    print(f"Payout = ${winnings}")
                else:
                    print("You Lose")
                    break
            elif roll == 5 or roll == 9 :
                if passlinebet > 0 and dontpasslinebet == 0:
                    print("You Win")
                    winnings = passline_oddsbet + (passline_oddsbet * 1.5) + (passlinebet * 2)
                    print(f"Payout = ${winnings}")
                else:
                    print("You Lose")
                    break
            elif roll == 6 or roll == 8 :
                if passlinebet > 0 and dontpasslinebet == 0:
                    print("You Win")
                    winnings = passline_oddsbet + (passline_oddsbet * 1.2) + (passlinebet * 2)
                    print(f"Payout = ${winnings}")
                else:
                    print("You Lose")
                    break
            come_out_roll()
            break
        elif result == 7 :
            if dontpasslinebet > 0:
                winnings = dontpasslinebet * 2
                print(f"You win ${winnings}")
            elif passlinebet > 0:
                print("You lose")
            break
## function for user to bet against pass line
def dont_pass_line_bet():
    ## employ error handling
    try:
        userinput = input("Would you like to place a Dont Pass Line Bet? (y/n) ")
        if userinput == 'y':
            dontpasslinebet = int(input("How much would you like to bet? "))
            if dontpasslinebet > 0:
                return dontpasslinebet
            else:
               print("Invalid Bet Amount") 
        else:
            dontpasslinebet = 0
            ## return player bet
            return dontpasslinebet
    except ValueError:
        print("Invalid Input")

## function for user to bet against pass line
def pass_line_bet():
    ## employ error handling
    try:
        passlinebet = int(input("How much would you like to bet on Pass Line? (Enter 0 if none) "))
        if passlinebet > 0:
            ## return player bet
            return passlinebet
        else:
            print("No Pass Line bet recorded.")
            return passlinebet == 0
    except ValueError:
        print("Invalid Input")
## function for user to bet bet for the pass line
def pass_line_odds_bet():
    ## employ error handling
    try:
        userinput = input("Would you like to place a Pass Line Odds Bet? (y/n) ")
        if userinput == 'y':
            passline_oddsbet = int(input("How much would you like to bet? "))
            if passline_oddsbet > 0:
                ## return player bet
                return passline_oddsbet
            else:
               print("Invalid Bet Amount") 
        else:
            passline_oddsbet = 0
            return passline_oddsbet
    except ValueError:
        print("Invalid Input")
## function for user to bet bet for a place to land besides the point value
def place_betting():
    ## employ error handling
    try:
        userinput = input("Would you like to place a Place Bet? (y/n)")
        if userinput == 'y':
            place_bet = int(input("What point would you like to bet on? "))
            if 3 < place_bet < 11 and place_bet != 7:
                place_betamt = int(input("How much would you like to bet?"))
                if place_betamt > 0:
                    ## return player bet amount and what they bet on
                    return place_betamt, place_bet
                else:
                   print("Invalid Bet Amount") 
            else:
               print("Invalid Bet Amount")
               return place_bet == None and place_betamt == 0
    except ValueError:
        print("Invalid Input")
come_out_roll()


