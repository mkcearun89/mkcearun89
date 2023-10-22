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
