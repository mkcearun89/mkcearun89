
##creating empty list
lt=[]
print(lt)

##slicing list
lt=[12,40,'Arun','Kumar']
print('removing first from the list lt[1:] - ' ,lt[1:])
print('removing last from the list lt[1:] - ' , lt[:3])
print('printing the range of values by using index -' , lt[0:2])

a='Arun'
b='kumar'
c='chennai'
d=[a,b,c]
print(d)

a=[1,2,4,5,6]
a.append(9)
print(a)
a.pop(1)
print(a)

print('deleting using index value - del a[0] ' )
del a[0]
print(a)

print('deleting using the value in list')
a.remove(4)
print(a)

print('adding elements using append')
a.append(99)
print(a)

print('removing element using pop - index values')
a.pop(3)
print(a)

print('what happens if we multiply a list with intergers list*2' '- printing the elements twice')
print(a*2)

print('concatinating two lists a+b')
a=[1,2,3]
b=[4,5,6]
print(a+b)


   
