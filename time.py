"""
Date Class. Provide an interface to a time module where
users can request dates in a few (given) date formats such as
“MM/DD/YY,” “MM/DD/YYYY,” “DD/MM/YY,” “DD/MM/
YYYY,” “Mon DD, YYYY,” or the standard Unix date of “Day
Mon DD, HH:MM:SS YYYY.” Your class should maintain a
single value of date and create an instance with the given
time. If not given, default to the current time at execution.
Additional methods:

update() - changes the data value to reflect time given or
            current time as a default
display() - takes format indicator and displays date in
            requested format:
"""


#!/usr/bin/python
import time

from time import gmtime, strftime

print("Do you want the date base on your choice :")
print(" Press 0 to allow the system to ouput the default time :")
print(" Press 1 to input the seconds :")


response = int(input("Your response :"))


class Date:

    def __init__(self, data = 1000):
        self.data = data

    def update(self):
        if (response == 0):
            print("default time is :", time.ctime())

        elif (response == 1):
            data = int(input("Enter your time in seconds"))
            print("default time is :", time.ctime(data))

        else:
            print("Your response should be eithern 0 or 1")

    def display(self):

        if (response == 0):
            print("The choice of Format")
            print("Select : 1. for 'MDY' => MM/DD/YY")
            print("Select : 2. for 'MDYY' => MM/DD/YYYY")
            print("Select : 3. for 'DMY' => DD/MM/YY")
            print("Select : 4. for 'DMYY' => DD/MM/YYYY")
            print("Select : 5. for 'MODYY' => Mon DD, YYYY")

            formatoption = int(input(" Indicate your format option :"))
            if (formatoption == 1):
                print(strftime("%m/%d/%y", gmtime()))

            elif (formatoption == 2):
                print(strftime("%m/%d/%Y", gmtime()))

            elif (formatoption == 3):
                print(strftime("%d/%m/%y", gmtime()))

            elif (formatoption == 4):
                print(strftime("%d/%m/%Y", gmtime()))

            elif (formatoption == 5):
                print(strftime("%b %d %Y", gmtime()))

        elif (response == 1):
            
            print("The choice of Format")
            print("Select : 1. for 'MDY' => MM/DD/YY")
            print("Select : 2. for 'MDYY' => MM/DD/YYYY")
            print("Select : 3. for 'DMY' => DD/MM/YY")
            print("Select : 4. for 'DMYY' => DD/MM/YYYY")
            print("Select : 5. for 'MODYY' => Mon DD, YYYY")

            formatoption = int(input(" Indicate your format option :"))
            if (formatoption == 1):
                print(strftime("%m/%d/%y", gmtime(self.data)))

            elif (formatoption == 2):
                print(strftime("%m/%d/%Y", gmtime(self.data)))

            elif (formatoption == 3):
                print(strftime("%d/%m/%y", gmtime(self.data)))

            elif (formatoption == 4):
                print(strftime("%d/%m/%Y", gmtime(self.data)))

            elif (formatoption == 5):
                print(strftime("%b %d %Y", gmtime(self.data)))

mytime = Date()
mytime.update()
mytime.display()


        
