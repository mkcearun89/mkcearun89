"""
program to find square
"""

def findsquare(in_num):
    return(in_num*in_num)
    
print(findsquare(5))

"""
program to find polindrome string
"""
def ispolindrome(s):
    rev=''.join(reversed(s))
    if (s==rev):
        return True
    else:
        return False
        
print (ispolindrome('malayalam'))
        
