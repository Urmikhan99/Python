
# a=4
# b=4
# diff=a+b
# print(diff)

# string & Numeric values can operate togather with
# a,b=2,3
# Txt="@"
# print(2*Txt*3)

# 💡 Rule:
# Python allows string × integer to repeat the string multiple times.
# But string + number (like "@" + 2) will give an error.

# String & String can operate with 
# A,B="3",2
# Txt="@"
# print((A+Txt)*B)

# 💡 Rule:
# You can concatenate strings with +
# You can repeat strings by multiplying with an integer.
# But you cannot directly add a string and an integer ("3" + 2) — that gives an error.

# Numeric Values can Operate with all arithmetic Operators

# A,B=3,2
# C=4
# print(A+B*C)

# 💡 Rule:
# Numeric variables (integers, floats) can use + - * / % // ** operators.
# Python respects operator precedence.

# Arithmetic expression with integer and float will result in float
# A,B=5,3.0
# C=A*B
# print(C)


# A,B=1,2
# C=A/B
# print(C)

# 💡 Rule:
# / → true division, always returns a float.
# // → floor division, returns integer (truncated result).

# A,B=1,2
# C=A//B
# print(C,A/B)

# 💡 Rule:
# / → float division
# // → floor division (integer part only)

# A,B=12,5
# C=A//B
# print((C))

# Floor Division
# Floor division মানে ভাগ করে integer part নাও, remainder ফেলে দাও।

A,B=12,-5
C=A//B
print((C))
