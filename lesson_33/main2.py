a = input()
perexod = 0
uborka = 0
while perexod != len(a) - 1:
    if a[perexod] == a[perexod+1]:
        a = a[:perexod]+a[perexod+1:]
        uborka+=1
    else:
        perexod+=1
print(uborka)