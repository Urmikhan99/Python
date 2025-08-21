# Arithmetic operators
a=5
b=20


# Addition
print(a+b)

# Subtraction
print(a-b)

# Division (float)
print(b/a)

# Floor Division (integer division)
print(b//a)

# Exponent (power)
print(a**b)

# Modulus (remainder)
print(32%5)


# Compound assignment operator
a +=20
a +=40
a +=60
a *=40
a **10
print(a)

# Comparison operator (Boolean result )
a=12.1
b=12
print(a == b)
print (a != b)
print( a>b )
print(23 >= 33)
print(45<=45)

print(ord("A"))
print(ord("B"))
print("A"<"B")
print("A">"B")

# Logical operators
# logical AND(and)

x=10
y=20
z=30
if x>y and y>z:
    print("x is largets Number")
else:
    print("x i not largest Number")


# Logical OR(or)
x=30
y=50
z=10
if x>y or x>z:
    print("x is at least larger than one number")
else:
    print("x is the smaller number")

# not operations
x=10
y=20
z=30
if not(x>y or x>z):
    print("x is not the larger number")
else:
    print("x is not the smallest number")



print(not 12==12)

'''
Rule:

and → True only if all conditions are True

or → True if at least one condition is True

not → Reverses the result of a condition
'''