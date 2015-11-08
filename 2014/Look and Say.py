a = [x for x in input().split(" ")]
s = a[0]
x = ""

for _ in range(1, int(a[1])):
    counter = 0
    el = s[0]

    for num in range(len(s)):

        if s[num] == el:
            counter += 1
            if num >= len(s) - 1:
                x += (str(counter)+el)

        else:
            if counter == 0:
                x += ("1" + el)
                el = s[num]
                counter = 1

            else:
                x += (str(counter)+el)
                counter = 1
                el = s[num]
                if num >= len(s) - 1:
                    x += ("1" + el)

    s = x
    x = ""
print(s)
