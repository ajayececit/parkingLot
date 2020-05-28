#!/usr/bin/env python3

'''

#               Developed by Ajay Balakumaran on 24/03/2019
#       >> Module for handling the Parking Lot Application, It manages the complete 
#       logic of parking lot
#       >> This module is consider as the admin class for the application which handles following
#           1) Create parking lot
#           2) Add vehicles
#           3) Remove vehicles
#           4) Find cars & slots
#           5) Status Report

'''

import sys
sys.path.append("..") 
from source.slotActions import slotClass
from source.vehicleAction import vehicleClass


class parkingClass(object):

    def __init__(self):
        pass
        
  
    # Method to Create the Slots which are required for the user

    def createSlot(self, count):
        try:
            if (count >0):
                slotClassInstance.addSlot(count)
                return 1
            else:
                return 0
        except:
            return 0
    
    

    # Method to Add Vehicle details into a list in the time of entering

    def addVehicle(self, vehicleDetails):
        try:
            availableSlot = slotClassInstance.findFreeSlot()
            if (availableSlot > 0):
                returnValue = vehicleClassInstance.addVehicleDetails(availableSlot, vehicleDetails)
                slotClassInstance.updateSlot(availableSlot,"Occupied")
                if (returnValue == 1):
                    return availableSlot 
                else:
                    return 0
            else:
                return 0
        except:
            return "error"

    # Method to Remove vehicle details from the list in the time of leaving

    def removeVehicle(self,slotNumber):
        if (slotNumber > 0):
            checkFlag = slotClassInstance.checkStatus(slotNumber)
            if (checkFlag != 0):
                vehicleClassInstance.removeVehicle(slotNumber)
                slotClassInstance.updateSlot(slotNumber,"leave")
                return 1
            else:
                return 0
        else:
            return "error"

    # Method to find the car details with respect to color of car
    # or registration number which are allocated in lot
    
    def findWithColor(self, color, details):
        try:
            details = vehicleClassInstance.findCarDetails(color,details)
            if (len(details)>0):
                return details
            else:
                return 0
        except:
            return "error"

    # Method to find the slot allocated to car with respect to registration number or car color
    # of car which are allocated in lot

    def findSlotNumber(self,regNumber, details):
        try:
            details = vehicleClassInstance.findSlotDetails(regNumber,details)
            if (len(details)>0):
                return details
            else:
                return 0
        except:
            return "error"

    # To provide the current status report of the parking lot
    
    def statusFunction(self):
        try:
            returnValue = vehicleClassInstance.status()
            return returnValue
        except:
            return -1

    def slotValidation(self):
        try:
            return slotClassInstance.slotCheck()
            
        except:
            return -1
    

slotClassInstance = slotClass()
vehicleClassInstance = vehicleClass()