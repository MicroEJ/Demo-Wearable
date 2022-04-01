# Overview

This project contains a minimal sample of a watch application. 

It consists in:
- an analog watchface
- an scrollable list of applications

## Application flow

The user can go from the watchface to the application list and vice versa by pressing the physical button.
Clicking on an item of the list opens a new page with the item's information. Pressing the button goes back to the list.


## Main classes

### WatchExample class

It is the entry point of the application. 

At boot, it does the following steps:

1. starts the MicroUI framework.
2. creates a desktop, a placeholder for the application widget tree.
3. creates the watchface and sets it as the root widget of the desktop.
4. shows the desktop on the display.

This class also provides convenient methods for navigating from one view to the other.


### Watchface class

This class implements a widget that displays three hands (hour, minute, second) and a full-screen background image.


### ApplicationList class

A widget that represents a scrollable list. It contains other widgets (the application items, see class `ApplicationListItem`).


### ApplicationListItem class

A widget that represents an item of the application list. It displays the icon and name of applications. Note that for purposes of performances, an image of the name is drawn rather than the text itself: drawing an image is faster than drawing a string. 


# Usage

## Run on the Virtual Device
   1. Right-click on this project
   2. Select `Run As` > `MicroEJ Application`
   3. Select `WatchExample (Simulator)`
   4. Click `Ok`

The application runs on the Virtual Device.

## Run on the device
   1. Right-click on this project
   2. Select `Run As` > `MicroEJ Application`
   3. Select `WatchExample (Device)`
   4. Click `Ok`
   
Upon success:
   - The MicroEJ Application file `microejapp.o` has been deployed to `${root.dir}`/`${microejapp.relative.dir}`.
   - The MicroEJ Platform runtime file `microejruntime.a` has been deployed to `${root.dir}`/`${microejlib.relative.dir}`.
   - The platform header files `*.h` have been deployed to `${root.dir}`/`${microejinc.relative.dir}`.
   - The BSP is compiled and linked using the C toolchain.
 
 	5. Program the firmware to the target device. You may use the `run.bat` script of the platform to program the device.

Notes:
- The above properties are platform options, they are set in the `bsp/bsp.properties` file of the platform configuration project (`*-configuration)`. They provide a flexible way to configure the BSP connection to target any kind of projects, teams organizations and company build flows. More about BSP Connection: <https://docs.microej.com/en/latest/PlatformDeveloperGuide/platformCreation.html#bsp-connection>.
   

# Requirements

This library requires the following Foundation Libraries:

    EDC-1.3, BON-1.4, MICROUI-3.0, DRAWING-1.0

# Dependencies

_All dependencies are retrieved transitively by MicroEJ Module Manager_.

# Source

N/A.

# Restrictions

None.

---  
_Copyright 2022 MicroEJ Corp. All rights reserved._  
_Use of this source code is governed by a BSD-style license that can be found with this software._
