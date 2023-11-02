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
