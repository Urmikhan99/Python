a="U"
print(ord(a))


a=55
print(chr(a))

'''
ord("A") → ASCII / Unicode value of "A" is 85
ord = ordinal → character থেকে number
chr = character → number থেকে character
'''

#indexing
a="Urmi"
print(a[1],a[-1])
print(a[2])
'''
In Python, negative indexing allows accessing elements from the end of a string (or list).
a[-1] → last character of the string "Urmi".
'''

# string slicing
a="urmi coder"
print(a[5::1])


a=5
a=str(a)        #int → string Convert
print(type(a))

print(bool(a)) 


num_str = "100"   # String
num_int = 20      # Integer

# Convert string to integer before addition
result = int(num_str) + num_int

print("num_str (before):", num_str, "| Type:", type(num_str))
print("num_int:", num_int, "| Type:", type(num_int))
print("Result:", result, "| Type:", type(result))

# Convert integer to string before concatenation
concat = num_str + str(num_int)
print("Concatenation Result:", concat, "| Type:", type(concat))