#imports random and time to be used and assigns rancharge and ranmoney as a global variable so it can be called whenever
import random

rancharge = random.randint(5,16)
ranmoney = random.randint(5,15)
import time


#global variable for user's name
name1 = input("What is your name player 1?")

#introduction function which states the setting takes place in NYC
def introduction():
    print("The year is 2001. Being new to Manhattan, you have decided to explore the city and the surrounding neighborhoods. One evening you pick a direction and start walking, eager to see new sights.\n")
    print("As you wander, you find a creepy old house on a quiet street in SoHo. Just as you are about to walk past, the clouds that had been gathering all day suddenly start raining. You have no choice but to seek shelter on the porch of the old house.\n")
    print('As you are standing there wondering what to do, the front door creaks open behind you. "No way I\'m going in there," you think. "I\'ve watched enough episodes of Unsolved Mysteries to know how THAT goes." You settle in to wait out the rain... until you notice most of the local rat population is also sharing the porch with you. You decide to step inside the house after all, and shut the door quickly behind you. Looking around inside the house, you see a dimly lit hallway full of doors.\n')
    print('"I\'d better get out of here fast," you think. But what can you do? Your phone battery is down to 5% and you only have one dollar, so you can’t risk making a call. If you could charge your phone battery (at least you remembered to bring a charging cable) you could call your friend to come pick you up. If you could find some money, you could try one of those yellow cabs for the first time and get a ride home. You square your shoulders and set off in search of an electrical outlet or a couch you can scrounge in for change.\n')
    

#sample room, kept the name/theme, delays(sleep) message for 3 seconds then returns the phone charge + 5 back to the main function
def sample_room(phone_charge):
    time.sleep(3)
    print("An outlet! You quickly plug in your phone, but the wiring in the house is faulty and soon shorts out.\n")
    return(phone_charge + 5)

#automatic charge no matter circumstances which charges it 3 times but not until it reaches a certain percent so the idea of the story is carried out
def charge_one(phone_charge):
    i = 0
    while i<3 :
        time.sleep(1)
        print("Charging...", "phase", i)
        i = i+1
        phone_charge = phone_charge + rancharge 
    return phone_charge
    
#ending if charge is greater than or = to 40 instead of 30 because it's less likely so the user can experience the other options
def ending1(phone_charge):
    if phone_charge >= 40:
     print("Congratulations! Your phone has achieved a suffient percent to escape")
     print("You escape to call your best friend ")
    return phone_charge

#validates if the option user puts is valid 
def checked1(lower_limit, upper_limit):
     i=0
     while i < 1:
        
        if lower_limit not in range(lower_limit, upper_limit):
            i=i+1
            print("That is not a valid option. Please enter option 1 or 2")
        else:
            i= i +1
            print("Let's see if you chose the right option...")
     return(lower_limit, upper_limit)

#alternative to user not getting 40 percent charge which uses their name and tells them 
def ending1_1(phone_charge):
    time.sleep(2)
    print("Your phone only got to " + str(phone_charge)  + "% " + name1)
    print("You didn't get the charge needed to escape, ",name1 , " , but you still have time to escape")
    return phone_charge

#tells them they found a charger and updates phone variable 
def room1(phone_charge):
    rancharge = random.randint(5,11)
    print("You have found a sufficient charger")
    phone_charge = phone_charge + rancharge
    return phone_charge


def room2(phone_charge):
    time.sleep(1)
    print("Uh oh, you got scared by a stray cat and dropped your phone making it lose charge")
    phone_charge = phone_charge - rancharge
    return phone_charge
        
def room3(money_balance):
    print("Cha ching, you have found some money under a hollow tile ")
    money_balance = money_balance + ranmoney
    return money_balance


def room4(money_balance):
    print("Someone else was out for your money and you got robbed! ")
    money_balance = money_balance - 5
    return money_balance

def room5(phone_charge, money_balance):
    print("Jackpot! You find a random amount of money in the cushion of a chair and an outlet ")
    phone_charge = phone_charge + rancharge
    money_balance = money_balance + ranmoney
    return phone_charge ,money_balance

def room6(money_balance): 
    print("You keep walking and you're able to look around a room that has nothing but a piano pulling the strings for itself, playing Ludovico Einaudi.")
    time.sleep(2)
    print("You lift the lid to find 5 dollars jumping up and down from the strings")
    print("Even though , you're creeped out by the piano playing itself, you snatch the 5 dollars and run")
    return money_balance + 5


def room7(money_balance):
    print("You enter and see that it was just a stereo playing jazz music. You scruff the stereo but don't find any money")
    return money_balance

def ending2():
    print("Your spirit remainsYou're able to escape through the kitchen and call for help!But before you go you help yourself to some matcha cookies and brown sugar boba")
    print("You take out your phone to call your friend")
    friend = input("Who would you like to call?")
    i = 0 
    while i<2:
     i = i + 1
     time.sleep(2)
     print("Calling...")
    print("Hey",friend ," I'm at 558 Broadway Ave and got stranded, can you come pick me up please?")
    print(friend,":", "Of course, " ,name1, " I'm on my way. You've got to tell me about this one.")

