#!/usr/bin/env python3
import unittest

from commandValidation import validateCommands
#from parking_lot import parkingLot
from parking import parkingClass
from slotActions import slotClass
from vehicleAction import vehicleClass
from slot import slotClassUpdate
from vehicle import vehicleClassUpdate

class parkClassTest(unittest.TestCase):
    
    #----------------------------------------------------------------
    #           Unit test case for slotActions.py module
    #   >> Tested addSlot function by passing Non Zero Integer,
    #   Zero, Negative and String 
    #   >> Tested slotCheck module to find if slots are present
    #   >> Tested freeSlots module to get the Available slots 
    #   >> Tested updateSlots module by passing the slots number and
    #   it's status to change the availablity. The module has been 
    #   tested by passing Negative number and nuumber greater than 
    #   slots available.
    #   >> Tested checkStatus with passing positive and negtive number
    #   to see the status whether selected slot is occupied

    # Create Slot Check with proper non zero  
    def test_createSlotCheck(self):
        self.assertEqual(slotActionsInstance.addSlot(1),1)
        self.assertEqual(slotActionsInstance.addSlot(2),1)

    # Create Slot Check with  zero  
    def test_createSlotCheckNegative(self):
        self.assertEqual(slotActionsInstance.addSlot(0),0)

     # Create Slot Check with  zero  
    def test_createSlotCheckZero(self):
        self.assertEqual(slotActionsInstance.addSlot(-1),0)
        

    # Create Slot Check with a string
    def test_createSlotCheckString(self):
        self.assertEqual(slotActionsInstance.addSlot("a"),-1)
        self.assertNotEqual(slotActionsInstance.addSlot("a"),1)

    def test_slot(self):
        self.assertEqual(slotActionsInstance.slotCheck(),1)

    #check for the free slot
    def test_freeSlot(self):
        self.assertEqual(slotActionsInstance.findFreeSlot(),1)

    def test_updateSlot(self):
        self.assertEqual(slotActionsInstance.updateSlot(1,"Occupied"),"updated")
    
    # check whether any slots are occupied
    def test_CheckStatus(self):
        self.assertEqual(slotActionsInstance.checkStatus(1),0)
        self.assertEqual(slotActionsInstance.checkStatus(-1),"negative")

    def test_updateSlotError(self):
        self.assertEqual(slotActionsInstance.updateSlot(10,"Occupied"),"err")
        self.assertNotEqual(slotActionsInstance.updateSlot(10,"Occupied"),"updated")
        self.assertEqual(slotActionsInstance.updateSlot(-1,"Occupied"),"negative")

    #----------------------------------------------------------------
    #           Unit test case for vehicleAction.py module
    #   >> Tested addVehicleDetails function by passing Non Zero Integer,
    #   Zero, Negative and String and check the slots available in the 
    #   parking lot
    #   >> Tested remove module to deallocate the vehicel once it left lot
    #   >> Tested viewSlot modules and compared the data with the test cases
    #   >> Tested findCarDetails module by passing the color and the data 
    #   needed to find the car. We can find the car details with registration 
    #   number or the slot the car is parked with the car color
    #   >> Tested findSlotDetails module by passing the registration and the data 
    #   needed to find the car. We can find the car details with slot 
    #   number or the color if the car is parked with the car color
    
    # Add Vehicle
    def test_addVehicle(self):
        slotActionsInstance.addSlot(3)
        freeSlot = slotActionsInstance.findFreeSlot()
        self.assertEqual(vehicleActionInstance.addVehicleDetails(freeSlot,"KA-53-Q-2961 White"),1)
        self.assertEqual(slotActionsInstance.updateSlot(freeSlot,"Occupied"),"updated")
        self.assertNotEqual(vehicleActionInstance.addVehicleDetails(-1,"KA-53-Q-2961 White"),1)
        freeSlot = slotActionsInstance.findFreeSlot()
        slotAvailable = slotActionsInstance.slotAvailablity(freeSlot)
        if (slotAvailable == 1):
            self.assertEqual(vehicleActionInstance.addVehicleDetails(freeSlot,"KA-53-Q-291 White"),1)
        else:
            self.assertNotEqual(vehicleActionInstance.addVehicleDetails(freeSlot,"KA-53-Q-291 White"),1)
        
    # Remove Vehicle
    def test_removeVehicle(self):
        self.assertEqual(vehicleActionInstance.removeVehicle(1),1)
        self.assertNotEqual(vehicleActionInstance.removeVehicle(1),1)
        self.assertEqual(vehicleActionInstance.removeVehicle(-1),"error")

    # view Status
    def test_viewStatus(self):
        statusReport = vehicleActionInstance.status()
        self.assertEqual(vehicleActionInstance.status(),statusReport)

    # find slot with color with wrong values
    def test_findCarDetails(self):
        self.assertEqual(len(vehicleActionInstance.findCarDetails("White" , "slot")),2)
        self.assertEqual((vehicleActionInstance.findCarDetails("White" , "slot")),[1, 2])
        self.assertNotEqual(len(vehicleActionInstance.findCarDetails(" White" , "slot")),2)
        self.assertNotEqual(len(vehicleActionInstance.findCarDetails(" tested " , "slot")),2)

    def test_findCarDetails1(self):
        vehicle = vehicleActionInstance.findCarDetails("White" , "registration")
        self.assertEqual(len(vehicleActionInstance.findCarDetails("White" , "registration")),2)
        self.assertEqual((vehicleActionInstance.findCarDetails("White" , "registration")),vehicle)
        self.assertNotEqual(len(vehicleActionInstance.findCarDetails(" White" , "slot")),2)
        self.assertNotEqual(len(vehicleActionInstance.findCarDetails(" White" , "slotest")),0)
        
    def test_findSlotDetails1(self):
        vehicle = vehicleActionInstance.findSlotDetails("KA-53-Q-291", "slot")
        self.assertEqual(len(vehicleActionInstance.findSlotDetails("KA-53-Q-291" , "slot")),1)
        self.assertEqual((vehicleActionInstance.findSlotDetails("KA-53-Q-291" , "slot")),vehicle)
        self.assertNotEqual(len(vehicleActionInstance.findSlotDetails(" White" , "slot")),"improper field")
        self.assertNotEqual(len(vehicleActionInstance.findSlotDetails(" White" , "slotest")),0)

    #----------------------------------------------------------------
    #           Unit test case for parking.py module
    #   >> This module is consider as the admin module which will handle
    #   both the Slot and Vehicle class.
    #   >> Tested createSlot function by passing Non Zero Integer,
    #   Zero, Negative and String and check the slots available in the 
    #   parking lot
    #   >> Tested addVehicle function and update the same with the slot 
    #   and vehicle class
    #   >> Tested remove module to deallocate the vehicel once it left lot
    #   and update the same with the slot and vehicle class 
    #   >> Tested slotValidation wheher to check whether it is a proper slot
    #   >> Tested viewSlot modules and compared the data with the test cases
    #   >> Tested findCarDetails module by passing the color and the data 
    #   needed to find the car. We can find the car details with registration 
    #   number or the slot the car is parked with the car color
    #   >> Tested findSlotDetails module by passing the registration and the data 
    #   needed to find the car. We can find the car details with slot 
    #   number or the color if the car is parked with the car color

    def test_addSlot(self):
        check = parkingInstance.createSlot("a")
        if (check == 1):
            self.assertEqual(parkingInstance.createSlot("a"), 1)
        else:
            self.assertEqual(parkingInstance.createSlot("a"), 0)
    
    def test_failedAddSlot(self):
        self.assertEqual(parkingInstance.createSlot(-1), 0)
        self.assertEqual(parkingInstance.createSlot(1), 1)
        self.assertEqual(parkingInstance.createSlot(0), 0)
        
    def test_statusFun(self):
        self.assertEqual(len(parkingInstance.statusFunction()), 1)
        self.assertIsNot(parkingInstance.statusFunction(),list)

    def test_slotValidation(self):
        self.assertEqual(parkingInstance.slotValidation(),1)
        self.assertNotEqual(parkingInstance.slotValidation(),0)

        
    # Remove Vehicle
    def test_removeVehicle1(self):
        self.assertEqual(parkingInstance.removeVehicle(1),1)
        self.assertNotEqual(parkingInstance.removeVehicle(1),1)
        self.assertEqual(parkingInstance.removeVehicle(-1),"error")

    #----------------------------------------------------------------
    #           Unit test case for slot.py module
    #   >> This module is for handling the slot details to set and get
    #   the parking lot
    #   >> Tested getSlot and setSlot by passing the slotdetails

    def test_getSlot(self):
        self.assertEqual(len(slotClassUpdateInstance.getSlot()),0)

    def test_setSlot(self):
        self.assertEqual(slotClassUpdateInstance.setSlot(1,"Occupied"),None)
        self.assertEqual(slotClassUpdateInstance.setSlot(2,"Occupied"),None)
        self.assertEqual(slotClassUpdateInstance.setSlot(3,"Occupied"),None)
        self.assertEqual(len(slotClassUpdateInstance.getSlot()),3)

    #----------------------------------------------------------------
    #           Unit test case for vehicle.py module
    #   >> This module is for handling the slot details to set and get
    #   the parking lot
    #   >> Tested getSlot and setSlot by passing the slotdetails
    #   >> Additionally to this we can able to remove the vehicle
    #   details from the lost

    
    def test_setVehicle(self):
        self.assertEqual(vehicleClassUpdateInstance.setVehicle(1, "KA-53-Q-2961", "Black"),None)
        self.assertEqual(vehicleClassUpdateInstance.setVehicle(2,"TN-72-AJ-1992", "Black"),None)
        self.assertEqual(vehicleClassUpdateInstance.setVehicle(3,"Test", "Test"),None)
        self.assertEqual(len(vehicleClassUpdateInstance.getVehicle()),3)

    def test_getVehicle(self):
        self.assertEqual(len(vehicleClassUpdateInstance.getVehicle()),0)

    def test_removeVehicle2(self):
        self.assertEqual((vehicleActionInstance.removeVehicle(4)),"error")
        self.assertEqual((vehicleActionInstance.removeVehicle(-1)),"error")

    #----------------------------------------------------------------
    #           Unit test case for commandValidation.py module
    #   >> This module is for handles the over all validation and passing
    #   the commands to fetch the respective output
    #   >> This module would help us to validate the commands and arguments
    #   which are passing by user to interactive window or using file method

    # Without failure
    def test_commandValidationCreate(self):
        command = "create_parking_lot"
        argument = "5"
        expectedOutput = "Created a parking lot with 5"
        self.assertEqual(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    # With passing more argument
    def test_commandValidationCreateError(self):
        command = "create_parking_lot"
        argument = "-1 0"
        expectedOutput = "Arguments mismatch for the"
        self.assertRegexpMatches(validateCommandsInstance.validateCommands(command,argument),expectedOutput)
        
    def test_commandValidationCreateErrorZero(self):

        command = "create_parking_lot"
        argument = "0"
        expectedOutput = "Not able to create Zero Slots"
        self.assertRegexpMatches(validateCommandsInstance.validateCommands(command,argument),expectedOutput)
        
    def test_commandValidationCreateMistake(self):
        command = "create_parking_lots_test"
        argument = "5"
        expectedOutput = "***Invalid Command*** \n Please refer the help tab if required"
        self.assertEqual(validateCommandsInstance.validateCommands(command,argument),expectedOutput)
    
    # test Status Report
    def test_statusCheck(self):
        command = "status"
        argument = ""
        self.assertRegexpMatches(validateCommandsInstance.validateCommands(command,argument),"Slot No.")
        
    def test_statusCheckError(self):
        command = "status"
        argument = "test"
        expectedOutput = "Arguments mismatch for the status command\nstatus expects 0 arguments"
        self.assertEqual(validateCommandsInstance.validateCommands(command,argument),expectedOutput)
      
    def test_statusCheckError1(self):
        command = "     statuss"
        argument = ""
        expectedOutput = "***Invalid Command*** \n Please refer the help tab if required"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    #test park function
    def test_parkFunc(self):
        command = "park"
        argument = "KA-03-Q-2961 White Test" 
        expectedOutput = "Arguments mismatch for the park command\npark expects 2 arguments"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    
    def test_parkFunc1(self):
        command = "park"
        argument = "KA-03-Q-2961 White" 
        expectedOutput = "Allocated slot number: 1"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    def test_leaveError(self):
        command = "leave"
        argument = "1" 
        expectedOutput = "Sorry, Slot number not valid. Please check the slot number"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    def test_leaveError1(self):
        command = "     leave"
        argument = ""
        expectedOutput = "***Invalid Command*** \n Please refer the help tab if required"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    # registration_numbers_for_cars_with_colour
    def test_getReg(self):
        command = "registration_numbers_for_cars_with_colour"
        argument = "White"
        expectedOutput = "KA-53-Q-2961,KA-53-Q-291"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    def test_getRegError(self):
        command = "registration_numbers_for_cars_with_colour"
        argument = "red"
        expectedOutput = "No Vehicles are parked in the parking lot"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    # slot_numbers_for_cars_with_colour
    def test_getSlotOfCar(self):
        command = "slot_numbers_for_cars_with_colour"
        argument = "White"
        expectedOutput = "1,2"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    def test_getSlotErr(self):
        command = "slot_numbers_for_cars_with_colour"
        argument = "red"
        expectedOutput = "No Vehicles are parked in the parking lot"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    # slot_number_for_registration_number
    def test_getSlotOfRef(self):
        command = "slot_number_for_registration_number"
        argument = "KA-53-Q-2961"
        expectedOutput = "1"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    def test_getSlotOfRefError(self):
        command = "slot_number_for_registration_number"
        argument = "Test"
        expectedOutput = "No Vehicles are parked in the parking lot"
        self.assertEquals(validateCommandsInstance.validateCommands(command,argument),expectedOutput)

    #----------------------------------------------------------------
    #           Unit test case for Parking Lot
    #   >>42 Unit test has been carried out to test the modules or functions
    #   which are written for the application program
    #   >>Unit test is done with the help of pytest module.
    #   >>It almost covered around 80-90% of problem
    
parkingInstance = parkingClass()    
slotActionsInstance = slotClass()
vehicleActionInstance = vehicleClass()
vehicleClassUpdateInstance = vehicleClassUpdate()
slotClassUpdateInstance = slotClassUpdate()
validateCommandsInstance = validateCommands()
if __name__ == '__main__':
    unittest.main()