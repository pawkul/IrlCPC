#!/usr/bin/python3
from operator import xor
'''
if 1 and
if 2 or
if 3 xor
if 4 not or
if 5 not and
'''
output = "" 

lst = []
bulbs = []
x = input().replace(" ","")

for sw in range(int(x[0])):

    swi = input()
    lst += swi[2]

for bu in range(int(x[1])):

    bul = input()
    bulbs += bul[2]

for ga in range(int(x[2])):

    z = input().replace(" ", "")
    var1 = int(lst[int(z[1])-1])
    var2 = int(lst[int(z[2])-1])
    
    if z[3] == '1':
        lst += str( var1 and var2 )

    elif z[3] == '2':
        lst += str( var1 or var2)

    elif z[3] == '3':
        lst += str(xor(var1, var2))

    elif z[3] == '4':
        add = var1 or var2
        lst += str(1 - add)

    else:
        add = var1 and var2
        lst += str(1 - add)

for element in bulbs:

    output += lst[int(element)-1] + ' '

print(output.rstrip())
