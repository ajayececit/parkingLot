#!/usr/bin/env python3

'''

#               Developed by Ajay Balakumaran on 25/03/2019
#
#       >> This module will be the main program of the whole application and it will start working with  
#       respect to the inputs provided
#       >> This module will work as a interactive window with the user if the program is run without 
#       an arguments.
#       >> This module will read the commands from the file which are provided by the user while 
#       running the program with the argument as a file path      
#       >>The input commands are passed to the commandValidation module to get the vaildation done

'''

import sys
import os
sys.path.append("..")
from source.commandValidation import validateCommands
class parkingLot(object):
    def __init__(self):
        pass
    
    def parkingFunc(self):
        
        if (len(sys.argv) == 1):
            print("Welcome to Parking Lot Application")
            print("Pass me help or ? to know about the command lines")
            
            while True:
                command = ""
                commandArgument = ""
                inputString = input("$")
                if (inputString.lower() == "exit" or inputString.lower() == "exit()"):
                    break
                elif (inputString.lower() == "help" or inputString.lower() == "?"):
                    print ("=============================================================================================================================")
                    print ("\t\t\t\t\tHelp for Parking Lot Application\n")
                    print ("This application to help the Parking Lot management")
                    print ("Below are the commands and it's functions")
                    print ("\n>> create_parking_lot <number_of_lots_required> -> Used to create the parking lot for the user with the reqired number of slots")
                    print ("\n>> park <vehicle_number> <vehicle_color> -> Used to allocate the vehicles in the free slots")
                    print ("\n>> leave <slot_number> -> Used to deallocate the space which is provided to the vehicle while entering")
                    print ("\n>> status -> Used to get the report of the slots which are allocated")
                    print ("\n>> registration_numbers_for_cars_with_colour <vehicel_color> -> Used to find the registration number with the vehicle color")
                    print ("\n>> slot_numbers_for_cars_with_colour <vehicel_color> -> Used to find the slots allocated to car with the car color")
                    print ("\n>> slot_number_for_registration_number <registration_number> -> Used to find the slots allocated to the car with vehicel number")
                    print ("\n>> exit or exit()  -> Used to exit the application\n")
                    print ("=============================================================================================================================")
                    
                elif (inputString != ""):
                    commandGiven = inputString.split(" ")
                    command = commandGiven[0]
                    commandArgument = inputString[len(command)+1:len(inputString)]
                    commandOutput = validateCommands().validateCommands(command,commandArgument)
                    print (commandOutput)
            return 1
        if (len(sys.argv) == 2):
            if (sys.argv[1].find(".txt") > -1):
                thisPath = os.path.dirname(os.getcwd())
                filePath = os.path.join(thisPath, sys.argv[1])
                if  ((os.path.exists(filePath)) is True):
                    with open(filePath, "r") as f:
                        text = f.readlines()
                    for inputString in text:
                        inputString = inputString.replace("\n", "")
                        commandGiven = inputString.split(" ")
                        command = commandGiven[0]
                        commandArgument = inputString[len(command)+1:len(inputString)]
                        commandOutput = validateCommands().validateCommands(command,commandArgument)
                        print (commandOutput)
                else:
                    print ("\n*********************************************\n"
                           "Given file name not found in the given folder.\n" 
                           "Kindly re-check the file name and the path"
                           "\n*********************************************\n")
                
            else:
                print ("\n*********************************************\n"
                      "Sorry, Kindly check for the proper input file"
                      "\n*********************************************\n")

            return 2
        if(len(sys.argv)>2):
            print("\n****************************************************\n"
                 "Sorry, Kindly provide the proper input \n"
                 "The program accepts eith zero or one argument"
                 "\nNo Argument -- Interactive mode \nOne Argument (filePath Expected) -- File read mode\n"
                 "****************************************************\n")

if (__name__ == "__main__"):
    parkingLot().parkingFunc()
