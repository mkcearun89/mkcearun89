#inserting a value in a list

print('inserting a value into a list using insert(index,valuetoinsert)')
a=[1,2,3,4,5,6,7,8]
a.insert(0,99)
print(a)

print('to print the square of numbers from 1 to 100')
a=[]
for i in range(1,101):
    a.append(i*i)
print(a)

a=[]
for i in range(1,101):
    a.append(i**2)
print(a)
