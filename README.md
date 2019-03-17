# ExplorerTest
Simple Hardware Test Script for Explorer Devices

# Usage

    git clone https://github.com/EnhancedRadioDevices/ExplorerTest.git
    cd ExplorerTest
    sudo ./run_test

When you run the test, it will check to see if you have the required software to run hardware installed. If you don't, it will attempt to install it for you.

# What is tested?

This code will ensure that the single-board computer can talk to the radio chip. It will also ensure that the screen is working (if your explorer has a screen). 

# What is not tested?

## Radio range

No RF transmissions or receptions are performed in this test, because we don't know what you're trying to connect to.

If this software passes and you are having issues communicating over RF with another device, here are things we recommend checking:

* software configuration
* antenna type and connection (if using an external antenna)
** note that the RPi version of the Explorer requires an external antenna
* the other device you're trying to communicate with
* try putting the devices right next to each other and see what happens. If this works, then one device or the other has antenna issues

## Battery charging

This software doesn't test battery charging. You can try testing that manually by plugging in a battery to the battery port, then plugging in USB. If the charging LED comes on, then it should be working.

## Buttons

The RPi version of the Explorer has buttons. This software doesn't test them (yet).
