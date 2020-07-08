*** Settings ***
Resource  Keywords.robot

*** Test Cases ***

Get Data Tests
    Get All Users Test
    Get A Specific User Test
    single user not found Test
    delayed response test

Alter Data Tests
    Create a New User and Verify it was created
    Update User and Verify it has been updated
    Delete User and Verify it Has been Deleted

Authorization Tests
    Successfull Registration Test
    UnSuccessfull Registration Test
    Successfull Login Test
    UnSuccessfull login Test

















