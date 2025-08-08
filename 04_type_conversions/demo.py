# type conversion 

a = 100 #int
b = 3.5 #float
c = a + b #python will convert to float automatically 
print(c)
print(type(c))

#Type Casting - no data loss
x = 100#int
y = float(x)# y should be float
print(x)
print(y)
print(type(y))

#type casting - data lossl
l= 3.14
m = int(l) # l should be int
print(l)
print(m)
print(type(m))

#above are for numeric types

#text to numeric or viceversa

x = "100"
y = int(x)+10
# y = x+10 --> typeerror: can only concatenate str ( not "int") to str

print(y)
print(type(y))

z = 10 #int
num_text = str(z)
print(type(num_text))

#non-numeric string 
x = "hello"
#y = int(x) --> valuaerror : invalid for int() with base 10 : 'hello'

x = 1j
# y = int(x)