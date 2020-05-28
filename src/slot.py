
#!/usr/bin/env python3
'''

#               Developed by Ajay Balakumaran on 25/03/2019
#       
#       >> This class will be used to hold the data in the respective dictionary 
#       >> This class can store the details of the slots whether it is avaliable or occupied
#       >> This class able to update the details and detele the record from the dictionary

'''

class slotClassUpdate(object):
    
    def __init__(self):
        self.slotDict = {}

    def getSlot(self):
        return self.slotDict

    def setSlot(self,slotNumber,status):
        self.slotDict.update({slotNumber:status})
        

