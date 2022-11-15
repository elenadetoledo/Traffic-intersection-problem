import pandas as pd
from csv import reader
from math import fabs


class Probability:
    def __init__(self,event=None,prob=None):
        self.e = event
        self.p = prob

    def computeprob(self, Nbeg, Ebeg, Wbeg, act, Nend, Eend, Wend, matrix):
        count1 = 0  # n times we have nbeg,ebeg,wbeg and act
        count2 = 0  # n times we have the whole line
        event = [Nbeg, Ebeg, Wbeg, act, Nend, Eend, Wend]

        for i in range(0, 8785):
            if matrix[i][0] == Nbeg and matrix[i][1] == Ebeg and matrix[i][2] == Wbeg and matrix[i][3] == act:
                count1 += 1
                if matrix[i][4] == Nend and matrix[i][5] == Eend and matrix[i][6] == Wend:
                    count2 += 1




        if count1 != 0:
            self.p = count2 / count1
        else:
            self.p = 0
        self.e = event
        return self

def searchprob(fact, lprob: list)->float:
    for i in lprob:
        if i.e == fact:
            break
    return i.p



#-------MAIN PROGRAM--------
# open file in read mode

MODE= "general" #CHANGE TO "specific" to alter the value of the variables involved in traffic flow
#HERE WE DEFINE OUR CONSTANTS
RAIN = True #Change here to True or False depending on what you wish to study
#We study the possibility that there's an event in one of the highways. Change as you please
EVENTN = True
EVENTE = True
EVENTW = True
DAYOFWEEK = "Friday" #Write here the day of the week that it's being studied
MONTH = "May" #Write here the month of the year being studied
#AVERAGE FLOW RATE ON EACH DIRECTION
FRATEN = 3
FRATEE = 1.27
FRATEW = 1.04

r1= 0
r2= 0
r3 =0
if RAIN == True:
    r1 = 0.5
    r2 = 0.7
    r3 = 2

if EVENTN == True:
    e1 = 0.2
else:
    e1 = 15
if EVENTE == True:
    e2 = 0.3
else:
    e2 = 0.26
if EVENTW == True:
    e3 = 0.5
else:
    e3 = 0.7

d1 = 0
d2 = 0
d3 = 0
m1 = 0
m2 = 0
m3 = 0
if DAYOFWEEK == "Monday":
    d1 = 0.1
    d2 = 0.12
    d3 = 0.4
if DAYOFWEEK == "Tuesday":
    d1 = 0.3
    d2 = 0.9
    d3 = 0.5
if DAYOFWEEK == "Wednesday":
    d1 = 0.4
    d2 = 0.5
    d3 = 0.1
if DAYOFWEEK == "Thursday":
    d1 = 0.4
    d2 = 0.3
    d3 = 0.6
if DAYOFWEEK == "Friday":
    d1 = 0.9
    d2 = 0.6
    d3 = 0.9
if DAYOFWEEK == "Saturday":
    d1 = 0.04
    d2 = 0.03
    d3 = 0.3
if DAYOFWEEK == "Sunday":
    d1 = 0.4
    d2 = 0.2
    d3 = 0.1

if MONTH == "January":
    m1 = 0.3
    m2 = 0.3
    m3 = 0.3
if MONTH == "August":
    m1 = 0.4
    m2 = 0.4
    m3 = 0.4
if MONTH == "February":
    m1 = 0.5
    m2 = 0.5
    m3 = 0.5
if MONTH == "July":
    m1 = 0.6
    m2 = 0.6
    m3 = 0.6
if MONTH == "April":
    m1 = 0.7
    m2 = 0.7
    m3 = 0.7
if MONTH == "March":
    m1 = 0.8
    m2 = 0.8
    m3 = 0.8
if MONTH == "June":
    m1 = 0.9
    m2 = 0.9
    m3 = 0.9
if MONTH == "September":
    m1 = 1
    m2 = 1
    m3 = 1
if MONTH == "December":
    m1 = 1.1
    m2 = 1.1
    m3 = 1.1
if MONTH == "November":
    m1 = 1.2
    m2 = 1.2
    m3 = 1.2
if MONTH == "October":
    m1 = 1.3
    m2 = 1.3
    m3 = 1.3
if MONTH == "May":
    m1 = 1.4
    m2 = 1.4
    m3 = 1.4

if MODE == "general":
    r1 = 0
    r2 = 0
    r3 = 0
    m1 = 0
    m2 = 0
    m3 = 0
    e1 = 0
    e2 = 0
    e3 = 0
    d1 = 0
    d2 = 0
    d3 = 0



count = 0
mdata = []
for i in range(0,8786):
     mdata.append([])
     for j in range(0,7):
         mdata[i].append(None)

