#!/usr/bin/python3
for i in range(0, 98):
    if i % 16 == 10:
        if(int(i / 16) != 0):
            print("{} = 0x{}{}".format(i, int(i / 10), i % 16))
        else:
            print("{} = 0x{}".format(i, i % 16))
    elif i % 16 == 11:
         if(int(i / 16) != 0):
             print("{} = 0x{}{}".format(i, int(i / 10), i % 16))
         else:                                                                                                       print("{} = 0x{}".format(i, i % 16))
     elif i % 16 == 12:
         if(int(i / 16) != 0):
             print("{} = 0x{}C".format(i, int(i / 10)))
         else:
             print("{} = 0x{}".format(i, i % 16))
    elif:

