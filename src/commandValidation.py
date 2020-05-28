#!/usr/bin/env python3

'''

#               Developed by Ajay Balakumaran on 25/03/2019
#
#       >> Module for handling validation of commands which are given by user as well as file.
#       >> It will be able validate the command line and arguments and pass to the respective
#       function to fetch the required/desired output
#       
#       1) It will get the input from the user and it start validate it with the command and number
#       of arguments defined
#       2) It will get the input commands from the file which are given as the arguments

'''
import sys
sys.path.append("..") 

from source.parking import parkingClass

class validateCommands(object):
    def __init__(self):
        pass
        
    def validateCommands(self,commands,arguments):


        output = "***Invalid Command*** \n Please refer the help tab if required" 
        commandAndArguments = {"create_parking_lot": 1,
                            "park":2,
                            "leave":1,
                            "status":0,
                            "registration_numbers_for_cars_with_colour": 1,
                            "slot_numbers_for_cars_with_colour":         1,
                            "slot_number_for_registration_number":       1}
        
        numberOfArguments = (arguments.count(" ") + 1)
        if (commands == "status" and arguments == ""):
            numberOfArguments = arguments.count(" ") 

        '''
            
        #       1) Validate the commands are number of arguments are present as per the 
        #       set of rules predefined. 
        #       2) System will through error in case of any wrong commands or in mismatch 
        #       of the number of arguments which are passed
        #       3) If commands and arguments are matched it will start fetching the details
        #       and provide us

        '''


        for key, value in commandAndArguments.items():
            if (commands == key):

                if (value == numberOfArguments):
                    # Create Action
                    if (commands == "create_parking_lot"):
                        try:
                            arguments = int(arguments)
                            if (arguments > 0):
                                returnCheck = parkingInstance.createSlot(arguments)
                                if(returnCheck == 1):
                                    output = "Created a parking lot with " + str(arguments)
                                else:
                                    output ="Unable to Create Parking Lot / Parking Lot already Created"
                            elif(arguments == 0):
                                output = "Not able to create Zero Slots"
                            else:
                                output = "Error"
                                
                        except:
                            return output
                    # Add the car details and allocate the slot
                    elif (commands == "park"):
                        try:
                            slotCheck = parkingInstance.slotValidation()
                            if (slotCheck ==1):
                                returnCheck = parkingInstance.addVehicle(arguments)
                                if (returnCheck !=0 and returnCheck !="error"):
                                    output = "Allocated slot number: " + str(returnCheck)
                                else:
                                    output = "Sorry, parking lot is full"
                            elif(slotCheck == 0):
                                output = "Slots are not generated yet \nUse command create_parking_slot <slot_size> to create slots"
                            elif(slotCheck == -1):
                                output = "Unexpected Error Occured"
                        except:
                            return output

                    # Remove car details and deallocted the slot
                    elif (commands == "leave"):
                        try:
                            slotCheck = parkingInstance.slotValidation()
                            if (slotCheck ==1):
                                arguments = int(arguments)
                                returnValue = parkingInstance.removeVehicle(arguments)
                                if (returnValue == 1):
                                    output = "Slot number " + str(arguments) + " is free" 
                                else:
                                    output = "Sorry, Slot number not valid. Please check the slot number"
                            elif(slotCheck == 0):
                                output = "Slots are not generated yet \nUse command create_parking_slot <slot_size> to create slots"
                            elif(slotCheck == -1):
                                output = "Unexpected Error Occured"
                        except:
                            output = "Arguments should be and integer, " + str(arguments) + " is not and interger"
                            return output

                    # To view the status of the slots
                    elif (commands == "status"):
                        try:
                            slotCheck = parkingInstance.slotValidation()
                            if (slotCheck ==1):
                                returnValue = parkingInstance.statusFunction()
                                if (returnValue == 0):
                                    output = "No Vehicles are parked in the parking lot"
                                elif (returnValue == -1):
                                    output = "Error"
                                else:
                                    stringTest = "Slot No. Registration Number    color"
                                    for key,value in returnValue.items():
                                        stringTest = stringTest + "\n" + str(key) + '{:>24}' .format(str(value[0])) + '{:>12}'.format(str(value[1]))
                                    
                                    output = stringTest
                            elif(slotCheck == 0):
                                output = "Slots are not generated yet \nUse command create_parking_slot <slot_size> to create slots"
                            elif(slotCheck == -1):
                                output = "Unexpected Error Occured"
                        
                        except:
                            return "No Vehicles are parked in the parking lot"

                    # Find Registration number of a car with the color
                    elif (commands == "registration_numbers_for_cars_with_colour"):
                        try:
                            slotCheck = parkingInstance.slotValidation()
                            if (slotCheck ==1):
                                arguments = str(arguments)
                                if (arguments != ""):
                                    returnValue = parkingInstance.findWithColor(arguments, "registration")
                                    if (returnValue != 0):
                                        stringOutput = ','.join(str(e) for e in returnValue)
                                        output = stringOutput
                                    elif(returnValue == 0):
                                        output = "No Vehicles are parked in the parking lot"
                                    else:
                                        output = "Car Not Found"
                                else:
                                    output = "Arguments are required, Please provide colour of a car to find the registration number \neg: registration_numbers_for_cars_with_colour <COLOR>"
                            elif(slotCheck == 0):
                                output = "Slots are not generated yet \nUse command create_parking_slot <slot_size> to create slots"
                            elif(slotCheck == -1):
                                output = "Unexpected Error Occured"
                        except: 
                            return output

                    # Find the slot number for a car with color
                    elif (commands == "slot_numbers_for_cars_with_colour"):
                        try:
                            slotCheck = parkingInstance.slotValidation()
                            if (slotCheck ==1):
                                arguments = str(arguments)
                                if (arguments != ""):
                                    returnValue = parkingInstance.findWithColor(arguments,"slot")
                                    if (returnValue != 0):
                                        stringOutput = ','.join(str(e) for e in returnValue)
                                        output = stringOutput
                                    elif(returnValue == 0):
                                        output = "No Vehicles are parked in the parking lot"
                                    else:
                                        output = "Slot Not Found"
                                else:
                                    output = "Arguments are required, Please provide color of a car to find the slot \neg: slot_numbers_for_cars_with_colour <COLOR>"
                            elif(slotCheck == 0):
                                output = "Slots are not generated yet \nUse command create_parking_slot <slot_size> to create slots"
                            elif(slotCheck == -1):
                                output = "Unexpected Error Occured"
                           
                        except: 
                            return 1

                    # Find the slot number for a car with slot
                    elif (commands == "slot_number_for_registration_number"):
                        try:
                            slotCheck = parkingInstance.slotValidation()
                            if (slotCheck ==1):
                                arguments = str(arguments)
                                if (arguments != ""):
                                    returnValue = parkingInstance.findSlotNumber(arguments, "slot")
                                    if (returnValue != 0):
                                        stringOutput = ','.join(str(e) for e in returnValue)
                                        output = stringOutput
                                    elif(returnValue == 0):
                                        output = "No Vehicles are parked in the parking lot"
                                    else:
                                        output = "Slot Not Found"
                                else:
                                    output = "Arguments are required, Please provide colour of a car registration number to find the slot \neg: slot_number_for_registration_number <VEHICLE_NUMBER>"
                            elif(slotCheck == 0):
                                output = "Slots are not generated yet \nUse command create_parking_slot <slot_size> to create slots"
                            elif(slotCheck == -1):
                                output = "Unexpected Error Occured"
                            
                        except: 
                            return output

                    else:
                        return 1

                
                else:
                    return "Arguments mismatch for the " + commands +" command\n" + commands + " expects " + str(value) + " arguments"

        else:
            return output    
        
parkingInstance = parkingClass()

