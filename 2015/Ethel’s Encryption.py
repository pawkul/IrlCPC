#!/bin/usr/python3
b = [int(x) for x in input().split(' ')]
c = [x for x in input()]
new_string = ""
move = (b[1]**b[2])

move = move % 26

for num in range(b[0]):
   if c[num] == " ":
      new_string += " "

   else:
      if ord(c[num]) - move < 65:
         diff = ord(c[num]) - 64
         to_add = chr(90 - (move - diff))
         new_string += to_add

      else:
         to_add = chr(ord(c[num]) - move)
         new_string += to_add

print(new_string)
