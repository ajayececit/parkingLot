#!/usr/bin/env python3

'''
Developed by Ajay Balakumaran on 24/03/2019
Module for handling the Parking Lot Application, It will be able update the vehicle 
details list with Registration Number and colour
    1) Add Registration number and color of a vehicle while entering
    2) Remove the vehicle details while leaving
'''

import sys
sys.path.append("..") 

from source.vehicle import vehicleClassUpdate
class vehicleClass(object):

    def __init__(self):
        pass

    # Method to add the vehicle details in the list while entering
    def addVehicleDetails(self, slot, vehicleData):
        vehicleData = vehicleData.split(" ")
        if (slot > 0):
            
            vehicleClassUpdateInstance.setVehicle(slot, vehicleData[0], vehicleData[1])
            return 1
        else:
            return 0

    # Method to remove the vehicle details from the list while leaving
    def removeVehicle(self, slotNumber):
        try:
            vehicleDict = vehicleClassUpdateInstance.getVehicle()
            del vehicleDict[slotNumber]
            return 1
        except:
            return "error"
    
    def status(self):
        try:
            vehicleDetails = vehicleClassUpdateInstance.getVehicle()
            if (len(vehicleDetails) > 0):
                return vehicleDetails
            else:
                return 0 
        except:
            return -1

    def findCarDetails(self, vehicleColor, detailsNeeded):
        vehichleDict = vehicleClassUpdateInstance.getVehicle()
        detailsList = []
        if (detailsNeeded == "slot"):
            for key, value in vehichleDict.items():
                if (value[1] == vehicleColor):
                    detailsList.append(key)                             # list which will return the car's
                                                                        # slot number which is allocated in the time of parking 
                                                                        # with the reference of vehicle colour
        elif(detailsNeeded == "registration"):
            for key, value in vehichleDict.items():
                if (value[1] == vehicleColor):
                    detailsList.append(value[0])                        # list which will return the car's
                                                                        # registration number
                                                                        # with the reference of vehicle colour
                
        else:
            detailsList.append("improper field")
        
        return detailsList
    
    def findSlotDetails(self, vehicleNumber, detailsNeeded):
        vehichleDict = vehicleClassUpdateInstance.getVehicle()
        detailsList = []
        if (detailsNeeded == "slot"):
            for key, value in vehichleDict.items():
                if (value[0] == vehicleNumber):
                    detailsList.append(key)                             # list which will return the car's
                                                                        # slot number which is allocated in parking 
                                                                        # with the reference of vehicle number
        elif(detailsNeeded == "color"):
            for key, value in vehichleDict.items():
                if (value[0] == vehicleNumber):
                    detailsList.append(value[1])                        # list which will return the car's
                                                                        # colour with the reference of vehicle number
                
        else:
            detailsList.append("improper field")

        return detailsList
        
vehicleClassUpdateInstance = vehicleClassUpdate()