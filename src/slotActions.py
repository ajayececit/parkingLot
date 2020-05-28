#!/usr/bin/env python3

'''

#               Developed by Ajay Balakumaran on 24/03/2019
#       >> Module for handling the Parking Lot Application, It will be able update the slot 
#       details and provide the free slots available
#           1) Create parking slots
#           2) Find available parking slots
#           3) Add or remove the slot details

'''
import sys
sys.path.append("..") 
from source.slot import slotClassUpdate

class slotClass(object):

    def __init__(self):
        pass

    def addSlot(self,count):
        try:
            count = int(count)
            if (count >0):
                for i in range(1,count+1):
                    slotClassUpdateInstance.setSlot(i,"Available")
                return 1
            else:
                return 0
        except:
            return -1

    def slotCheck(self):
        try:
            slotDetail = slotClassUpdateInstance.getSlot()
            if (len(slotDetail) > 0):
                return 1
            else:
                return 0
        except:
            return -1
    
    def slotAvailablity(self,slotNumber):
        if (slotNumber > 0):
            slotDict = slotClassUpdateInstance.getSlot()
            for key,value in slotDict.items():
                keyValue = int(key)
                
                if (keyValue is slotNumber and value == "Available"):
                    returnValue = 1
                    return returnValue
                
        else:
            return "negative"

    def checkStatus(self, slotNumber):
        if(slotNumber > 0):
            slotDict = slotClassUpdateInstance.getSlot()
            returnValue = 0
            for key,value in slotDict.items():
                keyValue = int(key)
                if (keyValue is slotNumber and value == "Occupied"):
                    returnValue = 1
                    return returnValue
            else:
                return returnValue
        else:
            return "negative"

    # Method to find the Free/Available slot in the parking Area
    def findFreeSlot(self):
        slotDict = slotClassUpdateInstance.getSlot()
        if (len(slotDict)> 0):
            for key,value in slotDict.items():
                if (value == "Available"):
                    return key
            else:
                key = 0
            return key
               

    # Method to Add or Remove the slot details
    def updateSlot(self, slotNumber, status):
        slotNumber = int(slotNumber)
        if (slotNumber > 0):
            slotDict = slotClassUpdateInstance.getSlot()
            if (slotNumber <= len(slotDict) and slotNumber >=  1):
                if(status == "Occupied"):
                    slotDict.update({slotNumber:"Occupied"})
                    return "updated"
                elif (status == "leave"):
                    slotDict.update({slotNumber:"Available"})
                    return "updated"
                else:
                    return "err"
            else:
                return "err"
        else:
            return "negative"
        
slotClassUpdateInstance = slotClassUpdate()
