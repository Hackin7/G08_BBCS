# G08_BBCS
Group 8's code for the BuildingBloCS Computing Conference 2017

## Competition in BBCS (1st place winner)
Rules:https://docs.google.com/document/d/1_PWH3DbfO9kBflDBdFyJ9L9nkCnmMvkTJRWiFCYVMKA/edit

Competition code in competition.py, which is a smart attendance taking system

1 microbit act as host, others as client.

The host counts the number of clients avaliable

Both host and client have a built in compass

To make it recalibratable, add this (with indent to show in loop) at last line:

```
if button_b.is_pressed(): compass.calibrate
```
