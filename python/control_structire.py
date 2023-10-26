""""
Write a Python program that displays a message as follows for a given number:
If it is a multiple of 3, display "Zip"
If it is a multiple of 5, display "Zap"
If it is a multiple of both 3 and 5, display "Zoom"
If it does not satisfy any of the above given conditions, display "Invalid"
"""
def calculation(a):
    print(" the entered numvber is ", a)
 
    if(a % 5==0):
        print("zip")
    elif(a % 3==0):
        print("zap")
    elif(a % 5==0 and a % 3==0):
        print("zoom")
    else:
        print("invalid")

calculation(56)

#####################################################################################################################
"""
 Sum of digits of the number 123 will be 6
 """
def sumofgivennumber(num):
    sum = 0
    for i in str(num):
        sum+=int(i)
    print (sum)

sumofgivennumber(123)
####################################################################################################################
"""
Ticket generation for Airline
"""

def tickgeneration(passcount,source,destination):
    airline='indigo'
    ticketlist=[]
    for i in range(1,(passcount+1)):
        ticket=airline+'-'+source[:3]+'-'+destination[:3]+'-'+str(i)
        ticketlist.append(ticket)
    return(ticketlist)

        
tickets=tickgeneration(10,'Chennai','DELHI')
lengthof=len(tickets)
for i in range(1,lengthof):
 print (tickets[i])
######################################################################################################################
""""
Program to find an year is leap year or not
""""
def leapyear_func(input_year):
    if(input_year%400 == 0 and input_year%100== 0):
        print("given year is a leap year")
    elif(input_year%4== 0 and input_year%100!=0):
        print("given year is a leap year")
    else:
        print("given year is not a leap year")


leapyear_func(3000)
##########################################################################################################################
"""
to find a given given number is prime or not
"""
def primenumberfind(in_num):
    if in_num>1:
        for i in range(2,in_num):
            if(in_num%i==0):
                return("given number is not a prime number")
            else:
                return("given number is a prime number")
    else:
        return("given number is not a prime number")


print(primenumberfind(111))
###########################################################################################################################
