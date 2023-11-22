##printing a string
str="Arunkumar"

print('printing a string - ' , str)

##printing a string in upper case
print('the upper case example -', str.upper())

##printing a string in lower case
str="ARUNKUMAR"
print('the lower case example -', str.lower())

#capitalize - making first letter to upper case
str='arunkumar'
print(str.capitalize())

#swapcase
str='Arun Kumar'
print(str.swapcase())

#to get the first letter from the string
str='Arunkumar'
print(str[0])


str='Arunkumar'
print(str[2:])
print(str[:2])

lt=[10,2,3,4,5,6,67,8,9]
print(lt[2:])


str="Arunkumar"
print(str[0:5])


## to find length of a string
str="Arunkumar"
print('The length of a string - ', len(str))

print('printing the string vertically')
for i in str:	
	print(i)
    

##strings are immutable
str="Arunkumar"
t=str[0]
print('Example says strings are immutable - ', str[0])

##
str2="Chennai"
print(str+str2[0:])

print ("i" in str2)

print("z" in str2)

#join

str1="Arun"
print(str1.join(str2))

str1="India is a great country"
print(str1.split(" "))

