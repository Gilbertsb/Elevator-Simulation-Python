from elevetor_class import *
from random import randrange
import time

def move_elevetor():  #Function to move elevator in different ways

    Decoration=Elevetor_class() #calling function from class
    elevtorfloor = randrange(1, 8) #Setting rendom values for elevator
    print("Elevetor is at Floor:", elevtorfloor)# showing where elevetor is
    #prompting user to show where he is
    userfloor = eval(input('Enter Floor number(1-8) of where you are now: '))  # 10
    if userfloor>8 or userfloor==0:
        print('SELECTED WRONG FLOOR NUMBER TRY AGAIN') #validation
        return

    # going up of elevetor to find user
    if elevtorfloor < userfloor:
        for y in range(elevtorfloor + 1, userfloor + 1): #loop to move elevator
            print('Elevetor going up:', y)
            time.sleep(2)                   #dalaying loop in time for 2secs
            elevtorfloor = y
        print("DOORS OPEN!")              #showing that doors are open
        Enter = input("Enter letter E to show that you have Entered:")#Entring into elevator
        if Enter.casefold()!='e':
            print('SELECTED WRONG LETTER PLEASE TRY AGAIN!!') #Validation
            return
        if Enter.casefold() == 'E'.casefold():
            print("DOORS CLOSE!")              #showing that doors are closed
        going = eval(input("Please Enter Floor number you are going to: "))
        if going > 8 or going == 0:
            print('SELECTED WRONG FLOOR NUMBER TRY AGAIN')    #Valiadation
            return

        # going up of elevetor to destination of user
        if elevtorfloor < going:
            for y in range(elevtorfloor + 1, going + 1):     #moving elevator
                print('Elevetor going up:', y)
                time.sleep(2)
            print("YOU HAVE REACHED TO DESTINATION!")
            print("DOORS OPEN!")
        # going down of elevetor to destination of user
        elif elevtorfloor > going:
            y = elevtorfloor
            while y >= going:                              #moving elevetor down words
                print('Elevetor going down:', y)
                time.sleep(2)                          #Delaying loop for 2secs for nice looks
                y -= 1
            print("YOU HAVE REACHED TO DESTINATION!") #showing to user he/she has reached
            print("DOORS OPEN!")
        else:
            print("YOU HAVE REACHED TO DESTINATION!")
            print("DOORS OPEN!")
    # going down of elevetor to find user
    elif elevtorfloor > userfloor:
        y = elevtorfloor
        while y >= userfloor:
            print('Elevetor going down:', y)       #moving elevetor down
            time.sleep(2)
            y -= 1
            elevtorfloor = y
        print("DOORS OPEN!")
        Enter = input("Enter letter E to show that you have Entered: ")
        if Enter.casefold()!='e':
            print('SELECTED WRONG LETTER PLEASE TRY AGAIN!!')    #validation
            return
        if Enter.casefold() == 'E'.casefold():
            print("DOORS CLOSE!")
        going = eval(input("Please Enter Floor number you are going to: "))
        if going > 8 or going== 0:
            print('SELECTED WRONG FLOOR NUMBER TRY AGAIN')     #validation
            return
        # going up of elevetor to destination of user
        if elevtorfloor < going:
            for y in range(elevtorfloor + 1, going + 1):   #moving elevato up ward
                print('Elevetor going up:', y)
                time.sleep(2)
            print("YOU HAVE REACHED TO DESTINATION!")    #showing user that he/sh reached
            print("DOORS OPEN!")
        # going down of elevetor to destination of user
        elif elevtorfloor > going:
            y = elevtorfloor
            while y >= going:
                print('Elevetor going down:', y)     #moving elevator down
                time.sleep(2)
                y -= 1
            print("YOU HAVE REACHED TO DESTINATION!")     #showing user that he/sh reached
            print("DOORS OPEN!")
        else:
            print("YOU HAVE REACHED TO DESTINATION!")     #showing user that he/sh reached
            print("DOORS OPEN!")

    elif elevtorfloor == userfloor:
        print("DOORS OPEN!")
        Enter = input("Enter letter E to show that you have Entered ")
        if Enter.casefold()!='e':
            print('SELECTED WRONG LETTER PLEASE TRY AGAIN!!')       #Validation
            return
        if Enter.casefold() == 'E'.casefold():
            print("DOORS CLOSE!")
        going = eval(input("Please Enter Floor number you are going to: "))
        if going > 8 or going == 0:
            print('SELECTED WRONG FLOOR NUMBER TRY AGAIN')   #Validation
            return
        # going up of elevetor to destination of user
        if elevtorfloor < going:
            for y in range(elevtorfloor + 1, going + 1):
                print('Elevetor going up:', y)
                time.sleep(2)
            print("YOU HAVE REACHED TO DESTINATION!")        #showing user that he/sh reached
            print("DOORS OPEN!")
        # going down of elevetor to destination of user
        elif elevtorfloor > going:
            y = elevtorfloor
            while y >= going:
                print('Elevetor going down:', y)          #Moving elevator downwoard
                time.sleep(2)
                y -= 1
            print("YOU HAVE REACHED TO DESTINATION!")    #showing user that he/sh reached
            print("DOORS OPEN!")
        else:
            print("YOU HAVE REACHED TO DESTINATION!")
            print("DOORS OPEN!")



def exit_this():
    exit("THANK YOU FOR USING THIS SOFTWARE SEE YOUUU!!!")    #Function to close program in case wants

