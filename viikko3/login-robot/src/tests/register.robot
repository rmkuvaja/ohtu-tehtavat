*** Settings ***
Resource  resource.robot
Test Setup  Create User And Validate

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  iines  Helkama123
    Output should contain  New user registered

*** Keywords ***
Create User And Validate
    Input New Command

*** Test Cases ***
Register With Already Taken Username And Valid Password
    Create User  iines  Helkama123
    Input Credentials  iines  Helka123
    Output should contain  User with username iines already exists

Register With Too Short Username And Valid Password
    Input Credentials  ii  Helkama123
    Output should contain  Username minimum 3 signs

Register With Valid Username And Too Short Password
    Input Credentials  iines  Helka1
    Output should contain  Password don't contain all required characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  iines  helkamama
    Output should contain  Password don't contain all required characters
