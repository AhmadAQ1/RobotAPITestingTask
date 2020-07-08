*** Settings ***
Resource  Keywords.robot

*** Test Cases ***

Get Data Tests
    Get All Users Test
    Get A Specific User Test
    Single User Not Found Test
    Delayed Response Test

Alter Data Tests
    Create A New User And Verify It Was Created
    Update User And Verify It Has Been Updated
    Delete User And Verify It Has been Deleted

Authorization Tests
    Successfull Registration Test
    UnSuccessfull Registration Test
    Successfull Login Test
    UnSuccessfull login Test

















