
#!/usr/bin/env python3

'''

#               Developed by Ajay Balakumaran on 25/03/2019
#       
#       >> This class will be used to hold the data in the respective dictionary 
#       >> This class can store the details of the vehicles
#               1) Number
#               2) Colour
#       >> This class able to update the details and detele the record from the dictionary

'''

class vehicleClassUpdate(object):
    
    def __init__(self):
        self.vehicleDict = {}

    def getVehicle(self):
        return self.vehicleDict

    def setVehicle(self, slotNumber, vNumber, vColour):
        self.vehicleDict.update({slotNumber: [vNumber,vColour]})
        

