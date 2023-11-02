"""
program to find proper divisor of given number
"""

def proper_divisor(num):
    lt=[]
    for i in range(1,num):
       if(220%i==0):
            lt.append(i)
    return(lt)

lt1=proper_divisor(220)
print(lt1)

#############################################################################################
"""
program to find leap years for the next 15 years of given given year

def leapyear(input_year):
    oplt=[]
    for input_year in range(input_year,input_year+15):
        if(input_year%400 == 0 and input_year%100== 0):
            oplt.append(input_year)
            input_year+=1
        elif(input_year%4== 0 and input_year%100!=0):
            oplt.append(input_year)
            input_year+=1
        else:
            input_year+=1
    return(oplt)

print(leapyear(2010))
######################################################################################################
