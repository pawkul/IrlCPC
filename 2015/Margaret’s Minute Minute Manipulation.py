#!/bin/usr/python3

#input
lst = [0,0,0,0,0,0]
lst2 = [0,0,0,0,0,0]
counter = 8
counter2 = 8
lst_fin = [0,0,0,0,0,0]

for _ in range(4):

   a = input().replace(" ","")
   for num in range(6):
      if a[num] == '1':
         lst[num] += counter

   counter = counter / 2

for _ in range(4):

   a = input().replace(" ","")
   for num in range(6):
      if a[num] == '1':
         lst2[num] += counter2

   counter2 = counter2 / 2


print(lst)
print(lst2)

#adding
count = 0
for e in range(1,7):
    
    if e%2 == 1:

        if (lst[-e] + lst2[-e] + count) >= 10:
            lst_fin[-e] += (lst[-e] + lst2[-e] + count) % 10
            count = 1

        else:
            lst_fin[-e] += lst[-e] + lst2[-e] + count
            count = 0


    else:

        if (lst[-e] + lst2[-e] + count) >= 6:
            count = 1
            lst_fin[-e] += (lst[-e] + lst2[-e] + count) % 6

        else:
            lst_fin[-e] += lst[-e] + lst2[-e] + count
            count = 0
            

print(lst_fin)

#check if or over 24h and fix if so
num = int("%i%i"%(lst_fin[0],lst_fin[1]))

if num >= 24:
    num = num % 24
    lst_fin[0], lst_fin[1] = num // 10, num % 10

print(lst_fin)

#print
counter = 0
x = ''
while True:
    if counter == 4:
        break
    
    for e in lst_fin:
        x += (bin(int(e))[2:].zfill(4)[counter])
        x += ' '

    print(x)
    x = ''
    

    counter += 1