with open(r"C:\Users\elena\OneDrive\Escritorio\Data.csv", 'r') as read_obj: #READ THE FILE
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj,delimiter=';')
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        for j in range(0,7):
            mdata[count][j] = row[j]
        count +=1

st1 = ["High","High","Low"]#
st2 = ["High","Low","Low"]#
st3 = ["Low","Low","Low"]#GOAL STATE
st4 = ["Low","Low","High"]#
st5=  ["High","High","High"]#
st6 = ["Low","High","Low"]#
st7 = ["Low","High","High"]#
st8 = ["High", "Low", "High"]#
#create a vector with the states
states=[]
states.append(st1)
states.append(st2)
states.append(st3)
states.append(st4)
states.append(st5)
states.append(st6)
states.append(st7)
states.append(st8)

action = ["N","E","W"]
lprobN=[]
#store the probabilities in a list of structures. THESE ARE THE CONDITIONAL PROBABILITIES P(st1| a, st2)
a = action[0]
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)

fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)
#
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)
#
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st1[0], st1[1], st1[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st2[0], st2[1], st2[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st3[0], st3[1], st3[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st4[0], st4[1], st4[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st5[0], st5[1], st5[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st6[0], st6[1], st6[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st7[0], st7[1], st7[2], mdata)
lprobN.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st8[0], st8[1], st8[2], mdata)
lprobN.append(p1)

a = action[1]
lprobE = []
fact = Probability()
p1 = fact.computeprob(st1[0],st1[1],st1[2],a,st1[0],st1[1],st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2],a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)

fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)
#
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)
#
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st1[0], st1[1], st1[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st2[0], st2[1], st2[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st3[0], st3[1], st3[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st4[0], st4[1], st4[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st5[0], st5[1], st5[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st6[0], st6[1], st6[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st7[0], st7[1], st7[2],mdata)
lprobE.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st8[0], st8[1], st8[2],mdata)
lprobE.append(p1)

a = action[2]
lprobW = []
fact = Probability()
p1 = fact.computeprob(st1[0],st1[1],st1[2],a,st1[0],st1[1],st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2],a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st1[0], st1[1], st1[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)

fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st2[0], st2[1], st2[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)
#
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st3[0], st3[1], st3[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st4[0], st4[1], st4[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st5[0], st5[1], st5[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)
#
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st6[0], st6[1], st6[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st7[0], st7[1], st7[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)

#
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st1[0], st1[1], st1[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st2[0], st2[1], st2[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st3[0], st3[1], st3[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st4[0], st4[1], st4[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st5[0], st5[1], st5[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st6[0], st6[1], st6[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st7[0], st7[1], st7[2],mdata)
lprobW.append(p1)
fact = Probability()
p1 = fact.computeprob(st8[0], st8[1], st8[2], a, st8[0], st8[1], st8[2],mdata)
lprobW.append(p1)








#WE HAVE TO DEFINE OUR INTERPRETATION OF THE COST
#list with cost(N), cost(W), cost(E)
cost=[(r2+m2+d2+e2+20*FRATEW)+ (r3+m3+d3+e3+20*FRATEE) + 3,
      (r1+m1+d1+e1+20*FRATEN)+(r3+m3+d3+e3+20*FRATEE) + 3,
      (r2+m2+d2+e2+20*FRATEW) + (r1+m1+d1+e1+20*FRATEN) +3]

#--------------------------------BELLMAN EQUATIONS------------------------------------------------------------------------------------
Vst1=[]
Vst2=[]
Vst3=[] #Goal state. Will always be zero
Vst4=[]
Vst5=[]
Vst6=[]
Vst7=[]
Vst8=[]
#max size of V is 50 (setted manually). WE CAN CHANGE IT OR DECLARE IT AS A CONSTANT. MIRAR
for i in range(0, 200):
    Vst1.append(0)
for i in range(0, 200):
    Vst2.append(0)
for i in range(0, 200): #WILL ALWAYS STAY AS ZERO (goal)
    Vst3.append(0)
for i in range(0, 200):
    Vst4.append(0)
for i in range(0, 200):
    Vst5.append(0)
for i in range(0, 200):
    Vst6.append(0)
for i in range(0, 200):
    Vst7.append(0)
for i in range(0, 200):
    Vst8.append(0)

counter=0
tolerance=10 #enters the loop
while tolerance>10^-6 and (counter+1)<200: #buscar una explicación para este criterio

    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st1[0])
        string.append(st1[1])
        string.append(st1[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st1[0])
        string.append(st1[1])
        string.append(st1[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st1[0])
        string.append(st1[1])
        string.append(st1[2])

        probE.append(string)

    # vst3 ni lo añado pq Vst3=0 always
    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst1[counter+1] = min(actN, actW, actE)
    diff = fabs(Vst1[counter + 1] - Vst1[counter])
    tolerance=diff

    # next-state---------------------st2
    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st2[0])
        string.append(st2[1])
        string.append(st2[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st2[0])
        string.append(st2[1])
        string.append(st2[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st2[0])
        string.append(st2[1])
        string.append(st2[2])

        probE.append(string)

    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst2[counter+1] = min(actN, actW, actE)
    diff = fabs(Vst2[counter + 1] - Vst2[counter])
    if diff>tolerance:
        tolerance=diff

    # new-state---------------------st4
    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st4[0])
        string.append(st4[1])
        string.append(st4[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st4[0])
        string.append(st4[1])
        string.append(st4[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st4[0])
        string.append(st4[1])
        string.append(st4[2])

        probE.append(string)

    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst4[counter+1] = min(actN, actW, actE)
    diff = fabs(Vst4[counter + 1] - Vst4[counter])
    if diff>tolerance:
        tolerance=diff

    # new-state----------------------st5
    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st5[0])
        string.append(st5[1])
        string.append(st5[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st5[0])
        string.append(st5[1])
        string.append(st5[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st5[0])
        string.append(st5[1])
        string.append(st5[2])

        probE.append(string)

    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst5[counter+1] = min(actN, actW, actE)
    diff = fabs(Vst5[counter + 1] - Vst5[counter])
    if diff>tolerance:
        tolerance=diff

    # new-state--------------------------st6
    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st6[0])
        string.append(st6[1])
        string.append(st6[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st6[0])
        string.append(st6[1])
        string.append(st6[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st6[0])
        string.append(st6[1])
        string.append(st6[2])

        probE.append(string)

    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst6[counter+1] = min(actN, actW, actE)
    diff = fabs(Vst6[counter + 1] - Vst6[counter])
    if diff>tolerance:
        tolerance=diff

    # new-state--------------------------st7
    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st7[0])
        string.append(st7[1])
        string.append(st7[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st7[0])
        string.append(st7[1])
        string.append(st7[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st7[0])
        string.append(st7[1])
        string.append(st7[2])

        probE.append(string)

    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst7[counter+1]= min(actN, actW, actE)
    diff = fabs(Vst7[counter + 1] - Vst7[counter])
    if diff>tolerance:
        tolerance=diff

    # new-state-------------------------st8
    probN = []
    probW = []
    probE = []
    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("N")
        string.append(st8[0])
        string.append(st8[1])
        string.append(st8[2])

        probN.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("W")
        string.append(st8[0])
        string.append(st8[1])
        string.append(st8[2])

        probW.append(string)

    for i in range(0, 8):
        string = []
        tempst = states[i]
        string.append(tempst[0])
        string.append(tempst[1])
        string.append(tempst[2])
        string.append("E")
        string.append(st8[0])
        string.append(st8[1])
        string.append(st8[2])

        probE.append(string)

    actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
        counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
               counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
               counter] * searchprob(probN[7], lprobN)

    actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
        counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
               counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
               counter] * searchprob(probW[7], lprobW)

    actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
        counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
               counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
               counter] * searchprob(probE[7], lprobE)

    Vst8[counter+1] = min(actN, actW, actE)
    aux1=Vst8[counter + 1]
    aux2=Vst8[counter]
    var=aux2
    diff = fabs (var)
    if diff>tolerance:
        tolerance=diff

    #UPDATE INDEX
    counter +=1


#end of Bellman equations
#-----------------------------------------------------------------------------------------------------------------
#LOOK FOR AN OPTIMAL POLICY
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st1[0])
    string.append(st1[1])
    string.append(st1[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st1[0])
    string.append(st1[1])
    string.append(st1[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st1[0])
    string.append(st1[1])
    string.append(st1[2])

    probE.append(string)

#vst3 ni lo añado pq Vst3=0 always
actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)



value= min(actN, actW, actE)
if value==actN:
    Polst1="N"
elif value==actW:
    Polst1="W"
else:
    Polst1="E"

#next-state---------------------st2
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st2[0])
    string.append(st2[1])
    string.append(st2[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st2[0])
    string.append(st2[1])
    string.append(st2[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st2[0])
    string.append(st2[1])
    string.append(st2[2])

    probE.append(string)

actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)
value= min(actN, actW, actE)
if value==actN:
    Polst2="N"
elif value==actW:
    Polst2="W"
else:
    Polst2="E"

#new-state---------------------st4
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st4[0])
    string.append(st4[1])
    string.append(st4[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st4[0])
    string.append(st4[1])
    string.append(st4[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st4[0])
    string.append(st4[1])
    string.append(st4[2])

    probE.append(string)

actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)
value= min(actN, actW, actE)
if value==actN:
    Polst4="N"
elif value==actW:
    Polst4="W"
else:
    Polst4="E"
#new-state----------------------st5
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st5[0])
    string.append(st5[1])
    string.append(st5[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st5[0])
    string.append(st5[1])
    string.append(st5[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st5[0])
    string.append(st5[1])
    string.append(st5[2])

    probE.append(string)

actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)

value= min(actN, actW, actE)
if value==actN:
    Polst5="N"
elif value==actW:
    Polst5="W"
else:
    Polst5="E"

#new-state--------------------------st6
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st6[0])
    string.append(st6[1])
    string.append(st6[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st6[0])
    string.append(st6[1])
    string.append(st6[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st6[0])
    string.append(st6[1])
    string.append(st6[2])

    probE.append(string)
actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)
value= min(actN, actW, actE)
if value==actN:
    Polst6="N"
elif value==actW:
    Polst6="W"
else:
    Polst6="E"
#new-state--------------------------st7
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st7[0])
    string.append(st7[1])
    string.append(st7[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st7[0])
    string.append(st7[1])
    string.append(st7[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st7[0])
    string.append(st7[1])
    string.append(st7[2])

    probE.append(string)

actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)
value= min(actN, actW, actE)
if value==actN:
    Polst7="N"
elif value==actW:
    Polst7="W"
else:
    Polst7="E"

#new-state-------------------------st8
probN=[]
probW=[]
probE=[]
for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("N")
    string.append(st8[0])
    string.append(st8[1])
    string.append(st8[2])

    probN.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("W")
    string.append(st8[0])
    string.append(st8[1])
    string.append(st8[2])

    probW.append(string)

for i in range(0, 8):
    string=[]
    tempst=states[i]
    string.append(tempst[0])
    string.append(tempst[1])
    string.append(tempst[2])
    string.append("E")
    string.append(st8[0])
    string.append(st8[1])
    string.append(st8[2])

    probE.append(string)

actN = cost[0] + Vst1[counter] * searchprob(probN[0], lprobN) + Vst2[counter] * searchprob(probN[1], lprobN) + Vst4[
    counter] * searchprob(probN[3], lprobN) + Vst5[counter] * searchprob(probN[4], lprobN) + Vst6[
           counter] * searchprob(probN[5], lprobN) + Vst7[counter] * searchprob(probN[6], lprobN) + Vst8[
           counter] * searchprob(probN[7], lprobN)

actW = cost[1] + Vst1[counter] * searchprob(probW[0], lprobW) + Vst2[counter] * searchprob(probW[1], lprobW) + Vst4[
    counter] * searchprob(probW[3], lprobW) + Vst5[counter] * searchprob(probW[4], lprobW) + Vst6[
           counter] * searchprob(probW[5], lprobW) + Vst7[counter] * searchprob(probW[6], lprobW) + Vst8[
           counter] * searchprob(probW[7], lprobW)

actE = cost[2] + Vst1[counter] * searchprob(probE[0], lprobE) + Vst2[counter] * searchprob(probE[1], lprobE) + Vst4[
    counter] * searchprob(probE[3], lprobE) + Vst5[counter] * searchprob(probE[4], lprobE) + Vst6[
           counter] * searchprob(probE[5], lprobE) + Vst7[counter] * searchprob(probE[6], lprobE) + Vst8[
           counter] * searchprob(probE[7], lprobE)

value= min(actN, actW, actE)
if value==actN:
    Polst8="N"
elif value==actW:
    Polst8="W"
else:
    Polst8="E"

Polst3="Goal"


print("-----------------------")
print("EXPECTED VALUES: ")
print("V(HHL): ", Vst1[counter])
print("V(HLL): ", Vst2[counter])
print("V(LLL): ", Vst3[counter])
print("V(LLH): ", Vst4[counter])
print("V(HHH): ", Vst5[counter])
print("V(LHL): ", Vst6[counter])
print("V(LHH): ", Vst7[counter])
print("V(HLH): ", Vst8[counter])
print("-----------------------")
#SHOW POLICY-----------------------------------------------
print("Policy for H H L ->", Polst1," ")
print("Policy for H L L ->", Polst2, " ")
print("Policy for L L L ->", Polst3, " ")
print("Policy for L L H ->", Polst4)
print("Policy for H H H ->", Polst5)
print("Policy for L H L ->", Polst6)
print("Policy for L H H ->", Polst7)
print("Policy for H L H ->", Polst8)