def ending2_2():
    print("Unfortunately your survival skills weren't enough and your spirit remains as a ghost")
    print("However, the other ghosts take you in as a rookie spirit, teaching you how to make matcha cookies and brown bubble tea from scratch to reward the next survivors")

def randomevent():
    time.sleep(3)
    randomooccurence = int(input("You turn and come across a holograph projecting from a small box.Pick a number from 1-20"))
    checked1(1,21)
    if randomooccurence == 1:
        print("Woah you got scared by a gargoyle and need a second to calm down")
        time.sleep(1)
    elif randomooccurence == 10:
        print("The box opens up to a glass of sweet tea and a fresh bacon egg and cheese laid out in front of you. Rehydrate , eat, and")
        print("continue your journey")
    elif randomooccurence == 20:
        print("You find a shortcut...through a hidden wine cellar")
    else:
        print("You get nothing unfortunately.") 
    return randomooccurence
    

def main():
    introduction()
    phone = 5
    money = 5
    print("You enter the living room.\n")
    phone = sample_room(phone)
    print("Your phone is now "+ str(phone)+ "% charged\n" )
    phone = charge_one(phone)
    print("Your phone is now " + str(phone) + "% charged\n and you walk until you come across something strange")
    print()
    randomevent()

    if phone >= 40:
        print()
        time.sleep(3)
        ending1(phone)
    else:
        ending1_1(phone)
        option = int(input("You walk further ahead and come across two rooms. (1) has a birch door and (2) dark oat "))
        print()
        checked1(option, 3)
        if option == 1:
            phone = room1(phone)
            print("Your phone is now charged at", phone, "% with your money balance still being 5 dollars")
        elif option == 2:
            phone = room2(phone)
            print("Your phone is now charged at", phone, "% with your money balance still being 5 dollars")
        print()
        optiontwo = int(input("You come across three rooms,one: (1) that is labeled with a triangle , (2) that is labeled with a square, (3)that is labled with an inscribed triangle . 1 , 2, or 3?"))
        checked1(optiontwo, 4)
        if optiontwo == 1:
            money = room3(money)
            print("You now have", money, "%")
        elif optiontwo == 2:
            money = room4(money)
            print("Your balance is now ",money, "$")
        elif optiontwo == 3:

            room5(phone, money) 
            print("Your phone is now charged at ",phone + rancharge, "% and your money balance is now\n ", money + ranmoney, "$")
        
        optionthree = int(input("You hear a piano playing in room (1), and an alto saxophone playing in room (2) "))
        checked1(optionthree, 3)
        if optionthree == 1:
            room6(money)
            print("You now have ", money, "$" )
        elif  optionthree == 2:
            room7(money)
            print("Your balance remains at", money, "$")
        
        print("You come to a halt. You hear something calling your name and you follow.")
            
        print("It leads you to a hidden wine cellar which drops you to the level below! You feel a thump. ")

        print("You are now floating and see your body standing right where you fell")

        name2 = input("What is your name Player 2?")
        money2 = 5
        phone2 = 5
        print("Welcome back,", name2, "The Ghost")
        option = int(input("You walk further ahead and come across two rooms. (1) has a birch door and (2) dark oat "))
        print()
        checked1(option, 3)
        if option == 1:
            phone = room1(phone2)
            print("Your phone is now charged at", phone, "% with your money balance still being 5 dollars")
        elif option == 2:
            phone = room2(phone2)
            print("Your phone is now charged at", phone, "% with your money balance still being 5 dollars")
        print()
        optiontwo = int(input("You come across three rooms,one: (1) that is labeled with a triangle , (2) that is labeled with a square, (3)that is labled with an inscribed triangle . 1 , 2, or 3?"))
        checked1(optiontwo, 4)
        if optiontwo == 1:
            money2 = room3(money2)
            print("You now have", money2, "%")
        elif optiontwo == 2:
            money2 = room4(money2)
            print("Your balance is now ",money2, "$")
        elif optiontwo == 3:

            room5(phone2, money2) 

        print("Your phone is now charged at ",phone2 + rancharge, "% and your money balance is now\n ", money2 + ranmoney, "$")
        
        optionthree = int(input("You hear a piano playing in room (1), and an alto saxophone playing in room (2) "))
        
        if optionthree == 1:
            room6(money2)
            print("You now have ", money2, "$" )
        elif  optionthree == 2:
            room7(money2)
            print("Your balance remains at", money2, "$")

    if phone >= 40 or money>= 20 or money2 >= 20 or phone2 >= 40:
            ending2()
    else:
            ending2_2()
    again = input("Would you like to play again?Y or N")
    if again == "Y":
        main()
    elif again == "N":
        print("Thank you for playing!")
    




main()
