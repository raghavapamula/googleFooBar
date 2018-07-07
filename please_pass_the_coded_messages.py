def answer(l):
    # your code here
    l.sort(reverse = True)
    mods = {}
    
    for i in range(len(l)):
        try:
            mods[l[i]%3].append(l[i])
        except:
            mods[l[i]%3] = [l[i]]

    while(sum(l) % 3 > 0):
        temp = sum(l) % 3
        try:
            l.pop(l.index(mods[temp].pop()))
        except:
            if(temp == 1):
                l.pop(l.index(mods[2].pop()))
                l.pop(l.index(mods[2].pop()))
            elif(temp == 2):
                l.pop(l.index(mods[1].pop()))
                l.pop(l.index(mods[1].pop()))
    if(len(l) == 0):
        return 0
    return int(''.join(list(map(lambda x: str(x), l))))
    
print(answer([3, 1, 4, 1, 5, 9]))
