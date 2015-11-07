a = int(str(input()),2)

x = 0
for _ in range(a):

    x += int(str(input()),2)


print(bin(x)[2:].zfill(32))
