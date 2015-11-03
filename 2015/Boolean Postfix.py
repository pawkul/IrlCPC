from operator import xor

num1 = int(input())
aa = ''
for _ in range(num1):

    x = input().split(' ')
    lst = []
    
    for e in range(int(x[0])):

        
        if x[1:][e] in ['0','1']:
            lst.append(x[1:][e])

        else:
            if x[1:][e] == 'N':
                p1 = lst.pop()
                if int(p1):
                    lst.append('0')
                else:
                    lst.append('1')

            elif x[1:][e] == 'A':
                p1 = lst.pop()
                p2 = lst.pop()
                d = int(p2) and int(p1)
                lst.append(d)

            elif x[1:][e] == 'R':
                p1 = lst.pop()
                p2 = lst.pop()
                d = int(p2) or int(p1)
                lst.append(d)

            else:
                p1 = lst.pop()
                p2 = lst.pop()
                d = xor(int(p2),int(p1))
                lst.append(d)
    aa += str(lst[0])
    aa += '\n'

print(aa)
