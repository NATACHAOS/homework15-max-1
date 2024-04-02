list_ = [14, 15, 11, 12, 13]
list_.sort()
print(list_[-1])

r1 = 14
r2 = 15
r3 = 11
r4 = 12
r5 = 13

l = True
while l:
    if r1 < r2:
        r1, r2 = r2, r1
    elif r2 < r3:
        r2, r3 = r3, r2
    elif r3 < r4:
        r3, r4 = r4, r3
    elif r4 < r5:
        r4, r5 = r5, r4
    if (r1 >= r2) and (r2 >= r3) and (r3 >= r4) and (r4 >= r5):
        l = False
print(r1, r2, r3, r4, r5, end='')
print()

print(sorted(list_)[::-1])
