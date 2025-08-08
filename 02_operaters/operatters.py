# Arithmetic Opetators
num1 = 3
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2) # quotient
print(num1%num2) #remainder
print(num1//num2) #quotient is round off to nearest integer
print(num1**num2) #expo (square of)
print(num1)

# compound assigment operators
num = 10
# num = num + 5
#num += 5
#num -= 5
num *= 5

print(num)

# comparsion operators
num1 = 3
num2 = 2
isEqual = num1 == num2
isnotequal = num1 != num2
isgreatequal = num1 >= num2
print(isEqual)
print(isnotequal)
print(isgreatequal)

str1 = "python"
str2 = "Django"
str3 = "PYTHON"
str4 = "PYTHOn"

print(str1 == str2)
print (str2 == str3)

print(str1 > str2)
print(str3 > str4)

#logical operators
num1 = 7
num2 = 5
num3 = 3
num4 = 5

# T and T --> T
resultAnd = num1 > num2 and num3 > num4
resultNot = num1 > num2
print (resultAnd)
print (resultNot)

# Membership Operators
text = "python in an programming Language"
isZpresent = 'Z' in text
islpresent = 'l' in text
ispatternPresent = 'prog' in text
isJavaPresent = 'java' not in text
print(isZpresent)
print(islpresent)
print(ispatternPresent)
print(isJavaPresent)

Courses_list = ["java","python","cloud","devops"]
inpythonpresent = "python" in Courses_list
print(inpythonpresent)

#identity Operators
#imutables
num1 = 10
num2 = 10

List1 = [1,2,3]
List2 = [1,2,3]

print(num1 is num2)
print(num1 == num2)

print(List1 is List2)
print(List1 == List2)

# bitwise Operators
a = 5 #0000000000101
b = 3 #0000000000011

result = a & b 
print(result)

result2 = a | b
print(result2)

result3 = a^b
print(result3)

result4 = ~b
print(result4)

print(3<<2) #0000000000000011 --> 0000000000001100
print(3<<1)
print(3<<4)

print(3>>1)
print(3>>3)
print(8>>2)


