# for loop
a=range(1,21,1)      
for i in a :
    print(i)

#range(start, stop, step)


for i in range(1,21,1):
    print(i)

for i in range(21):
    print (i)

for i in range(16,0,-1):
    print(i)

for i in range(-5,-15,-1):
    print(i)

# lets print a table

for i in range(7,71,7):
    print(i)

n=int(input("which table you want"))

for i in range(n,(n*10)+1,n):
    print(i)