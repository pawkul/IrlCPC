#!/bin/usr/python3
b = [int(x) for x in input().split(' ')]
c = [x for x in input()]
new_string = ""
move = (b[1]**b[2])

if move > 25:
    move = move%25 - 1

else:
    move = move - 1

for num in range(b[0]):
    if c[num] == ' ':
        new_string += ' '

    else:
        if ord(c[num]) - move < 65:
            new_string +=  chr(90 - (move - (ord(c[num]) - 64)))
        else:
            new_string += chr(ord(c[num])-move)

print(new_string)
